# -n --name
# -ns --n_samples
# -nr --n_rounds
# -nh --hiddens

# Run and analyse dap
echo -e '\n1. start'

python infer_real_data_3param.py -n _3param_1x20n_1x1k -ns 100 -nr 1 -nh 20
