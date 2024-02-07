
from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen = True)
class DataIngestionConfig:
    root_dir : Path
    source_URL : str
    local_data_file : Path
    unzip_dir : Path



@dataclass(frozen = True)
class DataValidationConfig:
    root_dir : Path
    unzip_data_dir : Path
    STATUS_FILE : str
    # I want to read the schema.yaml file and save the data as a dictionary format
    all_schema : dict


@dataclass
class DataTransformationConfig:
    root_dir : Path
    data_path : Path