from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareBaseModel
from deepClassifier import logger


STAGE_NAME = "Prepare Base Model Stage"

def main():

    config = ConfigurationManager()
    prepare_base_model_config = config.get_prepare_base_model()
    prepare_base_model = PrepareBaseModel(
        prepare_base_model_config=prepare_base_model_config
        )
    # prepare_base_model.get_base_model()
    prepare_base_model.update_base_model()
    

if __name__ == "__main__":
    try:
        print("\n")
        logger.info(">"*30)
        logger.info("Prepare Base Model Stage Started")
        main()
        logger.info("Prepare Base Model Stage completed")
        logger.info("*"*30)
        print("\n")
    except Exception as e:
        raise e
    
    