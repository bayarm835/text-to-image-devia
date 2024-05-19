FROM apache/airflow:2.9.1-python3.9
COPY /dist/text_to_image_devia-0.1.0-py3-none-any.whl /opt/airflow/dist/
COPY /docker-compose.yaml /tmp
COPY /src/text_to_image_devia/models/DockerFile /tmp
RUN pip install --upgrade pip && pip install --no-cache-dir dist/text_to_image_devia-0.1.0-py3-none-any.whl
