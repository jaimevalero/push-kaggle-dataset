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
from jinja2 import Template
from distutils.util import strtobool

import glob
from shutil import copyfile
import sys

commit_message=""

def execute(bashCommand):
    """ Execute a line of command """
    logger.debug(f"bashCommand={bashCommand}")
    #
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    logger.debug(f"output={output}")
    logger.debug(f"error={error}")
    #
    return output

def upload_files():
    # Get message
    # Get public/private
    # kaggle datasets version -m "Daily update  $DATE"
    stdout=execute(f"""  kaggle datasets version -m "{commit_message}" """).decode("utf-8").replace("\n","")
    logger.info(f"upload results={stdout}")

    INPUT_ID = os.environ.get('INPUT_ID')
    stdout=execute(f"""  kaggle datasets files {INPUT_ID} """).decode("utf-8").replace("\n","")
    logger.info(f"upload results={stdout}")
    return

def copy_files():
    """
        Parse user yaml and copy files to temp directory
    """
    current_work_directory = os.getcwd()
    dataset_file_in_yaml = [ x for x in os.environ.get('INPUT_FILES').split("\n")]
    logger.info(f"dataset_file_in_yaml={dataset_file_in_yaml}")
    FILE_PATH= os.environ.get('GITHUB_WORKSPACE')

    for dataset_file in dataset_file_in_yaml :
        logger.debug(f"dataset_file={dataset_file}")
        # Avoid empty strings
        if not dataset_file.replace(" ","") :   continue
        # We have to explode * expressions
        expanded_dataset_files = glob.glob(f"{FILE_PATH}/{dataset_file}")
        for expanded_dataset_file in expanded_dataset_files  :
            # If file already is there, we do not copy it
            file_not_exists_on_dst = not os.path.exists(expanded_dataset_file.split("/")[-1])
            if file_not_exists_on_dst :
                src = expanded_dataset_file
                dst = current_work_directory + "/" + os.path.basename(expanded_dataset_file)
                logger.info(f"copy {src} to {dst}")
                shutil.copy(src,dst)

    logger.success("Contents to be uploaded: " , glob.glob(current_work_directory + "/" +'*'))
    return

def prepare_job():
    """
        Prepare temp dir, create metadata if datasets is new , or download metadata from kaggle if datasets already exists.
    """

    commit_message=execute(" git log --oneline --format=%B -n 1 HEAD ").decode("utf-8").replace("\n","")
    logger.debug(f"commit_message={commit_message}")
    dirpath = tempfile.mkdtemp()
    os.chdir(dirpath)

    # Parse variables
    INPUT_ID = os.environ.get('INPUT_ID')
    INPUT_TITLE = os.environ.get('INPUT_TITLE',INPUT_ID.split("/")[1])
    INPUT_IS_PUBLIC =bool( strtobool(str( os.environ.get('INPUT_IS_PUBLIC',False))))
    logger.debug(f"INPUT_ID={INPUT_ID}, INPUT_TITLE={INPUT_TITLE}")
    vars = " --public " if INPUT_IS_PUBLIC else " "

    # Check dataset exists
    result = execute(f" kaggle datasets status {INPUT_ID}")
    logger.debug(f"result for {INPUT_ID} is result={result}")
    has_to_create_new_dataset = not "ready" in str(result)
    logger.debug(f"has_to_create_new_dataset={has_to_create_new_dataset}")

    if has_to_create_new_dataset:
        # Render template
        with open("/app/templates/dataset-metadata.j2") as file_:
            template = Template(file_.read())
        outputText = template.render(INPUT_ID=INPUT_ID, INPUT_TITLE=INPUT_TITLE)
        with open("dataset-metadata.json", "w") as fh:
            fh.write(outputText)
        with open("dataset-metadata.json", 'r') as fin:
            logger.debug(fin.read())

        command=f"kaggle datasets create  {vars}"
        result = execute(f"{command}")
        logger.info(f"result for {command} is result={result}")
    else:
        command=f"kaggle datasets metadata {INPUT_ID}"
        result = execute(f"{command}")
        logger.debug(f"result for {command} is result={result}")

    return
# Resolve if dataset has to be created

# Prepare temp dirname

# Prepare filenames

# PRepare

# prepare meta json if no
def print_files():
    """
        Helper function to know where are my files.
        Just for debug
    """

    for dirname, _, filenames in os.walk('/'):
        for filename in filenames:
            print(os.path.join(dirname, filename))
    return

def print_environment():
    """
        Helper function to know where are my variables.
        Just for debug
    """
    variables_functions = [dir(), globals() , locals()]
    for func in variables_functions:
        logger.debug( func)
    # Print environment varriables
    for key in os.environ.keys():
        valor=os.environ[key]
        logger.debug(f"llave {key} : {valor}")
    return

@logger.catch(onerror=lambda _: sys.exit(1))
def main():
    logger.info("Start")
    #print_files()
    print_environment()

    prepare_job()
    copy_files()
    upload_files()

    logger.info("info")
    return

if __name__ == '__main__':
    main()
