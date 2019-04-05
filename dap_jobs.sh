
tmux new -s 01 -d
tmux send-keys -t 01 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x20n_1x11k -ns 11000 -nr 1 -nh 20' C-m

tmux new -s 02 -d
tmux send-keys -t 02 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x20n_1x12 -ns 12000 -nr 1 -nh 20' C-m

tmux new -s 03 -d
tmux send-keys -t 03 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x20n_1x13 -ns 13000 -nr 1 -nh 20' C-m

tmux new -s 04 -d
tmux send-keys -t 04 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x20n_1x14 -ns 14000 -nr 1 -nh 20' C-m

tmux new -s 05 -d
tmux send-keys -t 05 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x20n_1x15 -ns 15000 -nr 1 -nh 20' C-m

tmux new -s 06 -d
tmux send-keys -t 06 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x20n_1x16 -ns 16000 -nr 1 -nh 20' C-m


tmux new -s 07 -d
tmux send-keys -t 07 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x20n_1x17 -ns 17000 -nr 1 -nh 20' C-m

tmux new -s 08 -d
tmux send-keys -t 08 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x20n_1x18 -ns 18000 -nr 1 -nh 20' C-m


tmux new -s 09 -d
tmux send-keys -t 09 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap
cd LFI_DAP/DAP_analysis
python args_model_infer_real_data.py -n _1x20n_1x19 -ns 19000 -nr 1 -nh 20' C-m
