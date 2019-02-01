import os
import numpy as np
import matplotlib.pyplot as plt

from delfi.distribution import Uniform
from delfi.generator import Default
from delfi.inference import SNPE  # , Basic, CDELFI

from dap.utils import obs_params_gbar, syn_obs_stats, syn_obs_data, syn_current
from dap.dap_sumstats import DAPSummaryStats
from dap.dap_sumstats_moments import DAPSummaryStatsMoments
from dap.dap_simulator import DAPSimulator
from dap import DAPcython
from dap.cell_fitting.read_heka import (get_sweep_index_for_amp,
                                             get_i_inj_from_function)
from dap.cell_fitting.read_heka import get_v_and_t_from_heka, shift_v_rest

# General Settings Pick
n_rounds = 1
n_summary = 17
n_samples = 10
n_hiddens = [20]
n_components = 1
reg_lambda = 0.01


name = '_4x4neur_3x4k'
direct_out = 'plots/dap_models' + name + '/'

if not os.path.exists(direct_out):
    print('creating output directory')
    os.makedirs(direct_out)

# Load the current
data_dir = '/home/ateska/Desktop/LFI_DAP/data/rawData/2015_08_26b.dat'    # best cell
protocol = 'rampIV' # 'IV' # 'rampIV' # 'Zap20'
ramp_amp = 3.1 # steps of 0.05 -0.15
v_shift = -16  # shift for accounting for the liquid junction potential

sweep_idx = get_sweep_index_for_amp(ramp_amp, protocol)

v, t = get_v_and_t_from_heka(data_dir, protocol, sweep_idxs=[sweep_idx])
v = shift_v_rest(v[0], v_shift)
t = t[0]
dt = t[1] - t[0]
I, t_on, t_off = get_i_inj_from_function(protocol, [sweep_idx], t[-1], t[1]-t[0],
                                             return_discontinuities=False)
I=I[0]

params, labels = obs_params_gbar(reduced_model=False)

print(params)
print(labels)

# Set up themodel
dap = DAPcython(-75, params*10)
U = dap.simulate(dt, t, I)

# generate data format for SNPE / OBSERVABLE
x_o = {'data': v.reshape(-1),
       'time': t,
       'dt': dt,
       'I': I}

# Setup Priors
prior_min = np.array([0, 0, 0])
prior_max = np.array([2, 2, 2])
prior_unif = Uniform(lower=prior_min, upper=prior_max)

# Summary Statistics
S = syn_obs_stats(x_o['I'], params=params, dt=x_o['dt'], t_on=t_on, t_off=t_off,
                  n_summary=n_summary, summary_stats=2, data=x_o)


M = DAPSimulator(x_o['I'], x_o['dt'], -75)
s = DAPSummaryStatsMoments(t_on, t_off, n_summary=n_summary)
G = Default(model=M, prior=prior_unif, summary=s)  # Generator

# Runing the simulation
inf_snpe = SNPE(generator=G, n_components=n_components, n_hiddens=n_hiddens, obs=S,
                # reg_lambda=reg_lambda, pilot_samples=0, prior_norm=True)
                reg_lambda=reg_lambda, pilot_samples=0)

logs, tds, posteriors = inf_snpe.run(n_train=[n_samples], n_rounds=n_rounds,
                                     proposal=prior_unif)


# Analyse results
samples_prior = prior_unif.gen(n_samples=int(5e5))
samples_posterior = posteriors[-1].gen(n_samples=int(5e5))

print('posterior:', posteriors[-1].mean)


x_post = syn_obs_data(I, dt, posteriors[-1].mean)
idx = np.arange(0, len(x_o['data']))
rmse = np.linalg.norm(x_o['data'] - x_post['data']) / len(x_o['data'])

print('RMSE:', rmse)

simulation, axes = plt.subplots(2, 1, figsize=(16,14))
axes[0].plot(idx, x_o['I'], c='g', label='goal')
axes[0].plot(idx, x_post['I'], label='posterior')
axes[0].set_title('current')
axes[0].legend()

axes[1].step(idx, x_o['data'], c='g', label='goal')
axes[1].step(idx, x_post['data'], label='posterior')
axes[1].set_title('Voltage trace')
axes[1].legend()


distr_comb, axes = plt.subplots(3, 1, figsize=(16, 14))
axes[0].hist(samples_prior[:, 0], bins='auto', label='prior')
axes[1].hist(samples_prior[:, 1], bins='auto', label='prior')
axes[2].hist(samples_prior[:, 2], bins='auto', label='prior')
axes[0].hist(samples_posterior[:, 0], bins='auto', label='posterior')
axes[1].hist(samples_posterior[:, 1], bins='auto', label='posterior')
axes[2].hist(samples_posterior[:, 2], bins='auto', label='posterior')
axes[0].legend()
axes[1].legend()
axes[2].legend()

axes[0].annotate(labels[0]+': '+str(round(posteriors[-1].mean[0], 3)),
                   xy=(1, 0), xycoords='axes fraction', fontsize=12,
                   xytext=(-5, 5), textcoords='offset points',
                   ha='right', va='bottom')
axes[1].annotate(labels[1]+': '+str(round(posteriors[-1].mean[1], 3)),
                   xy=(1, 0), xycoords='axes fraction', fontsize=12,
                   xytext=(-5, 5), textcoords='offset points',
                   ha='right', va='bottom')

axes[2].annotate(labels[2]+': '+str(round(posteriors[-1].mean[1], 3)),
                   xy=(1, 0), xycoords='axes fraction', fontsize=12,
                   xytext=(-5, 5), textcoords='offset points',
                   ha='right', va='bottom')


loss, ax = plt.subplots(1,1)
ax.plot(logs[0]['loss'])



loss.savefig(direct_out + 'loss.png', bbox_inches='tight')
distr_comb.savefig(direct_out + 'distr_comb.png', bbox_inches='tight')
simulation.savefig(direct_out + 'simulation.png', bbox_inches='tight')

#
# plt.show()
