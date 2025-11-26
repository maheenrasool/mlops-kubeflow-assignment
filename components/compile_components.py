import os
import sys
from kfp.components import create_component_from_func

#  Add project root to Python path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

#  Import the real functions
from src.pipeline_components import (
    extract_data,
    preprocess_data,
    train_model,
    evaluate_model
)

OUTPUT_DIR = "components"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def compile_component(func, filename):
    output_path = os.path.join(OUTPUT_DIR, filename)
    print(f" Compiling: {filename}")

    create_component_from_func(
        func,
        base_image="python:3.8",
        output_component_file=output_path
    )

    print(f" Saved → {output_path}")

if __name__ == "__main__":
    print("\n Compiling Kubeflow components using KFP v1...\n")

    compile_component(extract_data, "extract_data_component.yaml")
    compile_component(preprocess_data, "preprocess_component.yaml")
    compile_component(train_model, "train_model_component.yaml")
    compile_component(evaluate_model, "evaluate_model_component.yaml")

    print("\n All components successfully generated!\n")
