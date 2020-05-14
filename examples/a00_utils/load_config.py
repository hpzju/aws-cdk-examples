import yaml
import os
from contextlib import contextmanager 

# @contextmanager 
# def working_directory(directory):
#     owd = os.getcwd()
#     try: 
#        os.chdir(directory)
#        yield directory
#     finally:
#        os.chdir(owd)

def load_config(file):
    try:
        with open(file, ) as fd:
            config = yaml.load(fd, Loader=yaml.FullLoader)
    except:
        print("Config file loading Error")
    return config