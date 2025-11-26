import mlflow
import mlflow.sklearn
import os

from pipeline_components import (
    extract_data,
    preprocess_data,
    train_model,
    evaluate_model
)

# Paths
RAW_DATA_DVC = "data/BostonHousing.csv"
RAW_DATA_OUT = "data/raw_data.csv"
PREP_DIR = "data/preprocessed"
MODEL_PATH = "models/model.pkl"
METRICS_PATH = "models/metrics.json"

def run_pipeline():
    mlflow.set_tracking_uri("file:./mlruns")   # local MLflow storage
    mlflow.set_experiment("MLflow Housing Pipeline")

    with mlflow.start_run():

        mlflow.log_param("dataset_version", RAW_DATA_DVC)

        print("\n=== Step 1: Data Extraction ===")
        extract_data(RAW_DATA_DVC, RAW_DATA_OUT)
        mlflow.log_artifact(RAW_DATA_OUT)

        print("\n=== Step 2: Data Preprocessing ===")
        preprocess_data(RAW_DATA_OUT, PREP_DIR)
        mlflow.log_artifact(PREP_DIR)

        print("\n=== Step 3: Model Training ===")
        train_model(PREP_DIR, MODEL_PATH)
        mlflow.log_artifact(MODEL_PATH)

        print("\n=== Step 4: Model Evaluation ===")
        evaluate_model(PREP_DIR, MODEL_PATH, METRICS_PATH)
        mlflow.log_artifact(METRICS_PATH)

        print("\nPipeline completed successfully!")

if __name__ == "__main__":
    run_pipeline()
