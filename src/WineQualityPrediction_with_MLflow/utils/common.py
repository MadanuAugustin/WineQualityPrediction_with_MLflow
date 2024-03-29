
## utils file is used for storing the common functionalities in the project without re-writing the code thus saving memory and time.
## re-usability of code

import os
from box.exceptions import BoxValueError
import yaml
from src.WineQualityPrediction_with_MLflow import logger
import json
import joblib
from box import ConfigBox
from pathlib import Path
from typing import Any

## BoxValueError is a exception handler instead of creating custom exception
## after reading the yaml file it is returned as ConfigBox

# read_yaml function is used for reading yaml files


def read_yaml(path_to_yaml:Path) -> ConfigBox:
    # """
    # reads yaml files and returns

    # Args: 
        # path_to_yaml(str):path like input

    # Raises : 
    #         ValueError: if yaml file is empty
    #         e : empty file

    # Returns : 
    # ConfigBox : ConfigBox type
    # """
    try:
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
        
    except BoxValueError: 
        raise ValueError("yaml is empty")
    except Exception as e:
        raise e




def create_directories(path_to_directories: list, verbose = True):
    # """
    # create list of directories

    # Args:
    #     path_to_directories (list) : list of path of directories
    #     ignore_log (bool, optional) : ignore if multiple dirs is to be created. Defaults to False
    # """
    for path in path_to_directories:
        os.makedirs(path, exist_ok= True)
        
        if verbose:
            logger.info(f"created directory at : {path}")



def save_json(path : Path, data : dict):
    # """
    # save json data

    # Args:
    #     path (Path) : path to json file
    #     data (dict) : data to be saved in json file
    # """

    with open(path, 'w') as f:
        json.dump(data, f, indent=4)
    
    logger.info(f"json file saved at : {path}")



def load_json(path : Path) -> ConfigBox:
    # """
    # load json files data

    # Args : 
    #     path (Path) : path to json file


    # Returns:
    #     ConfigBox : data as class attributes instead of dict
    # """

    with open(path) as f:
        content = json.load(f)

    
    logger.info(f"json file loaded successfully from : {path}")

    return ConfigBox(content)


def save_bin(data : Any, path : Path):
    # """
    # save binary file

    # Args:
    #     data (Any): data to be saved as binary
    #     path (Path) : path to binary file
    # """

    joblib.dump(value = data, filename = path)
    logger.info(f"binary file saved at : {path}")



def load_bin(path : Path) -> Any:
    # """
    # load binary data

    # Args:
    #     path (Path) : path to binary file
    
    # Returns:
    #     Any : object stored in the file

    # """
    data = joblib.load(path)
    logger.info(f"binary file loaded from {path}")
    return data


def get_size(path: Path) -> str:
    # """get size in KB

    # Args:
    #     path (Path): path of the file

    # Returns:
    #     str: size in KB
    # """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"
    

