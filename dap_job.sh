n_samples=$1
n_rounds=$2
n_comp=$3

# Run and analyse dap
# ss1
echo -e '\n1. lfi_dap ss1'
python lfi_dap.py --name _ss1 --n_samples $n_samples 

echo -e '\n2. analyse_snpe'
python analyse_snpe_dap.py --name _ss1

echo -e '\n3. analyse_distr_snpe'
python analyse_distr_snpe_dap.py --name _ss1 --ii_samples 1000
