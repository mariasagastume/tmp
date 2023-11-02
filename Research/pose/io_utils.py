"""
File I/O and communication with database for running, logging, and evaluating experiments.

Note:
    Not part of the public API.
"""
# __all__ = []  # optionally uncomment for generating docs
from csv import writer, DictWriter
import logging
from mailjet_rest import Client
import os
import pathlib
import psutil
import subprocess


logger = logging.getLogger(__name__)


def get_mem_info():
    process = psutil.Process(os.getpid())
    mem = process.memory_info().vms // 1024 // 1024
    return f'[VMS={mem}MiB]'


def get_pose_lib_path():
    return pathlib.Path(__file__).parent


def get_debug_path():
    return pathlib.Path(__file__).parent.parent.parent / 'pose_debug'


def datetime_to_str(ts):
    return ts.strftime('%Y%m%d-%H%M%S-%f')


def get_mongo_uri(db='default') -> str:
    if db == 'default':
        return 'mongodb://mongo_user:mongo_password@127.0.0.1:27017/?authSource=admin'
    elif db == 'lab1':
        return 'mongodb://mongo_user:mongo_password@127.0.0.1:27018/?authSource=admin'
    else:
        raise ValueError("db '" + db + "' is not available")


def get_git_revision_hash():
    # from https://stackoverflow.com/a/66292983/2868795
    full_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    full_hash = str(full_hash, "utf-8").strip()
    return full_hash


def get_git_revision_short_hash():
    # from https://stackoverflow.com/a/66292983/2868795
    short_hash = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
    short_hash = str(short_hash, "utf-8").strip()
    return short_hash


# https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/
def append_list_as_row(file_name, list_of_elem):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        csv_writer = writer(write_obj)
        # Add contents of list as last row in the csv file
        csv_writer.writerow(list_of_elem)


# https://thispointer.com/python-how-to-append-a-new-row-to-an-existing-csv-file/
def append_dict_as_row(file_name, dict_of_elem, field_names):
    # Open file in append mode
    with open(file_name, 'a+', newline='') as write_obj:
        # Create a writer object from csv module
        dict_writer = DictWriter(write_obj, fieldnames=field_names, extrasaction='ignore')
        # Add dictionary as wor in the csv
        dict_writer.writerow(dict_of_elem)


# field_names = ['id']
# field_names += ['global_seed', 'resolution_u', 'resolution_v', 'resolution_w', 'num_coef_u', 'num_coef_v', 'num_coef_w', 'sd_pose_numerator', 'sd_pose_denominator', 'n_eval_points', 'dt', 'simulation_duration', 'nengo_seed', 'tau', 'sigma']
# append_list_as_row('experiment_log.csv', field_names)

def log_experiment(timestamp, exp_dict, csv_header):
    row_dict = exp_dict
    row_dict['id'] = timestamp

    append_dict_as_row('experiment_log.csv', row_dict, csv_header)


def send_mail(subject='', text=''):
    api_key = (get_pose_lib_path().parent.parent / 'mailjet_apikey.txt').read_text().replace("\n", "")
    api_secret = (get_pose_lib_path().parent.parent / 'mailjet_secretkey.txt').read_text().replace("\n", "")
    mail_address = (get_pose_lib_path().parent.parent / 'debug_status_mail_address.txt').read_text().replace("\n", "")
    name = (get_pose_lib_path().parent.parent / 'debug_status_mail_name.txt').read_text().replace("\n", "")
    mailjet = Client(auth=(api_key, api_secret), version='v3.1')
    data = {
        'Messages': [
            {
            "From": {
                "Email": mail_address,
                "Name": name
            },
            "To": [
                {
                "Email": mail_address,
                "Name": name
                }
            ],
            "Subject": subject,
            "TextPart": text,
            "HTMLPart": text
            }
        ]
    }
    result = mailjet.send.create(data=data)
    # print(result.status_code)
    # print(result.json())
