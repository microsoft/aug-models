from imodelsx import submit_utils
from os.path import dirname, join
import os.path
repo_dir = dirname(dirname(dirname(os.path.abspath(__file__))))

# Showcasing different ways to sweep over arguments
# Can pass any empty dict for any of these to avoid sweeping

# List of values to sweep over (sweeps over all combinations of these)
params_shared_dict = {
    'dataset': ['financial_phrasebank', 'sst2', 'emotion', 'rotten_tomatoes'],
}

# List of tuples to sweep over (these values are coupled, and swept over together)
# Note: this is a dictionary so you shouldn't have repeated keys
params_coupled_dict = {}

# Args list is a list of dictionaries
# If you want to do something special to remove some of these runs, can remove them before calling run_args_list
args_list = submit_utils.get_args_list(
    params_shared_dict=params_shared_dict,
    params_coupled_dict=params_coupled_dict,
)
submit_utils.run_args_list(
    args_list,
    script_name=join(repo_dir, 'experiments', '08_fit_instructor_models.py'),
    actually_run=True,
    n_cpus=4,
)