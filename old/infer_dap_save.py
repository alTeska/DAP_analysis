import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils_analysis import simulate_data_distr, logs_to_plot
from delfi.distribution import Uniform
from delfi.generator import Default
from delfi.inference import SNPE, Basic, CDELFI

from dap.utils import prior, obs_params, syn_obs_stats, syn_obs_data
from dap.dap_sumstats import DAPSummaryStats
from dap.dap_simulator import DAPSimulator
from dap.cell_fitting.read_heka import (get_sweep_index_for_amp,
                                             get_i_inj_from_function)
from dap.cell_fitting.read_heka import get_v_and_t_from_heka, shift_v_rest

# General Settings Pick
n_rounds = 1
n_summary = 10
n_samples = 2000
n_hiddens = [200, 200]
n_components = 1

name = '_ss999_4x4neur_3x4k'
direct_out = 'plots/dap_models' + name + '/'


# Setup Priors
prior_min = np.array([0, 1 ])
prior_max = np.array([2, 30])

prior_unif = Uniform(lower=prior_min, upper=prior_max)
# prior_gauss = prior(prior_max)

# Load the data
data_dir = '/home/alteska/Desktop/LFI_DAP/data/rawData/2015_08_26b.dat'    # best cell
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

params, labels = obs_params(reduced_model=True)


# Summary Statistics
S = syn_obs_stats(x_o['I'], params=params, dt=x_o['dt'], t_on=t_on, t_off=t_off,
                  n_summary=n_summary, summary_stats=1, data=x_o)


M = DAPSimulator(x_o['I'], x_o['dt'], -75)
s = DAPSummaryStats(t_on, t_off, n_summary=n_summary)
G = Default(model=M, prior=prior_unif, summary=s)  # Generator

# Runing the simulation
# inf_snpe = SNPE(generator=G, n_components=n_components, n_hiddens=n_hiddens, obs=S,
#                 pilot_samples=10, prior_norm=True)

inf_snpe = SNPE(generator=G, n_components=n_components, n_hiddens=n_hiddens, obs=S,
                pilot_samples=10, prior_norm=True)



logs, tds, posteriors = inf_snpe.run(n_train=[n_samples], n_rounds=n_rounds,
                                     proposal=prior_unif, monitor=observables)

# Analyse results
samples_prior = prior_unif.gen(n_samples=int(5e5))
samples_posterior = posteriors[-1].gen(n_samples=int(5e5))

# Plots
print('posterior:', posteriors[-1].mean)
# posterior = posteriors[-1]
# plt.plot(posterior.eval(np.arange(-5.0, 5.0, 0.01).reshape(-1,1), log=False), '-b')

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

axes[0].annotate(labels[0]+': '+str(round(posteriors[-1].mean[0], 2)),
                   xy=(1, 0), xycoords='axes fraction', fontsize=12,
                   xytext=(-5, 5), textcoords='offset points',
                   ha='right', va='bottom')
axes[1].annotate(labels[0]+': '+str(round(posteriors[-1].mean[1], 2)),
                   xy=(1, 0), xycoords='axes fraction', fontsize=12,
                   xytext=(-5, 5), textcoords='offset points',
                   ha='right', va='bottom')


plt.show()

# # Create Weights Plots
# print('Generating Plots')
#
# if not os.path.exists(direct_out):
#     print('creating output directory')
#     os.makedirs(direct_out)
#
# g_loss = logs_to_plot(logs, 'loss')
# g_meansW0 = logs_to_plot(logs, 'means.mW0', melted=True)
# g_precisionsW0 = logs_to_plot(logs, 'precisions.mW0', melted=True)
# g_h1W = logs_to_plot(logs, 'h1.mW', melted=True)
#
# # Create Biases Plots
# g_meansb0 = logs_to_plot(logs, 'means.mb0', melted=True)
# g_precisionsb0 = logs_to_plot(logs, 'precisions.mb0', melted=True)
# g_h1b = logs_to_plot(logs, 'h1.mb', melted=True)

# # Saving plots
# print('Saving Plots')
# simulation.savefig(direct_out + 'simulation.png', bbox_inches='tight')
# distr_comb.savefig(direct_out + 'distr_comb.png', bbox_inches='tight')
#
# g_loss.savefig(direct_out + 'loss.png', bbox_inches='tight')
# g_meansW0.savefig(direct_out + 'meansW0.png', bbox_inches='tight')
# g_precisionsW0.savefig(direct_out + 'precisionsW0.png', bbox_inches='tight')
# g_h1W.savefig(direct_out + 'h1W.png', bbox_inches='tight')
#
# g_meansb0.savefig(direct_out + 'meansb0.png', bbox_inches='tight')
# g_precisionsb0.savefig(direct_out + 'precisionsb0.png', bbox_inches='tight')
# g_h1b.savefig(direct_out + 'h1b.png', bbox_inches='tight')
#
#
# # Save hyperparameters
# hyper = {
#     'name': name,
#     'n_rounds' : n_rounds,
#     'n_summary': n_summary,
#     'n_samples' : n_samples,
#     'n_hidden' : str(n_hiddens),
#     'n_components': n_components,
#     'protocol': protocol,
#     'ramp_amp': ramp_amp,
#     'prior_min': str([0, 1]),
#     'prior_max': str([0.5, 30]),
# }
#
# hyperparams = pd.DataFrame(hyper, index=[0])
# hyperparams.to_csv(path_or_buf=direct_out)
