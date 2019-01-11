import numpy as np
import matplotlib.pyplot as plt

from utils_analysis import plot_distr_multiple, simulate_data_distr

from delfi.distribution import Uniform, Gaussian
from delfi.generator import Default
from delfi.inference import SNPE

from dap.utils import prior, obs_params, syn_obs_stats, syn_obs_data
from dap.dap_sumstats import DAPSummaryStats
from dap.dap_simulator import DAPSimulator
from dap.cell_fitting.read_heka import (get_sweep_index_for_amp,
                                             get_i_inj_from_function)
from dap.cell_fitting.read_heka import get_v_and_t_from_heka, shift_v_rest

# General Settings Pick
n_rounds = 1
n_summary = 7
n_samples = 1000

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
s = DAPSummaryStats(t_on, t_off, n_summary=n_summary)
G = Default(model=M, prior=prior_unif, summary=s)  # Generator

# Runing the simulation
inf_snpe = SNPE(generator=G, n_components=1, n_hiddens=[2], obs=S,
                pilot_samples=10, prior_norm=True)

logs, tds, posteriors = inf_snpe.run(n_train=[n_samples], n_rounds=n_rounds, proposal=prior_unif)

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


distr, axes = plt.subplots(2, 2, figsize=(16, 14))

axes[0, 0].hist(samples_prior[:, 0], bins='auto')
axes[1, 0].hist(samples_prior[:, 1], bins='auto')
axes[0, 1].hist(samples_posterior[:, 0], bins='auto')
axes[1, 1].hist(samples_posterior[:, 1], bins='auto')
axes[0, 0].set_title('prior')
axes[1, 0].set_title('prior')
axes[0, 1].set_title('posterior')
axes[1, 1].set_title('posterior')

distr, axes = plt.subplots(2, 1, figsize=(16, 14))
axes[0].hist(samples_prior[:, 0], bins='auto', label='prior')
axes[1].hist(samples_prior[:, 1], bins='auto', label='prior')
axes[0].hist(samples_posterior[:, 0], bins='auto', label='posterior')
axes[1].hist(samples_posterior[:, 1], bins='auto', label='posterior')
axes[0].legend()
axes[1].legend()

axes[0].set_title('both')
axes[1].set_title('both')

plt.show()
