import numpy as np
import matplotlib.pyplot as plt

from delfi.distribution import Uniform
from delfi.generator import Default
from delfi.inference import SNPE  # , Basic, CDELFI

from dap.utils import (obs_params, syn_obs_stats, syn_obs_data,
                       load_current, load_prior_ranges)
from dap.dap_sumstats_step_mom import DAPSummaryStatsStepMoments
from dap.dap_simulator import DAPSimulator
from dap import DAPcython


# General Settings Pick
n_rounds = 1
n_summary = 17
n_samples = 5
n_hiddens = [15]
n_components = 1
dt = 0.01
reg_lambda = 0.01
n_params = 2

# Load the current
data_dir = '/home/alteska/Desktop/LFI_DAP/data/rawData/2015_08_26b.dat'    # best cell
I, v, t, t_on, t_off, dt = load_current(data_dir, protocol='IV', ramp_amp=1)

params, labels = obs_params(reduced_model=True)
print(params)
print(labels)

# Set up themodel
dap = DAPcython(-75, params)
U = dap.simulate(dt, t, I)

# generate data format for SNPE / OBSERVABLE
x_o = {'data': U.reshape(-1),
       'time': t,
       'dt': dt,
       'I': I}

# Setup Priors
prior_min, prior_max, labels = load_prior_ranges(n_params)
prior_unif = Uniform(lower=prior_min, upper=prior_max)

# Summary Statistics
S = syn_obs_stats(x_o['I'], params=params, dt=x_o['dt'], t_on=t_on, t_off=t_off,
                  n_summary=n_summary, summary_stats=1, data=x_o)


M = DAPSimulator(x_o['I'], x_o['dt'], -75)
s = DAPSummaryStatsStepMoments(t_on, t_off, n_summary=n_summary)
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


distr_comb, axes = plt.subplots(2, 1, figsize=(16, 14))
axes[0].hist(samples_prior[:, 0], bins='auto', label='prior')
axes[1].hist(samples_prior[:, 1], bins='auto', label='prior')
axes[0].hist(samples_posterior[:, 0], bins='auto', label='posterior')
axes[1].hist(samples_posterior[:, 1], bins='auto', label='posterior')
axes[0].legend()
axes[1].legend()

axes[0].annotate(labels[0]+': '+str(round(posteriors[-1].mean[0], 3)),
                 xy=(1, 0), xycoords='axes fraction', fontsize=12,
                 xytext=(-5, 5), textcoords='offset points',
                 ha='right', va='bottom')
axes[1].annotate(labels[1]+': '+str(round(posteriors[-1].mean[1], 3)),
                 xy=(1, 0), xycoords='axes fraction', fontsize=12,
                 xytext=(-5, 5), textcoords='offset points',
                 ha='right', va='bottom')

plt.figure()
plt.plot(logs[0]['loss'])

plt.show()
