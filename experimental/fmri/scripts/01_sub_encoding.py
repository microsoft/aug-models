import itertools
import os
from os.path import dirname
import sys
import submit_utils
repo_dir = dirname(dirname(os.path.abspath(__file__)))
# python /home/chansingh/emb-gam/experimental/fmri/01_fit_encoding.py --feature bert-10 --ndelays 2 --seed 1 --subject UTS03

PARAMS_COUPLED_DICT = {}
# { 
#     ('checkpoint', 'batch_size'): [
#         ('gpt2-xl', 32),
#         ('EleutherAI/gpt-neo-2.7B', 16),
#     ],
# }

##########################################
# params shared across everything (higher up things are looped over first)
##########################################
PARAMS_SHARED_DICT = {
    # things to vary
    'feature': ['bert-3', 'bert-5', 'bert-10', 'bert-20'],
    'ndelays': [6],

    # things to average over
    'seed': [1],

    # fixed params
    'subject': ['UTS03', 'UTS02', 'UTS01',], #'UTS03', 'UTS01', 'UTS02'],
}

ks_final, param_combos_final = submit_utils.combine_param_dicts(
    PARAMS_SHARED_DICT, PARAMS_COUPLED_DICT)
submit_utils.run_dicts(
    ks_final, param_combos_final,
    script_name='01_fit_encoding.py',
    actually_run=True,
)