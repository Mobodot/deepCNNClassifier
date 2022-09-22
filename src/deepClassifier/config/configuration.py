
from deepClassifier import logger
from pathlib import Path
from deepClassifier.constants import CONFIG_FILE_PATH, PARAMS_FILE_PATH
from deepClassifier.utils import read_yaml, create_directories
from deepClassifier.entity.config_entity import (
    DataIngestionConfig, 
    PrepareBaseModelConfig
)

class ConfigurationManager:
    
    def __init__(
        self, 
        config_filepath=CONFIG_FILE_PATH, 
        params_filepath=PARAMS_FILE_PATH):
        self.config = read_yaml(config_filepath)
        self.params = read_yaml(params_filepath)
        create_directories([self.config.artifacts_root])
        
        
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        data_ingestion = self.config.data_ingestion
        
        create_directories([data_ingestion.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir=Path(data_ingestion.root_dir),
            source_url=Path(data_ingestion.source_url),
            local_data_file=Path(data_ingestion.local_data_file),
            unzipped_dir=Path(data_ingestion.unzipped_dir)
        )
        return data_ingestion_config
        
        
    def get_prepare_base_model(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model
        
        create_directories([config.root_dir])
        
        return PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_classes=self.params.CLASSES,
            params_learning_rate=self.params.LEARNING_RATE
        )
        