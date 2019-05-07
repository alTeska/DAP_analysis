import glob
import numpy as np
import pandas as pd
from tqdm import tqdm
from dap import DAPcython
from dap.utils import obs_params, load_current


dt = 1e-2
params, labels = obs_params(reduced_model=False)
data_dir = '/home/alteska/Desktop/LFI_DAP/data/rawData/2015_08_26b.dat'

# load the input data
Ir, vr, tr, t_onr, t_offr, dtr = load_current(data_dir, protocol='rampIV', ramp_amp=3.1)
Is, vs, ts, t_ons, t_offs, dts = load_current(data_dir, protocol='IV', ramp_amp=1)

# load the file
directory = './parameters/'

# load the data
dir = glob.glob(directory + '*')

# create variables name based on n_samples
dir_name = []
for n in dir:
    x = n.find('dap_')
    n = n[x:-4]
    dir_name.append(n)

# get parameters label
param_labels = pd.read_csv(dir[0])['Unnamed: 0'].values

# load parameters into arrays
for i, d in enumerate(dir):
    vars()[dir_name[i]] = pd.read_csv(d)['mean param'].values

# build a common array
parameter_matrix = np.zeros_like(param_labels)

for n in dir_name:
    x = vars()[n]
    parameter_matrix = np.vstack([parameter_matrix, x])

# create df columns name based on n_samples
col_names = []
for n in dir:
    x = n.find('n_')
    n = n[x+2:-4]
    col_names.append(n)

# create and save dataframe
df_param = pd.DataFrame(data=parameter_matrix[1:].T, columns=col_names)
df_param.set_axis(param_labels, inplace=True)
df_param = df_param.transpose()


fname_start = dir[0].find('dap_')
fname_stop = dir[0].find('n_')
fname = dir[0][fname_start:fname_stop]

# run for all cells and save into the the DF
daps = []
U_steps = []
U_ramps = []

for i, j in tqdm(df_param.iterrows()):
    # get parameters

    par_temp = j.values

    # define a model
    dap = DAPcython(-75, j)
    daps.append(dap)

    # run model
    U_steps.append(dap.simulate(dts, ts, Is).transpose()[0])
    U_ramps.append(dap.simulate(dtr, tr, Ir).transpose()[0])


# merge traces into one result dataframe
df_arr_step = pd.DataFrame({'step_traces': U_steps})
df_arr_step.set_index(df_param.index.values, inplace=True)

df_arr_ramp = pd.DataFrame({'ramp_traces': U_ramps})
df_arr_ramp.set_index(df_param.index.values, inplace=True)

result = pd.merge(df_param, df_arr_step, how='left', left_index=True, right_index=True)
result = pd.merge(result, df_arr_ramp, how='left', left_index=True, right_index=True)

# save data frames
df_param.to_csv(fname + '.csv')
result.to_csv(fname + '_traces.csv')
