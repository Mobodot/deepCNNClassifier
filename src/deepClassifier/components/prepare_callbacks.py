import tensorflow as tf
from typing import List
import time
import os
from deepClassifier.entity import PrepareCallbacksConfig


class PrepareCallbacks:
    
    def __init__(self, 
                 prepare_callback_config: PrepareCallbacksConfig):
        self.config = prepare_callback_config
    
    @property
    def _prepare_tb_callback(self) -> tf.keras.callbacks.TensorBoard:
        timestamp = time.strftime("%Y-%m-%d-%H-%M-%S")
        tensorboard_root_log_dir = os.path.join(
            self.config.tensorboard_root_log_dir,
            f"tb_logs_at_{timestamp}"
        )
        
        return tf.keras.callbacks.TensorBoard(
            log_dir=tensorboard_root_log_dir
        )
    
    @property
    def _prepare_ckpt_callback(self) -> tf.keras.callbacks.ModelCheckpoint:
        return tf.keras.callbacks.ModelCheckpoint(
            filepath=self.config.checkpoint_model_filepath,
            save_best_only=True
        )
        
    def get_tb_ckpt_callbacks(self) -> List:
        return [
            self._prepare_tb_callback,
            self._prepare_ckpt_callback
            ]
        