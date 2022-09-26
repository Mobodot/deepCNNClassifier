from deepClassifier import logger
from deepClassifier.entity import PrepareBaseModelConfig
from pathlib import Path
import tensorflow as tf
import os

class PrepareBaseModel:
    def __init__(
        self, 
        prepare_base_model_config: PrepareBaseModelConfig):
            self.config = prepare_base_model_config
            self._is_model_exists = False
            
    def get_base_model(self):
        logger.info("Trying to download VGG16 as base model...")
        if os.path.split(self.config.base_model_path)[-1] != "base_model.h5":
            self.model = tf.keras.applications.vgg16.VGG16(
                include_top=self.config.params_include_top,
                weights=self.config.params_weights,
                input_shape=self.config.params_image_size,
            )
            
            self.save_model(
                path=self.config.base_model_path,
                model=self.model)
            logger.info(f"Base model: [VGG16] saved at: [{self.config.base_model_path}]")
        else:
            logger.info(f"Base model VGG16 already exists at: [{self.config.base_model_path}]")
            self._is_model_exists = True
        
        
    @staticmethod
    def _prepare_full_model(
        model,
        classes,
        freeze_all,
        freeze_till,
        learning_rate
        ):
            if freeze_all:
                logger.info("Freezing all layers of base model")
                for layer in model.layers:
                    model.trainable = False
            elif (freeze_till is not None) and (freeze_till > 0):
                logger.info(f"Freezing all other layers except last {freeze_till}")
                for layer in model.layers[:-freeze_till]:
                    model.trainable = False
                    
                    
            flatten_in = tf.keras.layers.Flatten()(model.output)
            prediction = tf.keras.layers.Dense(
                units=classes,
                activation="softmax"
            )(flatten_in)
            
            logger.info("Creating new updated base model...")
            full_model = tf.keras.models.Model(
                inputs=model.inputs,
                outputs=prediction
            )
            
            logger.info("Compiling updated base model...")
            full_model.compile(
                optimizer=tf.keras.optimizers.SGD(learning_rate=learning_rate),
                loss=tf.keras.losses.CategoricalCrossentropy(),
                metrics=["accuracy"]
            )
            
            full_model.summary()
            
            return full_model
    
    def update_base_model(self):
        # newly added lines for getting basemodel
        
        if self._is_model_exists:
            logger.info("loading base model...")
            self.model = tf.keras.models.load_model(
                self.config.base_model_path
            )
        else:
            logger.info("Updating base model[VGG16] params...")
            

        self.full_model = self._prepare_full_model(
            model=self.model,
            classes=self.config.params_classes,
            freeze_all=True,
            freeze_till=None,
            learning_rate=self.config.params_learning_rate
        )
        
        logger.info(f"Updated base model saved at: [{self.config.updated_base_model_path}]")
        self.save_model(path=self.config.updated_base_model_path,
                        model=self.full_model)

    @staticmethod
    def save_model(path: Path, model: tf.keras.Model):
        model.save(path)    
    