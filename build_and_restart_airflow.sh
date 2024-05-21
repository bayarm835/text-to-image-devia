pdm build
docker compose  -f "docker-compose.yaml" up -d --build airflow-init airflow-scheduler airflow-triggerer airflow-webserver