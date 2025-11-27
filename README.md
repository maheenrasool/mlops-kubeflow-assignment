MLflow MLOps Pipeline with DVC & GitHub Workflows

A complete end-to-end MLOps project implementing dataset versioning, experiment tracking, reproducible pipelines, and CI/CD automation.

Project Overview

This repository contains an end-to-end MLOps pipeline built for the Boston Housing dataset using:

DVC → Dataset versioning & remote storage

MLflow → Experiment tracking & pipeline orchestration (replacing Kubeflow)

GitHub Workflows → CI/CD automation

Scikit-learn → Model training

Docker → Container environment for MLflow pipeline execution

The pipeline performs:

Data Extraction (from DVC remote)

Data Preprocessing (scaling + train/test split)

Model Training (Random Forest)

Model Evaluation (RMSE, MAE logged to MLflow)

Artifact Logging (model saved to MLflow registry)

Project Structure
```
mlops-mlflow-assignment/
│
├── data/
│   ├── raw/               # DVC-tracked dataset
│   └── processed/         # Train/Test split 
│
├── src/
│   ├── pipeline_components.py  # MLflow steps (extract, preprocess, train, evaluate)
│   ├── model_training.py       # Standalone training script
│   └── utils.py                # Helper functions
│
├── mlflow_pipeline.py          # MLflow Orchestrated Pipeline
├── Dockerfile                   # Optional Docker container for the pipeline
├── requirements.txt             # Project dependencies
├── .dvc/                        # DVC metadata
├── .gitignore
└── .github/workflows/mlops.yml  # CI/CD pipeline

```

Setup Instructions
1. Clone the repository
```
git clone https://github.com/<your-username>/mlops-mlflow-assignment.git
cd mlops-mlflow-assignment
```

3. Install dependencies

Using pip:
```
pip install -r requirements.txt
```
3. Set up DVC

Initialize and pull the dataset:
```
dvc pull
```

This downloads the dataset from the configured DVC remote storage.

4. Run the MLflow Pipeline
Option A → Run using MLflow CLI
```
mlflow run .
```
Option B → Run manually
```
python pipeline.py
```

5. View MLflow Dashboard

Start MLflow UI:
```
mlflow ui
```

Open:
```
  http://127.0.0.1:5000
```
You will see:

Model versions

Metrics (RMSE, r2_score)

Artifacts (trained model, plots, logs)

6. CI/CD with GitHub Workflows

A complete CI/CD workflow runs automatically:

✔ Installs dependencies
✔ Verifies the MLflow pipeline compiles
✔ Runs MLflow experiment
✔ Ensures repo is production-ready


Pipeline Steps
1. Data Extraction

Pull dataset using DVC

Validate file integrity

2. Preprocessing

Scaling

Train/Test split

Saving processed files

3. Model Training

Random Forest Regressor

Save model as MLflow artifact

4. Evaluation

RMSE


R² Score

Metrics logged automatically.

🧪 Dataset Used

Boston Housing Dataset

Technologies Used
Tool	Purpose
DVC	Data versioning
MLflow	Experiment tracking & model logging
Python	Core implementation
Scikit-learn	ML model
