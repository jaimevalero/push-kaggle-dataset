import sys
import yaml
import os
import json
import tempfile
import subprocess
import shutil
from distutils.util import strtobool
from loguru import logger



def prepare_job():
    """ Prepare temp dir"""
    return
# Resolve if dataset has to be created

# Prepare temp dirname

# Prepare filenames

# PRepare

# prepare meta json if no

def main():
    logger.info("Start")
    for key in os.environ.keys():
        llave=os.environ[key][0]
        valor=os.environ[key][1]
        logger.debug(f"llave {llave} : {valor}")
        print(os.environ.get('HOME', '/home/username/'))

    prepare_job()
    logger.info("info")
    return

if __name__ == '__main__':
    main()

    print("|||||||||||||" , dir())
    print("|||||||||||||" ,globals())
    print("|||||||||||||",locals())
    for dirname, _, filenames in os.walk('/'):
        for filename in filenames:
            print(os.path.join(dirname, filename))
