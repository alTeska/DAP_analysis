
tmux new -s 111 -d
tmux send-keys -t 111 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _3_param_1x15n_1x11k -ns 11000 -nr 1 -nh 15 -np 3' C-m

tmux new -s 112 -d
tmux send-keys -t 112 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _3_param_1x15n_1x12 -ns 12000 -nr 1 -nh 15 -np 3' C-m

tmux new -s 113 -d
tmux send-keys -t 113 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _3_param_1x15n_1x13 -ns 13000 -nr 1 -nh 15 -np 3' C-m

tmux new -s 114 -d
tmux send-keys -t 114 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _3_param_1x15n_1x14 -ns 14000 -nr 1 -nh 15 -np 3' C-m

tmux new -s 115 -d
tmux send-keys -t 115 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _3_param_1x15n_1x15 -ns 15000 -nr 1 -nh 15 -np 3' C-m

tmux new -s 116 -d
tmux send-keys -t 116 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _3_param_1x15n_1x16 -ns 16000 -nr 1 -nh 15 -np 3' C-m


tmux new -s 117 -d
tmux send-keys -t 117 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _3_param_1x15n_1x17 -ns 17000 -nr 1 -nh 15 -np 3' C-m

tmux new -s 118 -d
tmux send-keys -t 118 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _3_param_1x15n_1x18 -ns 18000 -nr 1 -nh 15 -np 3' C-m


tmux new -s 119 -d
tmux send-keys -t 119 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _3_param_1x15n_1x19 -ns 19000 -nr 1 -nh 15 -np 3' C-m
