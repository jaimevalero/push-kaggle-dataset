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
import pip
import glob
from shutil import copyfile,  ignore_patterns
import sys

commit_message=""

def execute(bashCommand):
    """ Execute a line of command """
    logger.info(f"bashCommand={bashCommand}")
    process = subprocess.Popen(bashCommand.split(), stdout=subprocess.PIPE)
    output, error = process.communicate()
    logger.info(f"output={output}")
    logger.debug(f"error={error}")
    #
    return output

def get_files_status():
    try :
        INPUT_ID = get_param('INPUT_ID')
        stdout=execute(f"""  kaggle datasets files {INPUT_ID} """).decode("utf-8")
        print(stdout)
    except Exception as e:
        pass

def copy_files():
    """
        Parse user yaml and copy files to temp directory
    """
    GITHUB_WORKSPACE = get_param('GITHUB_WORKSPACE')
    current_work_directory = os.getcwd()
    ignore=ignore_patterns('.git', '.git*')
    dataset_file_in_yaml = [ x for x in get_param('INPUT_FILES').split("\n")]
    logger.info(f"dataset_file_in_yaml={dataset_file_in_yaml}")
    FILE_PATH= get_param('GITHUB_WORKSPACE')

    for dataset_file in dataset_file_in_yaml :
        logger.debug(f"dataset_file={dataset_file}")
        # Avoid empty strings
        if not dataset_file.replace(" ","") :   continue
        if "#"    in dataset_file : continue
        # We have to expand * expressions
        expanded_dataset_files = glob.glob(f"{FILE_PATH}/{dataset_file}")
        for expanded_dataset_file in expanded_dataset_files  :
            if ".git" in expanded_dataset_file : continue
            try :
                src = expanded_dataset_file
                dst = current_work_directory + expanded_dataset_file.replace(GITHUB_WORKSPACE,"").rstrip('/')
                logger.info(f"copy {src} to {dst}")
                is_directory = os.path.isdir(src)
                if is_directory :
                    shutil.copytree(src,dst,ignore=ignore)
                else:
                    os.makedirs(os.path.dirname(dst), exist_ok=True)
                    shutil.copy(src,dst)
            except Exception as e:
            	logger.warning(f"Could not copy {src} to {dst}: {e}")


    logger.success("Contents to be uploaded: " , glob.glob(current_work_directory + "/" +'*'))
    print_files(path=".")
    return

def perform_job():
    """
        Prepare temp dir, create metadata if datasets is new , or download metadata from kaggle if datasets already exists.
    """
    commit_message= get_param('GITHUB_SERVER_URL') + "/"+ get_param('GITHUB_REPOSITORY') +"/commit/"  +get_param('GITHUB_SHA')
    dirpath = tempfile.mkdtemp()
    os.chdir(dirpath)

    # Parse variables
    INPUT_ID          = get_param('INPUT_ID')
    INPUT_TITLE       = get_param('INPUT_TITLE',INPUT_ID.split("/")[1])
    INPUT_SUBTITLE    = get_param('INPUT_SUBTITLE',"")
    if len(INPUT_SUBTITLE) < 21:
	       INPUT_SUBTITLE += ' '*(21-len(INPUT_SUBTITLE))
    INPUT_DESCRIPTION = get_param('INPUT_DESCRIPTION',"")

    INPUT_IS_PUBLIC =bool( strtobool(str(get_param('INPUT_IS_PUBLIC',False))))
    logger.debug(f"INPUT_IS_PUBLIC={INPUT_IS_PUBLIC}")
    vars = " --public " if INPUT_IS_PUBLIC else " "

    # Check dataset exists
    result = execute(f" kaggle datasets status {INPUT_ID}")
    logger.debug(f"result for {INPUT_ID} is result={result}")
    has_to_create_new_dataset = not "ready" in str(result)
    logger.debug(f"has_to_create_new_dataset={has_to_create_new_dataset}")

    copy_files()
    if has_to_create_new_dataset:
        # Render template
        with open("/app/templates/dataset-metadata.j2") as file_:
            template = Template(file_.read())
        outputText = template.render(
            INPUT_ID=INPUT_ID,
            INPUT_TITLE=INPUT_TITLE,
            INPUT_SUBTITLE=INPUT_SUBTITLE,
            INPUT_DESCRIPTION=INPUT_DESCRIPTION
            )

        with open("dataset-metadata.json", "w") as fh:
            fh.write(outputText)
        with open("dataset-metadata.json", 'r') as fin:
            logger.debug(fin.read())
        result = execute(f"kaggle datasets create --dir-mode tar {vars}").decode("utf-8")
        logger.info(f"Dataset creation result: {result}")

        if "Subtitle length" in result :
            logger.critical(f"Error. Dataset not created. {result}")
            raise Exception(f"Error. Dataset not created. {result}")
    else:
        execute(f"""  kaggle datasets metadata {INPUT_ID}""")
        pip.main(['install', '--upgrade', 'kaggle'])
        # pparently whitespaces are not allowed
        commit_message = commit_message.replace(" ","_")
        execute(f"""  kaggle datasets version --dir-mode tar --message "{commit_message}" """)
    return

def print_files(path="/"):
    """
        Helper function to know where are my files.
        Just for debug
    """
    for dirname, _, filenames in os.walk(path):
        for filename in filenames:
            logger.info(os.path.join(dirname, filename))
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
        logger.debug(f"key {key} : {valor}")
    return

def get_param(param_name,default_value=""):
    if param_name == "INPUT_ID":
        if os.environ.get('INPUT_ID')=="{KAGGLE_USERNAME}/{GITHUB_REPO_NAME}" :
            # Default value for dataset is <kaggle username>/<github repo name>
            result = os.environ.get('KAGGLE_USERNAME')+"/"+ os.environ.get('RUNNER_WORKSPACE').split("/")[-1]
        else :
            result = os.environ.get('INPUT_ID')
    elif param_name in [
		"GITHUB_REPOSITORY",
		"GITHUB_SERVER_URL",
		"GITHUB_SHA",
        "GITHUB_WORKSPACE" ,
		"INPUT_DESCRIPTION",
		"INPUT_FILES",
		"INPUT_IS_PUBLIC",
		"INPUT_SUBTITLE",
        "INPUT_TITLE" ] :
        result = os.environ.get(param_name,default_value)
    else :
        raise Exception(f"Value {param_name} not exists")
    logger.debug(f"{param_name}={result}")
    return result

def send_output_param():
    INPUT_ID = get_param('INPUT_ID')
    logger.info(f"::set-output name=url::https://kaggle.com/{INPUT_ID}")
    print(f"::set-output name=url::https://kaggle.com/{INPUT_ID}")
    return

@logger.catch(onerror=lambda _: sys.exit(1))
def main():
    logger.info("Start")
    print_environment()
    perform_job()
    #get_files_status()
    send_output_param()
    logger.info("End")

    return

if __name__ == '__main__':
    main()
