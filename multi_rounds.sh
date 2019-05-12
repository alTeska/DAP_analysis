# tmux new -s 11 -d
# tmux send-keys -t 11 '
# cd
# export PATH="anaconda3/bin:$PATH"
# source activate dap2
# cd LFI_DAP/DAP_analysis
# python args_infer_multi_rounds.py -n _step_11_param_1x132 -ns 1000 -nr 20 -np 11 -nh 132' C-m
#
# tmux new -s 12 -d
# tmux send-keys -t 12 '
# cd
# export PATH="anaconda3/bin:$PATH"
# source activate dap2
# cd LFI_DAP/DAP_analysis
# python args_infer_multi_rounds.py -n _step_11_param_2x132 -ns 1000 -nr 20 -np 11 -nh 132 132' C-m

tmux new -s 13 -d
tmux send-keys -t 13 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap2
cd LFI_DAP/DAP_analysis
python args_infer_multi_rounds.py -n _step_11_param_3x132 -ns 1000 -nr 20 -np 11 -nh 132 132 132' C-m

tmux new -s 14 -d
tmux send-keys -t 14 '
cd
export PATH="anaconda3/bin:$PATH"
source activate dap2
cd LFI_DAP/DAP_analysis
python args_infer_multi_rounds.py -n _step_11_param_4x132 -ns 1000 -nr 20 -np 11 -nh 132 132 132 132' C-m
