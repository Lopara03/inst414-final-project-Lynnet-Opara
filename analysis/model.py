"""
this module trains a classification model (e.g., logistic regression)
"""

import logging
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from .evaluate import evaluate_model

def run_model(df, features, target):
    """
    trains a classification model on the dataset.

    args:
        df (DataFrame): Cleaned dataset
        features (list): List of feature column names
        target (str): Target column name

    returns:
        tuple: trained model, evaluation metrics dict
    """
    logger = logging.getLogger("pipeline_logger")
    
    try:
        X = df[features]
        y = df[target]

        X_train, X_test, y_train, y_test = train_test_split(
            X, y, test_size=0.2, random_state=42
        )

        model = LogisticRegression(max_iter=1000)
        model.fit(X_train, y_train)
        logger.info("Model trained successfully.")

        metrics = evaluate_model(model, X_test, y_test)
        logger.info(f"Evaluation metrics: {metrics}")

        return model, metrics
    except Exception as e:
        logger.error(f"Error in run_model(): {e}")
        return None, None

