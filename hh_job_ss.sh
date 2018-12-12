n_samples=$1
n_rounds=$2
n_comp=$3

# Run and analyse HH SNPE
# ss1
echo -e '\n1. hh_snpe ss1'
python hh_SNPE.py -s 1 --name _ss1 --n_samples $n_samples --n_rounds $n_rounds --n_components $n_comp

echo -e '\n2. analyse_snpe'
python analyse_snpe_hh.py --name _ss1

echo -e '\n3. analyse_distr_snpe'
python analyse_distr_snpe_hh.py --name _ss1 --ii_samples 1000

# ss2
echo -e '\n1. hh_snpe ss2'
python hh_SNPE.py -s 2 --name _ss2 --n_samples $n_samples --n_rounds $n_rounds --n_components $n_comp

echo -e '\n2. analyse_snpe'
python analyse_snpe_hh.py --name _ss2

echo -e '\n3. analyse_distr_snpe'
python analyse_distr_snpe_hh.py --name _ss2 --ii_samples 1000


# ss3
echo -e '\n1. hh_snpe ss3'
python hh_SNPE.py -s 3 --name _ss3s --n_samples $n_samples --n_rounds $n_rounds --n_components $n_comp

echo -e '\n2. analyse_snpe'
python analyse_snpe_hh.py --name _ss3s

echo -e '\n3. analyse_distr_snpe'
python analyse_distr_snpe_hh.py --name _ss3s --ii_samples 1000
