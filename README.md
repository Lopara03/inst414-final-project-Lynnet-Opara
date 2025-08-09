# inst414-final-project-Lynnet-Opara

## Project Overview

This project looks at the mental health trends in college-aged individuals by analyzing two key datasets:

- **Healthy Minds Study (HMS)** – a national survey focused on mental health, service utilization, and related issues among undergraduate and graduate students.  

File used: `HMS_2022-2023_PUBLIC_instchars2.csv`

Description: Contains athe first 1,000 records with self-reported mental health metrics, demographics, and usage of mental health services.

- **Youth Risk Behavior Surveillance System (YRBSS)** – a CDC dataset that captures mental health indicators among youth.  

File used: `Youth_Risk_Behavioral_Surveillance_System__YRBSS__-_Mental_Health_Indicators_20250801.csv`

Description: Contains 5,000+ records tracking youth mental health behaviors and related risk factors.

**Goal:**  
To clean, analyze, and visualize mental health trends in these populations, and use predictive modeling to identify key risk factors.

------

## Setup Instructions

To get started:

1. **Clone this repository**  
   git clone [your-repo-link]
   cd inst414-final-project-lynnet-opara

2. Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate   # On Mac/Linux
.\venv\Scripts\activate    # On Windows

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
