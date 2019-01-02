# -n --name
# -ns --n_samples
# -nr --n_rounds
# -nh --hiddens

# Run and analyse dap
echo -e '\n1. start'
python infer_dap_save_all.py -n _2x4_1x9k -ns 9000 -nr 1 -nh 4 4

echo -e '\n2. start'
python infer_dap_save_all.py -n _2x4_1x10k -ns 10000 -nr 1 -nh 4 4

echo -e '\n3. start'
python infer_dap_save_all.py -n _2x4_2x9k -ns 9000 -nr 2 -nh 4 4

echo -e '\n4. start'
python infer_dap_save_all.py -n _2x4_2x10k -ns 10000 -nr 2 -nh 4 4
