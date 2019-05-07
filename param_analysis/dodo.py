import os


def task_copy_rename():
    def copy_rename(dir):
        os.system("python copy_rename.py --inp_dir {}".format(dir))
        pass

    return {
            'actions':[(copy_rename,)],
            'params':[{'name':'dir',
                       'short':'d',
                       'default':'ramp_current'},],
            }


def task_csv_to_dataframe():
    return {
        'actions': [['python', 'csv_to_dataframe.py']],
        'verbosity':2 ,
        }


# def task_param_similarity():
#     return {
#         'actions': [['python', 'param_similarity.py']],
#         'verbosity':2,
#     }
