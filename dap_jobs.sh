
tmux new -s 01 -d
tmux send-keys -t 01 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python infer_real_data_4param.py -n _4param_1x30n_1x1k -ns 1000 -nr 1 -nh 30' C-m

tmux new -s 02 -d
tmux send-keys -t 02 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python infer_real_data_4param.py -n _4param_1x30n_1x2k -ns 2000 -nr 1 -nh 30' C-m

tmux new -s 03 -d
tmux send-keys -t 03 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python infer_real_data_4param.py -n _4param_1x30n_1x5k -ns 5000 -nr 1 -nh 30' C-m

tmux new -s 04 -d
tmux send-keys -t 04 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python infer_real_data_4param.py -n _4param_1x30n_1x8k -ns 8000 -nr 1 -nh 30' C-m


tmux new -s 05 -d
tmux send-keys -t 05 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python infer_real_data_4param.py -n _4param_1x30n_1x10k -ns 10000 -nr 1 -nh 30' C-m
