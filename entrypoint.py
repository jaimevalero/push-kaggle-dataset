import sys
import yaml
import os
import json
import tempfile
import subprocess
import shutil
from distutils.util import strtobool



def main():
    return
#${{ github.event.head_commit.message }}

if __name__ == '__main__':
    print(os.environ.keys())
    print("|||||||||||||" , dir())
    print("|||||||||||||" ,globals())
    print("|||||||||||||",locals())
    for dirname, _, filenames in os.walk('/'):
        for filename in filenames:
            print(os.path.join(dirname, filename))
