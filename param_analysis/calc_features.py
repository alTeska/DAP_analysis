import glob
import shutil
import pandas as pd

from tqdm import tqdm
from scipy.spatial import distance
from dap import DAPcython
from dap.utils import obs_params, load_current
from utils import calc_features_ramp, calc_features_step, find_spikes


dt = 1e-2
params, labels = obs_params(reduced_model=False)
data_dir = '/home/alteska/Desktop/LFI_DAP/data/rawData/2015_08_26b.dat'

# load the file
directory = './parameters/'
dir = glob.glob(directory + '*')

fname_start = dir[0].find('dap_')
fname_stop = dir[0].find('n_')
fname = dir[0][fname_start:fname_stop]

df_param = pd.read_csv(fname + '.csv')
df_param.set_index('Unnamed: 0', inplace=True)

# calculate DAP
# load the input data
Ir, vr, tr, t_onr, t_offr, dtr = load_current(data_dir, protocol='rampIV', ramp_amp=3.1)
Is, vs, ts, t_ons, t_offs, dts = load_current(data_dir, protocol='IV', ramp_amp=1)

# get traces for both currents
U_steps, U_ramps = [], []

for i, j in tqdm(df_param.iterrows()):
    # get parameters
    par_temp = j.values

    # define a model
    dap = DAPcython(-75, j)

    # run model
    U_step_x = dap.simulate(dts, ts, Is)
    U_ramp_x = dap.simulate(dtr, tr, Ir)

    # run model
    U_steps.append(U_step_x.transpose()[0])
    U_ramps.append(U_ramp_x.transpose()[0])

    # calculate distance for both currents
    dis_step = distance.euclidean(vs, U_step_x)
    dis_ramp = distance.euclidean(vr, U_ramp_x)

    # save into new columns
    df_param.loc[i, 'distance_ramp'] = dis_ramp
    df_param.loc[i, 'distance_step'] = dis_step
    df_param.loc[i, 'distance_sum'] = dis_ramp + dis_step

# create DataFrames for traces
df_step = pd.DataFrame({'step_traces': U_steps})
df_step.set_index(df_param.index.values, inplace=True)

df_ramp = pd.DataFrame({'ramp_traces': U_ramps})
df_ramp.set_index(df_param.index.values, inplace=True)
df_traces_temp = pd.merge(df_param, df_step, how='left', left_index=True, right_index=True)
df_traces = pd.merge(df_traces_temp, df_ramp, how='left', left_index=True, right_index=True)

# Calculate Statistics for Ramp and Step currents
step_features_labels = ['rest_pot', 'rest_pot_std','firing_rate', 'ISI_mean', 'ISI_std', 'spike_count', 'spike_times_stim']
ramp_features_labels = ['rest_pot', 'AP_amp', 'AP_width', 'fAHP', 'DAP_amp', 'DAP_width', 'DAP_deflection','DAP_time', 'mAHP']

stats_step = []
for i,u in enumerate(U_steps):
    stats = calc_features_step(u, ts, dts, t_ons, t_offs)
    stats_step.append(stats)

stats_ramp = []
for i,u in enumerate(U_ramps):
    stats = calc_features_ramp(u, tr, dtr, t_onr, t_offr)
    stats_ramp.append(stats)

# change into data frame
df_ramps = pd.DataFrame(data=stats_ramp, columns=ramp_features_labels, index=df_param.index)
df_steps = pd.DataFrame(data=stats_step, columns=step_features_labels, index=df_param.index)


# save to HDF file
df_steps.to_hdf(fname + '.hdf', key='step_features')
df_ramps.to_hdf(fname + '.hdf', key='ramp_features')
df_traces.to_hdf(fname + '.hdf', key='param_traces')

# remove the temp directory
shutil.rmtree(directory)
