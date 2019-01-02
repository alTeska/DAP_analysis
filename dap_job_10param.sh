# -n --name
# -ns --n_samples
# -nr --n_rounds
# -nh --hiddens

# Run and analyse dap
echo -e '\n1. start'
python infer_dap_save_all_10param.py -n _10param_2x4_1x100 -ns 100 -nr 1 -nh 4 4
