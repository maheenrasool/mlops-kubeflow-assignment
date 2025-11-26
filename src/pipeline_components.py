import os
import shutil
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import json
import mlflow

# ============================================================
# 1. DATA EXTRACTION
# ============================================================
def extract_data(dataset_path: str, output_path: str):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    shutil.copy(dataset_path, output_path)


# ============================================================
# 2. DATA PREPROCESSING
# ============================================================
def preprocess_data(dataset_path: str, output_dir: str):
    os.makedirs(output_dir, exist_ok=True)
    df = pd.read_csv(dataset_path).dropna()

    # Remove classification target column if exists
    if "CAT.MEDV" in df.columns:
        df = df.drop("CAT.MEDV", axis=1)

    # Separate features and target
    X = df.drop("MEDV", axis=1)
    y = df["MEDV"]

    X_scaled = StandardScaler().fit_transform(X)

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled, y, test_size=0.2, random_state=42
    )

    joblib.dump(X_train, f"{output_dir}/X_train.pkl")
    joblib.dump(X_test, f"{output_dir}/X_test.pkl")
    joblib.dump(y_train, f"{output_dir}/y_train.pkl")
    joblib.dump(y_test, f"{output_dir}/y_test.pkl")


# ============================================================
# 3. MODEL TRAINING
# ============================================================
def train_model(preprocessed_dir: str, model_output_path: str):
    os.makedirs(os.path.dirname(model_output_path), exist_ok=True)

    X_train = joblib.load(f"{preprocessed_dir}/X_train.pkl")
    y_train = joblib.load(f"{preprocessed_dir}/y_train.pkl")

    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    joblib.dump(model, model_output_path)


# ============================================================
# 4. MODEL EVALUATION
# ============================================================
def evaluate_model(preprocessed_dir: str, model_path: str, metrics_output: str):
    X_test = joblib.load(f"{preprocessed_dir}/X_test.pkl")
    y_test = joblib.load(f"{preprocessed_dir}/y_test.pkl")
    model = joblib.load(model_path)

    predictions = model.predict(X_test)

    rmse = mean_squared_error(y_test, predictions, squared=False)
    r2 = r2_score(y_test, predictions)

    # Save to JSON file
    metrics = {"rmse": rmse, "r2_score": r2}

    with open(metrics_output, "w") as f:
        json.dump(metrics, f, indent=4)

    # Log metrics to MLflow (important for Task 3 screenshot)
    mlflow.log_metric("rmse", rmse)
    mlflow.log_metric("r2_score", r2)

