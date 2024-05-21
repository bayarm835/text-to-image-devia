from airflow.decorators import dag, task
import os
from datetime import datetime, timedelta
import pendulum
import docker

#from text_to_image_devia.models.train import training

@dag(
    schedule=None,
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    tags=["example"],
)
def training():
    """
    ## DAG to train the text-to-image model.
    
    """
    @task.bash
    def run_training_container():
        """
        Run the training container with text-to-image/models/train.py script.

        Returns:
            - Execution of the training container.
            - MLflow logs
            - 
            
    """
    return "docker-compose run --gpus all --build train"
    # "docker run --name training_container --rm --gpus all --net mlflow text-to-image-devia-train:latest"
    run_training_container()
training()


