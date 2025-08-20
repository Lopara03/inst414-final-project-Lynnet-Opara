import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

def evaluate_model(model, X_test, y_test, average='binary'):
    """
    Evaluates the trained model on test data.
    
    Args:
        model: trained model
        X_test: test features
        y_test: true labels
        average: 'binary' or 'macro' for multiclass
        
    Returns:
        dict: evaluation metrics
    """
    try:
        preds = model.predict(X_test)

        metrics = {
            "accuracy": accuracy_score(y_test, preds),
            "precision": precision_score(y_test, preds, zero_division=0, average=average),
            "recall": recall_score(y_test, preds, zero_division=0, average=average),
            "f1": f1_score(y_test, preds, zero_division=0, average=average)
        }

        return metrics
    except Exception as e:
        print(f"Error in evaluate_model(): {e}")
        return None


def save_metrics_and_plots(metrics_dict, save_path='/Users/lynnetopara/Desktop/INST414/inst414-final-project-Lynnet-Opara/data/model-eval/'):
    """
    Saves metrics dict as CSV and plots bar charts.
    """
    import os
    os.makedirs(save_path, exist_ok=True)

    metrics_df = pd.DataFrame([metrics_dict])
    metrics_df.to_csv(os.path.join(save_path, 'metrics_table.csv'), index=False)

    # plot each metric
    plt.figure(figsize=(6,4))
    plt.bar(metrics_dict.keys(), metrics_dict.values(), color='skyblue')
    plt.title('Model Evaluation Metrics')
    plt.ylabel('Score')
    plt.ylim(0,1)
    plt.savefig(os.path.join(save_path, 'metrics_barplot.png'))
    plt.close()


if __name__ == "__main__":
    example_metrics = {
        'accuracy': 0.85,
        'precision': 0.82,
        'recall': 0.80,
        'f1': 0.81
    }
    save_metrics_and_plots(example_metrics)
