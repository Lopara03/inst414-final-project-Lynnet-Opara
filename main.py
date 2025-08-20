"""
main script to run the ETL, analysis, and visualization pipeline 
for adult and student mental health datasets.
"""

import logging
import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def setup_logger():
    """Set up a logger to capture info and errors."""
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

    if not logger.hasHandlers():
        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger


def main():
    logger = setup_logger()
    logger.info("Pipeline started")

    # -------------------------
    # 1. extract data
    # -------------------------
    try:
        adult_file = "/Users/lynnetopara/Desktop/INST414/inst414-final-project-Lynnet-Opara/data/extracted/adult-depression-lghc-indicator-24.csv"
        students_file = "/Users/lynnetopara/Desktop/INST414/inst414-final-project-Lynnet-Opara/data/extracted/students_mental_health_survey.csv"


        adult_df = pd.read_csv(adult_file)
        students_df = pd.read_csv(students_file)

        logger.info(f"Adult dataset loaded, shape: {adult_df.shape}")
        logger.info(f"Students dataset loaded, shape: {students_df.shape}")

    except Exception as e:
        logger.error(f"Error loading datasets: {e}")
        return

    # -------------------------
    # 2. transform / clean data
    # -------------------------
    try:
        # adult dataset
        adult_df = adult_df.dropna(subset=["Percent"])
        adult_df["Year"] = adult_df["Year"].astype(int)

        # Students dataset
        students_df = students_df.dropna(subset=["Depression_Score"])
        students_df["Age"] = students_df["Age"].astype(int)
        students_df["CGPA"] = students_df["CGPA"].astype(float)
        students_df["Stress_Level"] = students_df["Stress_Level"].astype(int)
        students_df["Depression_Score"] = students_df["Depression_Score"].astype(int)
        students_df["Anxiety_Score"] = students_df["Anxiety_Score"].astype(int)

        logger.info("Both datasets cleaned successfully")

    except Exception as e:
        logger.error(f"Error cleaning datasets: {e}")
        return

    # -------------------------
    # 3. save cleaned datasets
    # -------------------------
    try:
        os.makedirs("data/processed", exist_ok=True)
        adult_df.to_csv("data/processed/cleaned_adult_depression.csv", index=False)
        students_df.to_csv("data/processed/cleaned_students_mental_health.csv", index=False)
        logger.info("Both datasets saved successfully")
    except Exception as e:
        logger.error(f"Error saving cleaned datasets: {e}")

    # -------------------------
    # 4. visualizations
    # -------------------------
    try:
        os.makedirs("data/visualizations", exist_ok=True)

        # --- adult dataset visualizations ---
        adult_total = adult_df[adult_df["Strata"] == "Total"]
        plt.figure(figsize=(8,5))
        plt.plot(adult_total["Year"], adult_total["Percent"], marker="o", color="navy")
        plt.title("Adult Depression Rates Over Time")
        plt.xlabel("Year")
        plt.ylabel("Percent")
        plt.grid(True)
        plt.savefig("data/visualizations/depression_trend_adult.png")
        plt.close()

        latest_year = adult_df["Year"].max()
        adult_latest = adult_df[adult_df["Year"] == latest_year]
        plt.figure(figsize=(10,6))
        sns.barplot(data=adult_latest, x="Strata Name", y="Percent", hue="Strata", dodge=False)
        plt.title(f"Adult Depression Rates by Group ({latest_year})")
        plt.xticks(rotation=45, ha="right")
        plt.ylabel("Percent")
        plt.tight_layout()
        plt.savefig("data/visualizations/depression_by_group_adult.png")
        plt.close()

        # --- students dataset visualizations ---
        plt.figure(figsize=(8,5))
        sns.histplot(students_df["Depression_Score"], bins=10, kde=True, color="green")
        plt.title("Distribution of Student Depression Scores")
        plt.xlabel("Depression Score")
        plt.ylabel("Count")
        plt.savefig("data/visualizations/depression_score_students.png")
        plt.close()

        plt.figure(figsize=(8,5))
        sns.countplot(x="Gender", data=students_df, palette="Set2")
        plt.title("Student Gender Distribution")
        plt.xlabel("Gender")
        plt.ylabel("Count")
        plt.savefig("data/visualizations/student_gender_distribution.png")
        plt.close()

        logger.info("Visualizations for both datasets saved successfully")

    except Exception as e:
        logger.error(f"Error during visualization: {e}")

    logger.info("Pipeline finished successfully")


if __name__ == "__main__":
    main()


