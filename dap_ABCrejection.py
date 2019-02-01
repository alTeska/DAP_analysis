import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import zscore
from tqdm import tqdm

from delfi.distribution import Uniform
from dap.utils import obs_params_gbar, syn_current
from dap.dap_sumstats_moments import DAPSummaryStatsMoments
from dap import DAPcython
from dap.dap_simulator import DAPSimulator


# General Settings Pick
n_samples = 100
n_summary = 13
dt = 0.01
percent_accept = 1


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


# Sample Parameters
params = prior_unif.gen(n_samples=n_samples)

# calculate the distance for each parameters
norms = []

for p in tqdm(params):
    x_o = sim.gen_single(p)
    y_obs = stats.calc([x_o])
    obs_zt = zscore(y_obs, axis=1)
    dist_sum_stats = np.linalg.norm((sum_stats-obs_zt),axis=1)

    norms.append(dist_sum_stats)

# get the scores
scores = N.transpose()[0]
arg_sorted = np.argsort(scores)

# rejection criterion
percent_criterion = int(len(arg_sorted)*percent_accept/100)
params_accept = params[dist_argsort[0:percent_criterion],:]*params

# plot results
fig, ax = plt.subplots(1,2,figsize=(10,5))
ax[0].hist(x=P[:,0], bins='auto', alpha=0.7, rwidth=0.85);
ax[1].hist(x=P[:,1], bins='auto', alpha=0.7, rwidth=0.85);
ax[0].set_title(labels[0])
ax[1].set_title(labels[1]);


plt.show()
