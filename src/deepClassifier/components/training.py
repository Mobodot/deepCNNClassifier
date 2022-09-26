import tensorflow as tf
import time
from pathlib import Path
import os
from deepClassifier import logger
from deepClassifier.entity import (
    TrainingConfig)


class Training:
    
    def __init__(
        self,
        training_config: TrainingConfig
    ):
        self.config = training_config
        
    def get_base_model(self) -> None:
        logger.info("Loading updated base model..")
        self.model = tf.keras.models.load_model(
            self.config.updated_base_model_path
        )
        
    def train_valid_generator(self):
        # goal: split data in train and validation set and pass its params
        datagenerator_kwargs = dict(
            rescale = 1./255,
            validation_split=0.20
        )
        
        dataflow_kwargs = dict(
            target_size=self.config.params_image_size[:-1],
            batch_size=self.config.params_batch_size,
            interpolation="bilinear"
        )
        
        valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            **datagenerator_kwargs
        )
        
        logger.info("loading and preprocessing image batches for validation...")
        self.valid_generator = valid_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="validation",
            shuffle=False,
            **dataflow_kwargs
        )
        
        if self.config.params_is_augmentation:
            train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range=40,
                horizontal_flip=True,
                width_shift_range=True,
                height_shift_range=0.2,
                shear_range=0.2,
                zoom_range=0.2,
                **datagenerator_kwargs
            )
        else:
            train_datagenerator = valid_datagenerator
        
        logger.info("loading and preprocessing image batches for training...")
        self.train_generator = train_datagenerator.flow_from_directory(
            directory=self.config.training_data,
            subset="training",
            shuffle=True,
            **dataflow_kwargs
        )
        
        
    def train(self, callback_list: list) -> None:
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size
        
        self.model.fit(
            self.train_generator,
            epochs=self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator,
            callbacks=callback_list
        )
        
        self.save_model(
            path=self.config.trained_model_path,
            model=self.model
        )
        
    @staticmethod
    def save_model(path: Path, model: tf.keras.Model) -> None:
        model.save(path)
