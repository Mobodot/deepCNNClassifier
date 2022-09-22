from deepClassifier.config import ConfigurationManager
from deepClassifier.components import DataIngestion
from deepClassifier import logger

STAGE_NAME = "Data Ingestion Stage"

def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_data()
    data_ingestion.unzip_and_clean()
    
    
if __name__ == "__main__":
    try:
        print("\n")
        logger.info("\n")
        logger.info(">"*30)
        logger.info(f"Data {STAGE_NAME} Started")
        main()
        logger.info(f"Data {STAGE_NAME} completed")
        logger.info("*"*30)
        
        print("\n")
    except Exception as e:
        raise e