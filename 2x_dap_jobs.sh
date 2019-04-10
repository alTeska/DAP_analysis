
tmux new -s 21 -d
tmux send-keys -t 21 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x21 -ns 21000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 22 -d
tmux send-keys -t 22 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x22 -ns 22000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 23 -d
tmux send-keys -t 23 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x23 -ns 23000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 24 -d
tmux send-keys -t 24 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x24 -ns 24000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 25 -d
tmux send-keys -t 25 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x25 -ns 15000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 26 -d
tmux send-keys -t 26 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x26 -ns 26000 -nr 1 -nh 30 -np 5' C-m


tmux new -s 27 -d
tmux send-keys -t 27 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x27 -ns 27000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 28 -d
tmux send-keys -t 28 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x28 -ns 28000 -nr 1 -nh 30 -np 5' C-m


tmux new -s 29 -d
tmux send-keys -t 29 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _5_param_1x30n_1x29 -ns 29000 -nr 1 -nh 30 -np 5' C-m
