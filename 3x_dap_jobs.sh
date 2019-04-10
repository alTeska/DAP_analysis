
tmux new -s 31 -d
tmux send-keys -t 31 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x31 -ns 31000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 32 -d
tmux send-keys -t 32 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x32 -ns 32000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 33 -d
tmux send-keys -t 33 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x33 -ns 33000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 34 -d
tmux send-keys -t 34 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x34 -ns 34000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 35 -d
tmux send-keys -t 35 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x35 -ns 35000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 36 -d
tmux send-keys -t 36 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x36 -ns 36000 -nr 1 -nh 30 -np 5' C-m


tmux new -s 37 -d
tmux send-keys -t 37 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x37 -ns 37000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 38 -d
tmux send-keys -t 38 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x38 -ns 38000 -nr 1 -nh 30 -np 5' C-m


tmux new -s 39 -d
tmux send-keys -t 39 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x39 -ns 39000 -nr 1 -nh 30 -np 5' C-m
