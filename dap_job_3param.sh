# -n --name
# -ns --n_samples
# -nr --n_rounds
# -nh --hiddens

# Run and analyse dap
echo -e '\n1. start'
python infer_real_data_3param.py -n _3param_1x20n_1x1k -ns 100 -nr 1 -nh 20
python infer_real_data_3param.py -n _3param_1x20n_1x2k -ns 2000 -nr 1 -nh 20
python infer_real_data_3param.py -n _3param_1x20n_1x5k -ns 5000 -nr 1 -nh 20
python infer_real_data_3param.py -n _3param_1x20n_1x8k -ns 8000 -nr 1 -nh 20
python infer_real_data_3param.py -n _3param_1x20n_1x10k -ns 10000 -nr 1 -nh 20

echo -e '\n1. start'
python infer_real_data_3param.py -n _3param_2x20n_1x1k -ns 1000 -nr 1 -nh 20 20
python infer_real_data_3param.py -n _3param_2x20n_1x2k -ns 2000 -nr 1 -nh 20 20
python infer_real_data_3param.py -n _3param_2x20n_1x5k -ns 5000 -nr 1 -nh 20 20
python infer_real_data_3param.py -n _3param_2x20n_1x8k -ns 8000 -nr 1 -nh 20 20
python infer_real_data_3param.py -n _3param_2x20n_1x10k -ns 10000 -nr 1 -nh 20 20
