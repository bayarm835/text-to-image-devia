# text-to-image-devia

## Prérequis
Docker Desktop 
WSL - Ubuntu-22.04
[NVIDIA Container Toolkit sur WSL](https://docs.nvidia.com/datacenter/cloud-native/container-toolkit/latest/install-guide.html)  - [version 12.3](https://developer.nvidia.com/cuda-12-3-2-download-archive?target_os=Linux&target_arch=x86_64&Distribution=WSL-Ubuntu&target_version=2.0&target_type=deb_local)

## Arborescence du projet

```
├── README.md <- The top-level README for developers using this project.
├── data
│ ├── processed <- The final, canonical data sets for modeling.
│ └── raw <- The original, immutable data dump.
│
├── models <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks <- Jupyter notebooks. Naming convention is a number (for ordering),
│ the creator's initials, and a short - delimited description, e.g.
│ 1.0-jqp-initial-data-exploration.
│
├── references <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports <- Generated analysis as HTML, PDF, LaTeX, etc.
│ └── figures <- Generated graphics and figures to be used in reporting
│
├── setup.py <- makes project pip installable (pip install -e .) so src can be imported
├── src <- Source code for use in this project.
│ ├── init.py <- Makes src a Python module
│ │
│ ├── data <- Scripts to download or generate data
│ │ └── make_dataset.py
│ │
│ ├── features <- Scripts to turn raw data into features for modeling
│ │ └── build_features.py
│ │
│ ├── models <- Scripts to train models and then use trained models to make
│ │ │ predictions
│ │ ├── predict_model.py
│ │ └── train_model.py
│ │
│ └── visualization <- Scripts to create exploratory and results oriented visualizations
│ └── visualize.py
│
```

# Entraînement
`pdm run tensorflow` : Lance un entraînement sur le container tensorflow

Réaliser un entraînement :
    Créer un network mlflow : `docker network create mlflow`
    Reopen in dev container
    Réaliser les expérimentations


