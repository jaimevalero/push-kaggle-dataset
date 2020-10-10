import sys
import yaml
import os
import json
import tempfile
import subprocess
import shutil
from distutils.util import strtobool


# Prepare temp dir

# Resolve if dataset has to be created

# Prepare temp dirname

# Prepare filenames

# PRepare

# prepare meta json if no

def main():
    prepare_job()
    return
#${{ github.event.head_commit.message }}

if __name__ == '__main__':
    for key in os.environ.keys():  print(f"llave: {key}")
    print("|||||||||||||" , dir())
    print("|||||||||||||" ,globals())
    print("|||||||||||||",locals())
    for dirname, _, filenames in os.walk('/'):
        for filename in filenames:
            print(os.path.join(dirname, filename))
