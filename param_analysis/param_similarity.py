import glob
import shutil
import pandas as pd

from dap import DAPcython
from dap.utils import obs_params, load_current
from tqdm import tqdm
from scipy.spatial import distance


dt = 1e-2
params, labels = obs_params(reduced_model=False)
data_dir = '/home/alteska/Desktop/LFI_DAP/data/rawData/2015_08_26b.dat'

# load the file
directory = './parameters/'
dir = glob.glob(directory + '*')

fname_start = dir[0].find('dap_')
fname_stop = dir[0].find('n_')
fname = dir[0][fname_start:fname_stop] + '.csv'

df_param = pd.read_csv(fname)


# calculate DAP
# load the input data
Ir, vr, tr, t_onr, t_offr, dtr = load_current(data_dir, protocol='rampIV', ramp_amp=3.1)
Is, vs, ts, t_ons, t_offs, dts = load_current(data_dir, protocol='IV', ramp_amp=1)

# define a model
dap = DAPcython(-75, params)

# run models on original parameters
U_step = dap.simulate(dts, ts, Is)
U_ramp = dap.simulate(dtr, tr, Ir)

# calculate the similarities
d_step = distance.euclidean(vs, U_step)
d_ramp = distance.euclidean(vr, U_ramp)

# run for all cells and save into the the DF
df_paramT = df_param.transpose()
df_paramT.head()
df_paramT.drop('Unnamed: 0', inplace=True)

for i, j in tqdm(df_paramT.iterrows()):
    # get parameters
    par_temp = j.values

    print(par_temp)

    # define a model
    dap = DAPcython(-75, j)

    # run model
    U_step_x = dap.simulate(dts, ts, Is)
    U_ramp_x = dap.simulate(dtr, tr, Ir)

    # calculate distance for both currents
    dis_step = distance.euclidean(vs, U_step_x)
    dis_ramp = distance.euclidean(vr, U_ramp_x)

    # save into new columns
    df_paramT.loc[i, 'distance_ramp'] = dis_ramp
    df_paramT.loc[i, 'distance_step'] = dis_step
    df_paramT.loc[i, 'distance_sum'] = dis_ramp + dis_step

# save the new data DataFrame
df_paramT.to_csv(fname[:-4] + '_similarity.csv')

# remove the temp directory
shutil.rmtree(directory)
