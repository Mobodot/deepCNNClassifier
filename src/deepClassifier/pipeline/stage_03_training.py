from deepClassifier.config import ConfigurationManager
from deepClassifier.components import PrepareCallbacks
from deepClassifier.components import Training
from deepClassifier import logger


STAGE_NAME = "Training Stage"

def main():
    config = ConfigurationManager()
    
    callback_config = config.get_prepare_callbacks_config()
    callbacks = PrepareCallbacks(prepare_callback_config=callback_config)
    callbacks = callbacks.get_tb_ckpt_callbacks()
    
    training_config = config.get_training_config()
    training = Training(training_config=training_config)
    training.get_base_model()
    training.train_valid_generator()
    training.train(callback_list=callbacks)
    
    
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