import argparse, os, sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils_analysis import logs_to_plot
from delfi.distribution import Uniform
from delfi.generator import Default
from delfi.inference import SNPE
from delfi.utils.io import save_pkl

from DAPmodel.utils import prior, obs_params, syn_obs_stats, syn_obs_data
from DAPmodel.DAPSumStats import DAPSummaryStatsA
from DAPmodel.DAPsimulator import DAPSimulator
from DAPmodel.cell_fitting.read_heka import (get_sweep_index_for_amp,
                                             get_i_inj_from_function)
from DAPmodel.cell_fitting.read_heka import get_v_and_t_from_heka, shift_v_rest


# General Settings Pick
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="file name")
parser.add_argument("-ns", "--n_samples",
                    help="number of samples per round")
parser.add_argument("-nr", "--n_rounds",
                    help="number of rounds")

args = parser.parse_args()

if args.name  is None: args.name = ''
if args.n_samples is None: args.n_samples = '10'
if args.n_rounds is None: args.n_rounds = '1'

directory = 'pickle/dap_model' + args.name
direct_out = 'plots/dap_models' + args.name + '/'

if not os.path.exists(directory):
    print('creating directory')
    os.makedirs(directory)

if not os.path.exists(direct_out):
    print('creating output directory')
    os.makedirs(direct_out)

n_samples = int(args.n_samples)
n_rounds = int(args.n_rounds)

n_hiddens = [4,4]
n_summary = 7
n_components = 1


# Setup Priors
prior_min = np.array([0, 1])
prior_max = np.array([0.5, 30])

prior_unif = Uniform(lower=prior_min, upper=prior_max)
prior_gauss = prior(prior_max)

# Load the data
data_dir = '/home/ateska/Desktop/LFI_DAP/data/rawData/2015_08_26b.dat'    # best cell
protocol = 'rampIV' # 'IV' # 'rampIV' # 'Zap20'
ramp_amp = 3.1 # steps of 0.05 -0.15
v_shift = -16  # shift for accounting for the liquid junction potential

sweep_idx = get_sweep_index_for_amp(ramp_amp, protocol)

v, t = get_v_and_t_from_heka(data_dir, protocol, sweep_idxs=[sweep_idx])
v = shift_v_rest(v[0], v_shift)
t = t[0]
dt = t[1] - t[0]
i_inj, t_on, t_off = get_i_inj_from_function(protocol, [sweep_idx], t[-1], t[1]-t[0],
                                             return_discontinuities=False)

# picking experiments observables
observables = {'loss.lprobs', 'imputation_values', 'h1.mW', 'h1.mb', 'h2.mW',
               'h2.mb', 'weights.mW', 'weights.mb', 'means.mW0', 'means.mW1',
               'means.mb0', 'means.mb1', 'precisions.mW0', 'precisions.mW1',
               'precisions.mb0', 'precisions.mb1'}

# generate data format for SNPE / OBSERVABLE
x_o =  {'data': v,
        'time': t,
        'dt': t[1]-t[0],
        'I': i_inj[0]}

params, labels = obs_params()

# Summary Statistics
S = syn_obs_stats(x_o['I'], params=params, dt=x_o['dt'], t_on=t_on, t_off=t_off,
                  n_summary=n_summary, summary_stats=1, data=x_o)


M = DAPSimulator(x_o['I'], x_o['dt'], -75)
s = DAPSummaryStatsA(t_on, t_off, n_summary=n_summary)
G = Default(model=M, prior=prior_unif, summary=s)  # Generator

# Runing the simulation
inf_snpe = SNPE(generator=G, n_components=n_components, n_hiddens=n_hiddens, obs=S,
                pilot_samples=10, prior_norm=True)

logs, tds, posteriors = inf_snpe.run(n_train=[n_samples], n_rounds=n_rounds,
                                     proposal=prior_unif, monitor=observables)

# Analyse results
samples_prior = prior_unif.gen(n_samples=int(5e5))
samples_posterior = posteriors[-1].gen(n_samples=int(5e5))

# Plots
x_post = syn_obs_data(i_inj[0], dt, posteriors[-1].mean)
idx = np.arange(0, len(x_o['data']))

