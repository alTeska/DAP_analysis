
tmux new -s 131 -d
tmux send-keys -t 131 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_5_param_1x30n_1x31 -ns 31000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 132 -d
tmux send-keys -t 132 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_5_param_1x30n_1x32 -ns 32000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 133 -d
tmux send-keys -t 133 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_5_param_1x30n_1x33 -ns 33000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 134 -d
tmux send-keys -t 134 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_5_param_1x30n_1x34 -ns 34000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 135 -d
tmux send-keys -t 135 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_5_param_1x30n_1x35 -ns 35000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 136 -d
tmux send-keys -t 136 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_5_param_1x30n_1x36 -ns 36000 -nr 1 -nh 30 -np 5' C-m


tmux new -s 137 -d
tmux send-keys -t 137 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_5_param_1x30n_1x37 -ns 37000 -nr 1 -nh 30 -np 5' C-m

tmux new -s 138 -d
tmux send-keys -t 138 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_5_param_1x30n_1x38 -ns 38000 -nr 1 -nh 30 -np 5' C-m


tmux new -s 139 -d
tmux send-keys -t 139 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_5_param_1x30n_1x39 -ns 39000 -nr 1 -nh 30 -np 5' C-m
