# -n --name
# -ns --n_samples
# -nr --n_rounds
# -nh --hiddens

# Run and analyse dap
echo -e '\n1. start'
python infer_dap_save_all.py -n _2x4_1x1k -ns 1000 -nr 1 -nh 4 4
python infer_dap_save_all.py -n _2x4_1x2k -ns 2000 -nr 1 -nh 4 4
python infer_dap_save_all.py -n _2x4_1x3k -ns 3000 -nr 1 -nh 4 4
python infer_dap_save_all.py -n _2x4_1x4k -ns 4000 -nr 1 -nh 4 4
python infer_dap_save_all.py -n _2x4_1x5k -ns 5000 -nr 1 -nh 4 4

echo -e '\n2. start'
python infer_dap_save_all.py -n _2x4_2x1k -ns 1000 -nr 2 -nh 4 4
python infer_dap_save_all.py -n _2x4_2x2k -ns 2000 -nr 2 -nh 4 4
python infer_dap_save_all.py -n _2x4_2x3k -ns 3000 -nr 2 -nh 4 4
python infer_dap_save_all.py -n _2x4_2x4k -ns 4000 -nr 2 -nh 4 4
python infer_dap_save_all.py -n _2x4_2x5k -ns 5000 -nr 2 -nh 4 4

echo -e '\n3. start'
python infer_dap_save_all.py -n _2x4_3x1k -ns 1000 -nr 3 -nh 4 4
python infer_dap_save_all.py -n _2x4_3x2k -ns 2000 -nr 3 -nh 4 4
python infer_dap_save_all.py -n _2x4_3x3k -ns 3000 -nr 3 -nh 4 4
python infer_dap_save_all.py -n _2x4_3x4k -ns 4000 -nr 3 -nh 4 4
python infer_dap_save_all.py -n _2x4_3x5k -ns 5000 -nr 3 -nh 4 4

echo -e '\n4. start'
python infer_dap_save_all.py -n _2x4_4x1k -ns 1000 -nr 4 -nh 4 4
python infer_dap_save_all.py -n _2x4_4x2k -ns 2000 -nr 4 -nh 4 4
python infer_dap_save_all.py -n _2x4_4x3k -ns 3000 -nr 4 -nh 4 4
python infer_dap_save_all.py -n _2x4_4x4k -ns 4000 -nr 4 -nh 4 4
python infer_dap_save_all.py -n _2x4_4x5k -ns 5000 -nr 4 -nh 4 4

 echo -e '\n5. start'
python infer_dap_save_all.py -n _2x4_5x1k -ns 1000 -nr 5 -nh 4 4
python infer_dap_save_all.py -n _2x4_5x2k -ns 2000 -nr 5 -nh 4 4
python infer_dap_save_all.py -n _2x4_5x3k -ns 3000 -nr 5 -nh 4 4
python infer_dap_save_all.py -n _2x4_5x4k -ns 4000 -nr 5 -nh 4 4
python infer_dap_save_all.py -n _2x4_5x5k -ns 5000 -nr 5 -nh 4 4