simulation, axes = plt.subplots(2, 1, figsize=(16,14))
axes[0].plot(idx, x_o['I'], c='g', label='goal')
axes[0].plot(idx, x_post['I'], label='posterior')
axes[0].set_title('current')
axes[0].legend()

axes[1].step(idx, x_o['data'], c='g', label='goal')
axes[1].step(idx, x_post['data'], label='posterior')
axes[1].set_title('Voltage trace')
axes[1].legend()

distr_comb, axes = plt.subplots(2, 1, figsize=(16, 14))
axes[0].hist(samples_prior[:, 0], bins='auto', label='prior')
axes[1].hist(samples_prior[:, 1], bins='auto', label='prior')
axes[0].hist(samples_posterior[:, 0], bins='auto', label='posterior')
axes[1].hist(samples_posterior[:, 1], bins='auto', label='posterior')
axes[0].legend()
axes[1].legend()

axes[0].set_title('both')
axes[1].set_title('both')

plt.show()

distr, axes = plt.subplots(2, 2, figsize=(16, 14))

axes[0, 0].hist(samples_prior[:, 0], bins='auto')
axes[1, 0].hist(samples_prior[:, 1], bins='auto')
axes[0, 1].hist(samples_posterior[:, 0], bins='auto')
axes[1, 1].hist(samples_posterior[:, 1], bins='auto')
axes[0, 0].set_title('prior')
axes[1, 0].set_title('prior')
axes[0, 1].set_title('posterior')
axes[1, 1].set_title('posterior')

# Create Weights Plots
print('Generating Plots')

g_loss = logs_to_plot(logs, 'loss')
g_meansW0 = logs_to_plot(logs, 'means.mW0', melted=True)
g_precisionsW0 = logs_to_plot(logs, 'precisions.mW0', melted=True)
g_h1W = logs_to_plot(logs, 'h1.mW', melted=True)

# Create Biases Plots
g_meansb0 = logs_to_plot(logs, 'means.mb0', melted=True)
g_precisionsb0 = logs_to_plot(logs, 'precisions.mb0', melted=True)
g_h1b = logs_to_plot(logs, 'h1.mb', melted=True)

# Saving plots
print('Saving Plots')
simulation.savefig(direct_out + 'simulation.png', bbox_inches='tight')
distr.savefig(direct_out + 'distr.png', bbox_inches='tight')
distr_comb.savefig(direct_out + 'distr_comb.png', bbox_inches='tight')

g_loss.savefig(direct_out + 'loss.png', bbox_inches='tight')
g_meansW0.savefig(direct_out + 'meansW0.png', bbox_inches='tight')
g_precisionsW0.savefig(direct_out + 'precisionsW0.png', bbox_inches='tight')
g_h1W.savefig(direct_out + 'h1W.png', bbox_inches='tight')

g_meansb0.savefig(direct_out + 'meansb0.png', bbox_inches='tight')
g_precisionsb0.savefig(direct_out + 'precisionsb0.png', bbox_inches='tight')
g_h1b.savefig(direct_out + 'h1b.png', bbox_inches='tight')

# Saving data
print('Saving data')
save_pkl(M, directory + '/dap_model' + args.name)
save_pkl(s, directory + '/dap_stats' + args.name)
save_pkl(S, directory + '/dap_stats_data' + args.name)
save_pkl(G, directory + '/dap_gen' + args.name)

save_pkl(logs, directory + '/dap_logs' + args.name)
save_pkl(tds, directory + '/dap_tds' + args.name)
save_pkl(posteriors, directory + '/dap_posteriors' + args.name)
save_pkl(prior, directory + '/dap_prior' + args.name)
save_pkl(params, directory + '/dap_params' + args.name)
save_pkl(labels, directory + '/dap_labels' + args.name)


# Save hyperparameters
hyper = {
    'name': name,
    'n_rounds' : n_rounds,
    'n_summary': n_summary,
    'n_samples' : n_samples,
    'n_hidden' : str(n_hiddens),
    'n_components': n_components,
    'protocol': protocol,
    'ramp_amp': ramp_amp,
    'prior_min': str([0, 1]),
    'prior_max': str([0.5, 30]),
}

hyperparams = pd.DataFrame(hyper, index=[0])
