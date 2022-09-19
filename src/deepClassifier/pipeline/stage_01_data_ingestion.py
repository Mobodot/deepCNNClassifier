from symbol import except_clause
from deepClassifier.config import ConfigurationManager
from deepClassifier.components import DataIngestion
from deepClassifier import logger


def main():
    config = ConfigurationManager()
    data_ingestion_config = config.get_data_ingestion_config()
    data_ingestion = DataIngestion(config=data_ingestion_config)
    data_ingestion.download_data()
    data_ingestion.unzip_and_clean()
    
    
if __name__ == "__main__":
    try:
        print("\n")
        logger.info(">"*30)
        logger.info("Data Ingestion Stage Started")
        main()
        logger.info("Data ingestion stage completed")
        logger.info("*"*30)
        print("\n")
    except Exception as e:
        raise e