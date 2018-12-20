import argparse, os, sys
import numpy as np
import matplotlib.pyplot as plt
from delfi.inference import SNPE
from delfi.generator import Default
from delfi.utils.io import save, save_pkl

from DAPmodel.DAPsumstats import DAPSummaryStats
from DAPmodel.DAPSumStatsNoAP import DAPSummaryStatsNoAP
from DAPmodel.DAPSumStats import DAPSummaryStatsA

from DAPmodel.DAPsimulator import DAPSimulator

from DAPmodel.utils import obs_params, syn_obs_data, prior, syn_obs_stats
from utils_analysis import plot_distr, plot_distr_multiple, simulate_data_distr


from DAPmodel.cell_fitting.read_heka import get_sweep_index_for_amp, get_i_inj_from_function
from DAPmodel.cell_fitting.read_heka import get_v_and_t_from_heka, shift_v_rest


parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="file name")
parser.add_argument("-ns", "--n_samples",
                    help="number of samples per round")

args = parser.parse_args()

if args.name  is None: args.name = ''
if args.n_samples is None: args.n_samples = '10'

directory = 'pickle/dap_model' + args.name
direct_out = 'plots/dap_models' + args.name + '/'

if not os.path.exists(directory):
    print('creating directory')
    os.makedirs(directory)

if not os.path.exists(direct_out):
    print('creating output directory')
    os.makedirs(direct_out)

n_samples = int(args.n_samples)
n_rounds = 1
dt = 0.01

summary_stats_type = 1
n_summary = 8

# load the data
data_dir = '/home/ateska/Desktop/LFI_DAP/data/rawData/2015_08_26b.dat'    # best cell
protocol = 'rampIV' # 'IV' # 'rampIV' # 'Zap20'
ramp_amp = 3.1 # steps of 0.05 -0.15
v_shift = -16  # shift for accounting for the liquid junction potential

if protocol == 'Zap20':
    sweep_idx = 0
else:
    sweep_idx = get_sweep_index_for_amp(ramp_amp, protocol)

v, t = get_v_and_t_from_heka(data_dir, protocol, sweep_idxs=[sweep_idx])
v = shift_v_rest(v[0], v_shift)
t = t[0]
i_inj, t_on, t_off = get_i_inj_from_function(protocol, [sweep_idx], t[-1], t[1]-t[0],
                                             return_discontinuities=False)


# generate data format for SNPE
x_o =  {'data': v,
        'time': t,
        'dt': t[1]-t[0],
        'I': i_inj[0]}


# picking experiments observables
observables = {'loss.lprobs', 'imputation_values', 'h1.mW', 'h1.mb', 'h2.mW',
               'h2.mb', 'weights.mW', 'weights.mb', 'means.mW0', 'means.mW1',
               'means.mb0', 'means.mb1', 'precisions.mW0', 'precisions.mW1',
               'precisions.mb0', 'precisions.mb1'}

# setting up parameters
params, labels = obs_params()

params = np.array([0.1, 15])
prior = prior(params, prior_log=False, prior_uniform=False)

S = syn_obs_stats(x_o['I'], params=params, dt=x_o['dt'], t_on=t_on, t_off=t_off,
                  n_summary=n_summary, summary_stats=summary_stats_type, data=x_o)


M = DAPSimulator(x_o['I'], x_o['dt'], -75)

if summary_stats_type == 0:
    s = DAPSummaryStats(t_on, t_off, n_summary=n_summary)
elif summary_stats_type == 1:
    s = DAPSummaryStatsA(t_on, t_off, n_summary=n_summary)
elif summary_stats_type == 2:
    s = DAPSummaryStatsNoAP(t_on, t_off, n_summary=n_summary)
else:
    raise ValueError('Only 0, 1, 2 as an option for summary statistics.')

sum_stats = DAPSummaryStatsA(t_on, t_off, n_summary=8)


G = Default(model=M, prior=prior, summary=sum_stats)  # Generator


# Runing the simulation
inf_snpe = SNPE(generator=G, n_components=1, n_hiddens=[2], obs=S,
                pilot_samples=10)

logs, tds, posteriors = inf_snpe.run(n_train=[n_samples], n_rounds=n_rounds,
                                     monitor=observables, round_cl=1)


# Analyse results
print('expected mean, std', expected.mean, expected.std)
print('posterior mean, std', posteriors[-1].mean, posteriors[-1].std)


# Saving Data into pickle files
posterior_sampl = simulate_data_distr(posteriors[-1], M, sum_stats, n_samples=1)

print('Saving Data')
sys.setrecursionlimit(10000)
# save(inf_snpe, directory + '/dap_snpe' + args.name)

save_pkl(x_o['I'], directory + '/dap_I' + args.name)
save_pkl(x_o['dt'], directory + '/dap_dt' + args.name)
save_pkl(t_on, directory + '/dap_t_on' + args.name)
save_pkl(t_off, directory + '/dap_t_off' + args.name)

save_pkl(M, directory + '/dap_model' + args.name)
save_pkl(sum_stats, directory + '/dap_stats' + args.name)
save_pkl(S, directory + '/dap_stats_data' + args.name)
save_pkl(G, directory + '/dap_gen' + args.name)

save_pkl(logs, directory + '/dap_logs' + args.name)
save_pkl(tds, directory + '/dap_tds' + args.name)
save_pkl(posteriors, directory + '/dap_posteriors' + args.name)
save_pkl(expected, directory + '/dap_expected' + args.name)
save_pkl(params, directory + '/dap_params' + args.name)
save_pkl(labels, directory + '/dap_labels' + args.name)
