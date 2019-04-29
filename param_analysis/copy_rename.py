import argparse, os
import shutil
import glob

# General Settings Pick
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--inp_dir", default='ramp_current', help="name of the folder containing the recorded data")

args = parser.parse_args()

input_dir = './' + args.inp_dir + '/*'
output_dir = 'parameters/'

if not os.path.exists(output_dir):
    # print('creating directory')
    os.mkdir(output_dir)

dir = glob.glob(input_dir)

print('start copying')

for i, d in enumerate(dir):
    n = d.find('dap_')
    # print(output_dir + d[n:] + '.csv')
    shutil.copyfile(d + '/parameters.csv', output_dir + d[n:] + '.csv')
