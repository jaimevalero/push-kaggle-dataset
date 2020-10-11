import sys
import yaml
import os
import json
import tempfile
import subprocess
import shutil
from loguru import logger
import tempfile
import subprocess
from jinja2 import Environment, PackageLoader, select_autoescape
import glob
from shutil import copyfile

def execute(bashCommand):
    logger.debug(f"bashCommand={bashCommand}")

    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    logger.debug(f"output={output}")
    logger.debug(f"error={error}")

    return output

def copy_files():
    dataset_file_in_yaml = [ x for x in os.environ.get('INPUT_FILES ').split("\n")]
    logger.info(f"FILES={FILES}")
    FILE_PATH= os.environ.get('GITHUB_WORKSPACE')

    for dataset_file in dataset_file_in_yaml :
        # We have to explode * expressions
        expanded_dataset_files = glob.glob(f"{FILE_PATH}/{dataset_file}")
        for expanded_dataset_file in expanded_dataset_files  :
            # If file already is there, we do not copy it
            if os.path.exists(expanded_dataset_file.split("/")[-1]) :
                continue
            else :
                shutil.copy(expanded_dataset_file,".")
                logger.info(f"file {expanded_dataset_file}")

    print(glob.glob('*'))

def prepare_job():
    """ Prepare temp dir"""
    dirpath = tempfile.mkdtemp()
    os.chdir(dirpath)

    #kaggle datasets status jaimevalero/covid19-madrid

    INPUT_ID = os.environ.get('INPUT_ID')
    result = execute(f" kaggle datasets status {INPUT_ID}")
    logger.debug(f"result: {result}")

    has_to_create_new_dataset = not "ready" in str(result)

    if has_to_create_new_dataset:
        env = Environment(
            loader=PackageLoader('templates'),
            autoescape=select_autoescape(['html', 'xml'])
        )
        template = env.get_template('templates/dataset-metadata.j2')

        INPUT_ID = os.environ.get('INPUT_ID')
        REPO_NAME= os.environ.get('GITHUB_REPOSITORY').split("/")[-1]
        TITLE = os.environ.get('INPUT_TITLE',REPO_NAME)
        logger.debug(f"INPUT_ID={INPUT_ID}, INPUT_TITLE={INPUT_TITLE}")

        outputText = template.render(INPUT_ID=INPUT_ID, INPUT_TITLE=INPUT_TITLE)
        with open("dataset-metadata.json", "w") as fh:
            fh.write(outputText)
        with open("dataset-metadata.json", 'r') as fin:
            logger.debug(fin.read())
    copy_files()

    return
# Resolve if dataset has to be created

# Prepare temp dirname

# Prepare filenames

# PRepare

# prepare meta json if no
def print_files():
    """
        Helper function to know where are my files
    """

    for dirname, _, filenames in os.walk('/'):
        for filename in filenames:
            print(os.path.join(dirname, filename))
    return

def print_environment():
    """
        Helper function to know where are my variables
    """
    variables_functions = [dir(), globals() , locals()]
    for func in variables_functions:
        logger.debug( func)
    # Print environment varriables
    for key in os.environ.keys():
        valor=os.environ[key]
        logger.debug(f"llave {key} : {valor}")
    return

def main():
    logger.info("Start")
    #
    print_files()
    print_environment()

    prepare_job()

    logger.info("info")
    return

if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logger.error( "Error "+ str(e))
