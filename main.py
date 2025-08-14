"""
main script to run the ETL, analysis, and visualization pipeline 
for mental health trends in undergraduate students.
"""

import logging
import os
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

from etl.extract import extract_hms, extract_yrbss
from etl.transform import clean_data
from etl.load import save_data  
from analysis.model import run_model
from analysis.evaluate import evaluate_model
from vis import visualizations as visualize  


def setup_logger():
    """set up a logger to capture info and errors."""
    logger = logging.getLogger("pipeline_logger")
    logger.setLevel(logging.INFO)

    # file handler
    fh = logging.FileHandler("pipeline.log")
    fh.setLevel(logging.INFO)

    # console handler
    ch = logging.StreamHandler()
    ch.setLevel(logging.INFO)

    # formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter)
    ch.setFormatter(formatter)

    # add handlers
    if not logger.hasHandlers():
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger


def main():
    """entry point to run the full project pipeline."""
    logger = setup_logger()
    logger.info("Pipeline started")

    # 1. extract data
    try:
        logger.info("Extracting HMS data...")
        hms_df = extract_hms("/Users/lynnetopara/Desktop/INST414/inst414-final-project-Lynnet-Opara/data/extracted/HMS_2022-2023_PUBLIC_instchars2.csv")
        logger.info(f"HMS data loaded, shape: {hms_df.shape}")

        logger.info("Extracting YRBSS data...")
        yrbss_df = extract_yrbss("/Users/lynnetopara/Desktop/INST414/inst414-final-project-Lynnet-Opara/data/extracted/Youth_Risk_Behavioral_Surveillance_System__YRBSS__-_Mental_Health_Indicators_20250801.csv")
        logger.info(f"YRBSS data loaded, shape: {yrbss_df.shape}")

    except Exception as e:
        logger.error(f"Error during data extraction: {e}")
        return

    # 2. transform data
    try:
        logger.info("Cleaning HMS data...")
        hms_clean = clean_data(hms_df)
        logger.info(f"HMS data cleaned, shape: {hms_clean.shape}")

        logger.info("Cleaning YRBSS data...")
        yrbss_clean = clean_data(yrbss_df)
        logger.info(f"YRBSS data cleaned, shape: {yrbss_clean.shape}")

    except Exception as e:
        logger.error(f"Error during data cleaning: {e}")
        return

    # 3. load / merge data
    try:
        logger.info("Merging datasets...")
        # If save_data just writes a file, you need a merge function; otherwise, just merge here
        full_data = pd.concat([hms_clean, yrbss_clean], ignore_index=True)
        save_data(full_data, "data/processed/full_data.csv")
        logger.info(f"Data merged and saved, shape: {full_data.shape}")

    except Exception as e:
        logger.error(f"Error during data merging/loading: {e}")
        return

    # 4. modeling / evaluation
    hms = pd.read_csv("HMS_2022-2023_PUBLIC_instchars2csv")
    try:
        logger.info("Running predictive model and evaluating...")

        # example: defining my target column and feature columns
        hms['mental_health_risk'] = hms['dep_any'] | hms['anx_any'] | hms['anymhprob']
        # replace with my actual target column
        feature_cols = [c for c in full_data.columns if c != target_col]

        X = full_data[feature_cols]
        y = full_data[target_col]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        # train model
        model = run_model(X_train, y_train)  # returns trained model

        # evaluate
        evaluation_metrics = evaluate_model(model, X_test, y_test)
        logger.info(f"Evaluation Metrics: {evaluation_metrics}")

        #  metrics CSV
        os.makedirs("data/model-eval", exist_ok=True)
        metrics_df = pd.DataFrame([evaluation_metrics])
        metrics_df.to_csv("data/model-eval/metrics_table.csv", index=False)
        logger.info("Evaluation metrics saved to data/model-eval/metrics_table.csv")

        #  bar chart
        os.makedirs("data/visualizations", exist_ok=True)
        plt.figure(figsize=(6,4))
        plt.bar(evaluation_metrics.keys(), evaluation_metrics.values(), color='skyblue')
        plt.title("Model Evaluation Metrics")
        plt.ylabel("Score")
        plt.ylim(0,1)
        plt.savefig("data/visualizations/metrics_barplot.png")
        plt.close()
        logger.info("Evaluation metrics bar chart saved to data/visualizations/metrics_barplot.png")

    except Exception as e:
        logger.error(f"Error during modeling/evaluation: {e}")
        return

    # 5. visualizations
    try:
        logger.info("Generating additional visualizations...")
        visualize(full_data)  # adapt based on my visualizations module
        logger.info("Visualizations complete")
    except Exception as e:
        logger.error(f"Error during visualization: {e}")

    logger.info("Pipeline finished successfully")


if __name__ == "__main__":
    main()
