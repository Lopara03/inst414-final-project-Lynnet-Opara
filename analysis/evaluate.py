
"""
this module evaluates the performance of the model using various metrics
"""
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(model, X_test, y_test):
    """
    evaluates the trained model on test data.

    args:
        model: trained model
        X_test: test features
        y_test: true labels

    returns:
        dict: evaluation metrics (accuracy, precision, recall, f1)
    """
    try:
        preds = model.predict(X_test)

        metrics = {
            "accuracy": accuracy_score(y_test, preds),
            "precision": precision_score(y_test, preds, zero_division=0),
            "recall": recall_score(y_test, preds, zero_division=0),
            "f1": f1_score(y_test, preds, zero_division=0)
        }

        return metrics
    except Exception as e:
        # If logging is set up in main.py, this will show errors there
        print(f"Error in evaluate_model(): {e}")
        return None

def save_metrics_and_plots(metrics_dict):
    # Convert dict to DataFrame
    metrics_df = pd.DataFrame(metrics_dict)
    
    # Save metrics table
    metrics_df.to_csv('/Users/lynnetopara/Desktop/INST414/inst414-final-project-Lynnet-Opara/data/model-eval/metrics_table.csv', index=False)
    
    # Example: save accuracy plot
    plt.bar(metrics_df['Model'], metrics_df['Accuracy'])
    plt.ylabel('Accuracy')
    plt.title('Model Accuracy Comparison')
    plt.close()  # avoids overlapping plots if you call multiple times

if __name__ == "__main__":
    metrics = {
        'Model': ['Logistic Regression', 'Decision Tree'],
        'Accuracy': [0.85, 0.78],
        'Precision': [0.82, 0.76],
        'Recall': [0.80, 0.75]
    }
    save_metrics_and_plots(metrics)
