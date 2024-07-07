from os import path, makedirs
from inspect import getfile, currentframe
from logging import basicConfig, getLogger, DEBUG
import boto3
from botocore.exceptions import ClientError

def get_main_directory():
    return path.dirname(path.abspath(getfile(currentframe())))

def start_log(class_name, maindirectory):
    directory = path.join(maindirectory, 'log')  # Modificado para usar path.join
    if not path.exists(directory):
        makedirs(directory)

    log_file = path.join(directory, f"Event{class_name}.log")  # Modificado para usar path.join

    basicConfig(filename=log_file, format='%(asctime)s %(message)s', filemode='w')
    EventWriter = getLogger()
    EventWriter.setLevel(DEBUG)
    return EventWriter
