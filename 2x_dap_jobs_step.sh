
tmux new -s 121 -d
tmux send-keys -t 121 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_4_param_1x20n_1x21k -ns 21000 -nr 1 -nh 20 -np 4' C-m

tmux new -s 122 -d
tmux send-keys -t 122 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_4_param_1x20n_1x22 -ns 22000 -nr 1 -nh 20 -np 4' C-m

tmux new -s 123 -d
tmux send-keys -t 123 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_4_param_1x20n_1x23 -ns 23000 -nr 1 -nh 20 -np 4' C-m

tmux new -s 124 -d
tmux send-keys -t 124 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_4_param_1x20n_1x24 -ns 24000 -nr 1 -nh 20 -np 4' C-m

tmux new -s 125 -d
tmux send-keys -t 125 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_4_param_1x20n_1x25 -ns 15000 -nr 1 -nh 20 -np 4' C-m

tmux new -s 126 -d
tmux send-keys -t 126 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_4_param_1x20n_1x26 -ns 26000 -nr 1 -nh 20 -np 4' C-m


tmux new -s 127 -d
tmux send-keys -t 127 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_4_param_1x20n_1x27 -ns 27000 -nr 1 -nh 20 -np 4' C-m

tmux new -s 128 -d
tmux send-keys -t 128 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_4_param_1x20n_1x28 -ns 28000 -nr 1 -nh 20 -np 4' C-m


tmux new -s 129 -d
tmux send-keys -t 129 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_4_param_1x20n_1x29 -ns 29000 -nr 1 -nh 20 -np 4' C-m
