import mlflow

# TensorFlow and tf.keras
import tensorflow as tf
from tensorflow import keras
from mlflow.tensorflow import MlflowCallback

print(tf.config.list_physical_devices('GPU'))

fashion_mnist = keras.datasets.fashion_mnist

(train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()

train_images = train_images / 255.0

test_images = test_images / 255.0

model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),
    keras.layers.Dense(128, activation='relu'),
    keras.layers.Dense(10)
])

model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True))

mlflow.set_tracking_uri("http://mlflow-server:5000") #  connects to a tracking URI.

mlflow.set_experiment("/mlflow-tf-fashion-mnist")

mlflow.tensorflow.autolog(disable=True)

with mlflow.start_run() as run:
    model.fit(
        x=train_images,
        y=train_labels,
        epochs=10,
        callbacks=[MlflowCallback(run)],
    )

test_loss, test_acc = model.evaluate(test_images,  test_labels, verbose=2)

print('\nTest accuracy:', test_acc)







# Turn off autologging.






#print("Hello world ! Ca va ?")