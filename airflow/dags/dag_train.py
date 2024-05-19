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
def tutorial_taskflow_api():
    """
    ### TaskFlow API Tutorial Documentation
    This is a simple data pipeline example which demonstrates the use of
    the TaskFlow API using three simple tasks for Extract, Transform, and Load.
    Documentation that goes along with the Airflow TaskFlow API tutorial is
    located
    [here](https://airflow.apache.org/docs/apache-airflow/stable/tutorial_taskflow_api.html)
    """
    #@task.bash
    #def build_training_image():
    
    
    #    return 'docker build --pull --rm -f "src/text_to_image_devia/models/dockerfile" -t texttoimagedevia:latest "src/text_to_image_devia/models"' 
    #@task.bash
    #def build_training_image():
    #    return 'docker build --pull -t text-to-image-devia-train:latest "src/text_to_image_devia/models"'
    
    #@task()
    #def build_container():
    #    client = docker.from_env()
    #    client.images.build(path="/tmp", dockerfile="DockerFile",  tag="text-to-image-devia-train:latest")
    #    return "Container built"
    
    
    @task.bash
    def run_training_container():
            return "docker run --name training_container --rm --gpus all --network mlflow text-to-image-devia-train:latest"
    run_training_container()
tutorial_taskflow_api()
