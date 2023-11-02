"""
Set up Sacred and logging for running experiments. Define a default config.
"""
import logging
import mimetypes
import pickle

# needed for the source files to be included in the experiment database
from pose import (
    experiments,
    freq_space,
    hex,
    input,
    io_utils,
    nengo_utils,
    plotting,
    typing
)

from pose.experiments import run_experiment

from pose.io_utils import (
    get_mongo_uri,
    datetime_to_str,
    get_debug_path
)


import sacred


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
mimetypes.add_type('application/x-binary', '.pkl')


ex = sacred.Experiment('main')

ex.captured_out_filter = sacred.utils.apply_backspaces_and_linefeeds

ex.observers.append(sacred.observers.MongoObserver(
    url=get_mongo_uri(), db_name='sacred'))


default_config = {
    'seed': 0,
    'nengo_seed': 0,

    # run
    'dt': 0.001,
    'fgrid_shape': (12, 12, 12),
    'grid_shape': (12, 12, 12),
    'variance_pose': 0.0025,
    'sample_every': 0.1,
    'simulation_duration': 0.0,
    'tau': 0.1,

    # impl
    'base_exp_id': 0,  # 1154,
    'weights': {
        'var_exc': 0.0108485147,
        'var_inh': 0.01084861,
        'fact_exc': 1.00115141,
        'fact_inh': 1.001155,
        'offset': 0.0,
        'tran_shift': 0.25*1/12,
        'rot_shift': 0.25*1/12
    },
    'weight_sparse_threshold': 2.3e-5,
    'input': [],
    'use_loihi': False,
    'bias': 0.968,
    'enable_noise': False,
    'noise_std': 0.0,
    'continuous_inhib': True,
    'full_init_con': True,

    # eval
    'comment': '',
    'output_filename': 'sim_data',
    'enable_status_mails': False,
    'textid': ''
}
"""Supported config parameters for simulation, with sensible defaults."""

ex.add_config(default_config)


@ex.main
def run(_config, _run) -> None:
    """Gets called when running an experiment with Sacred.
    Delegates to `pose.experiments.run_experiment` and handles output data generated during simulation.
    """
    start_time_str = datetime_to_str(_run.start_time)

    exp_dir = get_debug_path() / 'exp' / start_time_str
    exp_dir.mkdir()

    data = run_experiment(_config)

    # save recorded simulation data to file
    if _config['output_filename'] is not None:
        data_file = exp_dir / (_config['output_filename'] + '.pkl')
        with data_file.open('wb') as f:
            pickle.dump(data, f, pickle.HIGHEST_PROTOCOL)

    # add any files generated during or after simulation as Sacred artifacts
    for artif in exp_dir.iterdir():
        print(artif)
        ex.add_artifact(artif, content_type=mimetypes.guess_type(artif)[0])

    if _config['enable_status_mails']:
        io_utils.send_mail('[IDP] Experiment ' + str(_run._id) + ' done', 'Simulation run finished.')
