import numpy as np
import matplotlib.pyplot as plt
from delfi.utils.viz import plot_pdf

#################################
# distance of the z-scored summary statistics 'sum_stats' to the z-scored observed data 'obs_zt'
dist_sum_stats = np.linalg.norm((sum_stats-obs_zt),axis=1)

# sorting the distances
dist_argsort = np.argsort(dist_sum_stats)

# rejection criterion
percent_accept = 1
percent_criterion = int(len(dist_sum_stats)*percent_accept/100)

# rejection (or more positively, acceptance) of the z-scored parameters 'params' and inverse z-scoring of the accepted parameters
params_accept = params[dist_argsort[0:percent_criterion],:]*params_std + params_mean

# inspect number and distance of accepted samples
np.shape(params_accept)
plt.hist(dist_sum_stats[dist_argsort[0:percent_criterion]])

# plotting SNPE posterior 'posterior_snpe' and rejection ABC posterior 'params_accept'
plot_pdf(posterior_snpe, samples=params_accept.T)
#################################
