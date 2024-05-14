import tensorflow as tf
import tensorflow_datasets as tfds
from tensorflow import keras

print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Load the mnist dataset.
train_ds, test_ds = tfds.load(
    "mnist",
    split=["train", "test"],
    shuffle_files=True,
)

def preprocess_fn(data):
    image = tf.cast(data["image"], tf.float32) / 255
    label = data["label"]
    return (image, label)


train_ds = train_ds.map(preprocess_fn).batch(128).prefetch(tf.data.AUTOTUNE)
test_ds = test_ds.map(preprocess_fn).batch(128).prefetch(tf.data.AUTOTUNE)

input_shape = (28, 28, 1)
num_classes = 10

model = keras.Sequential(
    [
        keras.Input(shape=input_shape),
        keras.layers.Conv2D(32, kernel_size=(3, 3), activation="relu"),
        keras.layers.MaxPooling2D(pool_size=(2, 2)),
        keras.layers.Conv2D(64, kernel_size=(3, 3), activation="relu"),
        keras.layers.MaxPooling2D(pool_size=(2, 2)),
        keras.layers.Flatten(),
        keras.layers.Dropout(0.5),
        keras.layers.Dense(num_classes, activation="softmax"),
    ]
)

import mlflow

mlflow.login()




with mlflow.start_run():
    mlflow.log_param("lr", 0.001)
    # Your ml code
    ...
    mlflow.log_metric("val_loss", val_loss)
    
tf.keras