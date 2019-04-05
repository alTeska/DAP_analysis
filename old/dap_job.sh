# -n --name
# -ns --n_samples
# -nr --n_rounds
# -nh --hiddens

# Run and analyse dap
echo -e '\n1. start'
python infer_dap_save_all.py -n _2x4_1x1k -ns 1000 -nr 1 -nh 4 4
