import glob
import numpy as np
import pandas as pd


directory = './parameters/'

# load the data
dir = glob.glob(directory + '*')

# create variables name based on n_samples
dir_name = []
for n in dir:
    x = n.find('dap_')
    n = n[x:-4]
    dir_name.append(n)

# get parameters label
param_labels = pd.read_csv(dir[0])['Unnamed: 0'].values

# load parameters into arrays
for i, d in enumerate(dir):
    vars()[dir_name[i]] = pd.read_csv(d)['mean param'].values

# build a common array
parameter_matrix = np.zeros_like(param_labels)

for n in dir_name:
    x = vars()[n]
    parameter_matrix = np.vstack([parameter_matrix, x])

# create df columns name based on n_samples
col_names = []
for n in dir:
    x = n.find('n_')
    n = n[x+2:-4]
    col_names.append(n)

# create and save dataframe
df_param = pd.DataFrame(data=parameter_matrix[1:].T, columns=col_names)
df_param.set_axis(param_labels, inplace=True)

fname_start = dir[0].find('dap_')
fname_stop = dir[0].find('n_')
fname = dir[0][fname_start:fname_stop]

df_param.to_csv(fname + '.csv')
