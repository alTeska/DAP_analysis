
tmux new -s 01 -d
tmux send-keys -t 01 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _3_param_1x20n_1x1k -ns 1000 -nr 1 -nh 20 -np 3 ' C-m

tmux new -s 02 -d
tmux send-keys -t 02 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _3_param_1x20n_1x2 -ns 2000 -nr 1 -nh 20 -np 3' C-m

tmux new -s 03 -d
tmux send-keys -t 03 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _3_param_1x20n_1x3 -ns 3000 -nr 1 -nh 20 -np 3' C-m

tmux new -s 04 -d
tmux send-keys -t 04 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _3_param_1x20n_1x4 -ns 4000 -nr 1 -nh 20 -np 3' C-m

tmux new -s 05 -d
tmux send-keys -t 05 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _3_param_1x20n_1x5 -ns 5000 -nr 1 -nh 20 -np 3' C-m

tmux new -s 06 -d
tmux send-keys -t 06 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _3_param_1x20n_1x6 -ns 6000 -nr 1 -nh 20 -np 3' C-m


tmux new -s 07 -d
tmux send-keys -t 07 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _3_param_1x20n_1x7 -ns 7000 -nr 1 -nh 20 -np 3' C-m

tmux new -s 08 -d
tmux send-keys -t 08 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _3_param_1x20n_1x8 -ns 8000 -nr 1 -nh 20 -np 3' C-m


tmux new -s 09 -d
tmux send-keys -t 09 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _3_param_1x20n_1x9 -ns 9000 -nr 1 -nh 20 -np 3' C-m

tmux new -s 10 -d
tmux send-keys -t 10 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _3_param_1x20n_1x10 -ns 10000 -nr 1 -nh 20 -np 3' C-m
