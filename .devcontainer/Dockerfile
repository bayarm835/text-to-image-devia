FROM tensorflow/tensorflow:latest-gpu
VOLUME ./data/:/data
VOLUME .models:/models
RUN pip install --no-cache-dir scikit-learn matplotlib numpy mlflow boto3 psycopg2-binary tensorflow-datasets ipykernel minio ipywidgets tqdm --ignore-installed blinker