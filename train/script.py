import os
import tensorflow as tf # type: ignore
    
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))