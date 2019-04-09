import numpy as np
import matplotlib.pyplot as plt

from delfi.distribution import Uniform
from delfi.generator import Default
from delfi.inference import SNPE

from dap.utils import (obs_params, syn_obs_stats, syn_obs_data,
                       load_current, load_prior_ranges, syn_current)
from dap.dap_sumstats import DAPSummaryStats
from dap.dap_simulator import DAPSimulator
from dap import DAPcython


# General Settings Pick
n_rounds = 1
n_params = 4
n_summary = 17
n_samples = 10
n_hiddens = [30]
n_components = 1
dt = 0.01
reg_lambda = 0.01

# Load the current
# data_dir = '/home/ateska/Desktop/LFI_DAP/data/rawData/2015_08_26b.dat'    # best cell
# protocol = 'rampIV' # 'IV' # 'rampIV' # 'Zap20'
# ramp_amp = 3.1
# I, v, t, t_on, t_off, dt = load_current(data_dir, protocol=protocol, ramp_amp=ramp_amp)
I, t, t_on, t_off = syn_current(duration=50, dt=0.01, t_on=15, t_off=20, amp=3.1)

# Set up themodel
params, labels = obs_params(reduced_model=True)
dap = DAPcython(-75, params)
U = dap.simulate(dt, t, I)

# generate data format for SNPE / OBSERVABLE
x_o =  {'data': U.reshape(-1),
        'time': t,
        'dt': dt,
        'I': I}

# Setup Priors
prior_min, prior_max, labels = load_prior_ranges(n_params)
prior_unif = Uniform(lower=prior_min, upper=prior_max)

print(prior_min)
print(prior_max)
print(labels)

# Summary Statistics
S = syn_obs_stats(x_o['I'], params=params, dt=x_o['dt'], t_on=t_on, t_off=t_off,
                  n_summary=n_summary, summary_stats=0, data=x_o)


M = DAPSimulator(x_o['I'], x_o['dt'], -75)
s = DAPSummaryStats(t_on, t_off, n_summary=n_summary)
G = Default(model=M, prior=prior_unif, summary=s)  # Generator

# Runing the simulation
inf_snpe = SNPE(generator=G, n_components=n_components, n_hiddens=n_hiddens, obs=S,
                reg_lambda=reg_lambda, pilot_samples=0, prior_norm=True)

logs, tds, posteriors = inf_snpe.run(n_train=[n_samples], n_rounds=n_rounds,
                                     proposal=prior_unif)


# Analyse results
samples_prior = prior_unif.gen(n_samples=int(5e5))
samples_posterior = posteriors[-1].gen(n_samples=int(5e5))

print('posterior:', posteriors[-1].mean)


x_post = syn_obs_data(I, dt, posteriors[-1].mean)

simulation, axes = plt.subplots(2, 1, figsize=(16, 14))
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
axes[1].annotate(labels[0]+': '+str(round(posteriors[-1].mean[1], 3)),
                   xy=(1, 0), xycoords='axes fraction', fontsize=12,
                   xytext=(-5, 5), textcoords='offset points',
                   ha='right', va='bottom')
axes[2].annotate(labels[0]+': '+str(round(posteriors[-1].mean[2], 3)),
                   xy=(1, 0), xycoords='axes fraction', fontsize=12,
                   xytext=(-5, 5), textcoords='offset points',
                   ha='right', va='bottom')

plt.figure()
plt.plot(logs[0]['loss'])

plt.show()
