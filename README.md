# inst414-final-project-Lynnet-Opara

## Project Overview

This project looks at the mental health trends in college-aged individuals by analyzing two key datasets:

- **Adult Depression Indicators (LGHC)** – sourced from national health data on depression prevalence and related indicators.

File used: `adult-depression-lghc-indicator-24.csv`

Description: Contains approximately 160 records with demographic information, self-reported depression indicators, and access to care variables.

- **Students’ Mental Health Survey** – a dataset formed through survey data that reflects student demographics, lifestyle, and mental health factors.

File used: `students_mental_health_survey.csv`

Description: Contains over 1,500 records tracking youth mental health behaviors and related risk factors.

**Goal:**  
To clean, analyze, and visualize mental health trends in these populations, and use predictive modeling to identify key risk factors.

------

## Setup Instructions

To get started:

1. **Clone this repository**  
   git clone [your-repo-link]
   cd inst414-final-project-lynnet-opara

2. Create and activate a virtual environment  

```bash
python3 -m venv venv
source venv/bin/activate   # On Mac/Linux
.\venv\Scripts\activate    # On Windows
```
3. Install: "pip install -r requirements.txt" into terminal
pip install -r requirements.txt

# Running the Project
Run the project pipeline by executing:


Copy

Edit

python main.py


This will run the full data science pipeline including:

Extracting raw data files

Cleaning and transforming the data

Running analytical models

Generating visualizations

# Code Package Structure

Copy

Edit

inst414-final-project-Lynnet-Opara/

```
│
├── data/                     # Data files
│   ├── extracted/            # Raw data files
│   ├── processed/            # Cleaned and transformed data
│   ├── outputs/              # Output data and results
│   ├── reference-tables/     # Data dictionaries and lookup tables
│
├── etl/                      # Extract, Transform, Load scripts
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│
├── analysis/                 # Analytical models and evaluation scripts
│   ├── model.py
│   ├── evaluate.py
│
├── vis/                      # Visualization scripts
│   ├── visualizations.py
│
├── main.py                   # Entry point to run full pipeline
├── README.md                 # Project overview and instructions
├── requirements.txt          # Python dependencies
```
# Add Collaborators
mali24@umd.edu
gillikin@umd.edu
