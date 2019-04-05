
tmux new -s 101 -d
tmux send-keys -t 101 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_3_param_1x15n_1x1k -ns 1000 -nr 1 -nh 15 -np 3 ' C-m

tmux new -s 102 -d
tmux send-keys -t 102 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_3_param_1x15n_1x2 -ns 2000 -nr 1 -nh 15 -np 3' C-m

tmux new -s 103 -d
tmux send-keys -t 103 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_3_param_1x15n_1x3 -ns 3000 -nr 1 -nh 15 -np 3' C-m

tmux new -s 104 -d
tmux send-keys -t 104 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_3_param_1x15n_1x4 -ns 4000 -nr 1 -nh 15 -np 3' C-m

tmux new -s 105 -d
tmux send-keys -t 105 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_3_param_1x15n_1x5 -ns 5000 -nr 1 -nh 15 -np 3' C-m

tmux new -s 106 -d
tmux send-keys -t 106 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_3_param_1x15n_1x6 -ns 6000 -nr 1 -nh 15 -np 3' C-m


tmux new -s 107 -d
tmux send-keys -t 107 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_3_param_1x15n_1x7 -ns 7000 -nr 1 -nh 15 -np 3' C-m

tmux new -s 108 -d
tmux send-keys -t 108 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_3_param_1x15n_1x8 -ns 8000 -nr 1 -nh 15 -np 3' C-m


tmux new -s 109 -d
tmux send-keys -t 109 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_3_param_1x15n_1x9 -ns 9000 -nr 1 -nh 15 -np 3' C-m

tmux new -s 110 -d
tmux send-keys -t 110 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_step_current.py -n _step_3_param_1x15n_1x10 -ns 10000 -nr 1 -nh 15 -np 3' C-m
