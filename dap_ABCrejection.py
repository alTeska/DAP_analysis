import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore

from delfi.distribution import Uniform
from dap.utils import obs_params_gbar, syn_current
from dap.dap_sumstats_moments import DAPSummaryStatsMoments
from dap import DAPcython
from dap.dap_simulator import DAPSimulator

# General Settings Pick
n_samples = 100
n_summary = 13
dt = 0.01

# Get current
I, t, t_on, t_off = syn_current(duration=70, dt=dt, t_on=15, t_off=20, amp=3.1)
params, labels = obs_params_gbar(reduced_model=True)
dap = DAPcython(-75, params*10)

# Set up the model
sim = DAPSimulator(I, dt, -75, dim_param=2)
stats = DAPSummaryStatsMoments(t_on, t_off, n_summary=n_summary)

# Setup Priors
prior_min = np.array([0, 0])
prior_max = np.array([2, 2])
prior_unif = Uniform(lower=prior_min, upper=prior_max)

# generate desired data
U = dap.simulate(dt, t, I)
y_o = {'data': U.reshape(-1),
       'time': t,
       'dt': dt,
       'I': I}
y = stats.calc([y_o])

# sample one parameter, simulate and get the summary statistics
params = prior_unif.gen(n_samples=1)
x_o = sim.gen_single(params[0])

y_obs = stats.calc([x_o])

sum_stats = zscore(y, axis=1)
obs_zt = zscore(y_obs, axis=1)
print('sum_stats', sum_stats[0])
print('obs_zt', obs_zt[0])
#
# # distance of the z-scored summary statistics 'sum_stats' to the z-scored observed data 'obs_zt'
dist_sum_stats = np.linalg.norm((sum_stats-obs_zt),axis=1)
dist_argsort = np.argsort(dist_sum_stats)

print(dist_sum_stats)
