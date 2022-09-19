
from deepClassifier import logger
from deepClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from deepClassifier.utils import read_yaml, create_directories
from deepClassifier.entity.config_entity import DataIngestionConfig


class ConfigurationManager:
    
    def __init__(
        self, 
        config_filepath=CONFIG_FILE_PATH, 
        params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
        
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        try:
            data_ingestion = self.config.data_ingestion
            
            create_directories([data_ingestion.root_dir])
            
            data_ingestion_config = DataIngestionConfig(
                root_dir=data_ingestion.root_dir,
                source_url=data_ingestion.source_url,
                local_data_file=data_ingestion.local_data_file,
                unzipped_dir=data_ingestion.unzipped_dir
            )
            return data_ingestion_config
        
        except Exception as e:
            raise e
        
        