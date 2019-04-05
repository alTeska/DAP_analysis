
tmux new -s 11 -d
tmux send-keys -t 11 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x15n_1x11k -ns 11000 -nr 1 -nh 15' C-m

tmux new -s 12 -d
tmux send-keys -t 12 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x15n_1x12 -ns 12000 -nr 1 -nh 15' C-m

tmux new -s 13 -d
tmux send-keys -t 13 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x15n_1x13 -ns 13000 -nr 1 -nh 15' C-m

tmux new -s 14 -d
tmux send-keys -t 14 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x15n_1x14 -ns 14000 -nr 1 -nh 15' C-m

tmux new -s 15 -d
tmux send-keys -t 15 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x15n_1x15 -ns 15000 -nr 1 -nh 15' C-m

tmux new -s 16 -d
tmux send-keys -t 16 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x15n_1x16 -ns 16000 -nr 1 -nh 15' C-m


tmux new -s 17 -d
tmux send-keys -t 17 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x15n_1x17 -ns 17000 -nr 1 -nh 15' C-m

tmux new -s 18 -d
tmux send-keys -t 18 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x15n_1x18 -ns 18000 -nr 1 -nh 15' C-m


tmux new -s 19 -d
tmux send-keys -t 19 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x15n_1x19 -ns 19000 -nr 1 -nh 15' C-m
