tmux new -s 11 -d
tmux send-keys -t 11 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap2
cd LFI_DAP/DAP_analysis
python args_infer_multi_rounds.py -n _5_param_2k_1x30 -ns 2000 -nr 20 -np 5 -nh 30' C-m

tmux new -s 12 -d
tmux send-keys -t 12 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap2
cd LFI_DAP/DAP_analysis
python args_infer_multi_rounds.py -n _5_param_2k_2x30 -ns 2000 -nr 20 -np 5 -nh 30 30' C-m

tmux new -s 13 -d
tmux send-keys -t 13 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap2
cd LFI_DAP/DAP_analysis
python args_infer_multi_rounds.py -n _5_param_2k_3x30 -ns 2000 -nr 20 -np 5 -nh 30 30 30' C-m

tmux new -s 14 -d
tmux send-keys -t 14 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap2
cd LFI_DAP/DAP_analysis
python args_infer_multi_rounds.py -n _5_param_2k_4x30 -ns 2000 -nr 20 -np 5 -nh 30 30 30 30' C-m
