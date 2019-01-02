# -n --name
# -ns --n_samples
# -nr --n_rounds
# -nh --hiddens

# Run and analyse dap
echo -e '\n1. start'
python infer_dap_save_all.py -n _1x4_1x1k -ns 1000 -nr 1 -nh 4 4

echo -e '\n2. start'
python infer_dap_save_all.py -n _1x4_1x2k -ns 2000 -nr 1 -nh 4 4

echo -e '\n3. start'
python infer_dap_save_all.py -n _1x4_1x4k -ns 4000 -nr 1 -nh 4 4

echo -e '\n4. start'
python infer_dap_save_all.py -n _1x4_1x8k -ns 8000 -nr 1 -nh 4 4

echo -e '\n5. start'
python infer_dap_save_all.py -n _2x4_1x1k -ns 1000 -nr 2 -nh 4 4

echo -e '\n6. start'
python infer_dap_save_all.py -n _2x4_1x2k -ns 2000 -nr 2 -nh 4 4

echo -e '\n7. start'
python infer_dap_save_all.py -n _2x4_1x4k -ns 4000 -nr 2 -nh 4 4

echo -e '\n8. start'
python infer_dap_save_all.py -n _2x4_1x8k -ns 8000 -nr 2 -nh 4 4

echo -e '\n9. start'
python infer_dap_save_all.py -n _3x4_1x1k -ns 1000 -nr 3 -nh 4 4

echo -e '\n10. start'
python infer_dap_save_all.py -n _3x4_1x2k -ns 2000 -nr 3 -nh 4 4

echo -e '\n11. start'
python infer_dap_save_all.py -n _3x4_1x4k -ns 4000 -nr 3 -nh 4 4

echo -e '\n12. start'
python infer_dap_save_all.py -n _3x4_1x8k -ns 8000 -nr 3 -nh 4 4
