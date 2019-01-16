import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from utils_analysis import simulate_data_distr, logs_to_plot
from delfi.distribution import Uniform
from delfi.generator import Default
from delfi.inference import SNPE, Basic, CDELFI

from dap.utils import prior, obs_params, syn_obs_stats, syn_obs_data, syn_current
from dap.dap_sumstats import DAPSummaryStats
from dap.dap_simulator import DAPSimulator
from dap import DAPcython

# General Settings Pick
n_rounds = 1
n_summary = 9
n_samples = 1
n_hiddens = [200, 200]
n_components = 1
dt = 0.01

# Get current
I, t, t_on, t_off = syn_current(duration=70, dt=0.01, t_on=15, t_off=20, amp=3.1)
params, labels = obs_params()
params[0] *= 10
print(params)

# Set up themodel
dap = DAPcython(-75, params)
U = dap.simulate(dt, t, I)

# generate data format for SNPE / OBSERVABLE
x_o =  {'data': U,
        'time': t,
        'dt': dt,
        'I': I}
# Prior
# Setup Priors
prior_min = np.array([0, 1 ])
prior_max = np.array([2, 30])

prior_unif = Uniform(lower=prior_min, upper=prior_max)

# Summary Statistics
S = syn_obs_stats(x_o['I'], params=params, dt=x_o['dt'], t_on=t_on, t_off=t_off,
                  n_summary=n_summary, summary_stats=1, data=x_o)


M = DAPSimulator(x_o['I'], x_o['dt'], -75)
s = DAPSummaryStats(t_on, t_off, n_summary=n_summary)
G = Default(model=M, prior=prior_unif, summary=s)  # Generator

# Runing the simulation
sim = Basic(generator=G, n_components=n_components, n_hiddens=n_hiddens, obs=S,
                pilot_samples=10, prior_norm=True)

logs, tds, posteriors = sim.run(n_train=[n_samples], n_rounds=n_rounds,
                                     proposal=prior_unif)


# Analyse results
samples_prior = prior_unif.gen(n_samples=int(5e5))
samples_posterior = posteriors[-1].gen(n_samples=int(5e5))

print('posterior:', posteriors[-1].mean)

x_post = syn_obs_data(I, dt, posteriors[-1].mean)
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

plt.figure()
plt.plot(logs[0]['loss'])

plt.show()
