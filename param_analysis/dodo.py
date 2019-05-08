import os


directory = 'step_current'


def task_copy_rename():
    def copy_rename(dir):
        os.system("python copy_rename.py --inp_dir {}".format(dir))
        pass
    return {
        'actions': [(copy_rename, [], {
            # 'dir': 'step_current'})
            'dir': directory})
        ],
        'verbosity': 2,
    }


def task_csv_to_dataframe():
    return {
        'actions': [['python', 'csv_to_dataframe.py']],
        'verbosity':2 ,
        }


def task_calc_features():
    return {
        'actions': [['python', 'calc_features.py']],
        'verbosity':2,
    }
