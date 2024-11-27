
# Healthcare Data Warehouse and Analytics Dashboard

## Project Overview

This project analyzes stroke-related healthcare data using a cloud-based data warehouse. It provides insights with a dashboard and a custom query feature. 
The project is powered by Google BigQuery for data warehouse and Flask for dashboard developement.

---

## Features

1. **Cloud Data Warehouse**: Google BigQuery for scalable data storage and querying.
2. **Dashboards**: Developed with Flask to provide stroke case prediction analytics with BMI, and glucose trends based on gender, age, and hypertension.
3. **Custom Query**: Allows the user to execute SQL queries directly for advanced analysis.

---

## Dataset

- **Source**: Publicly available dataset from Kaggle: (https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset?resource=download)
- **Details**: 12 features including gender, age, BMI, hypertension, heart disease, glucose levels, and stroke case prediction.

---

## Setup Instructions

1. Install Python 3.8+
2. Create a Google Cloud account
3. Create a project in Google Cloud Console.
4. Enable BigQuery API.
5. Add the medical dataset and create a table. 
6. Create a service account key (`key.json`).
7. Share the BigQuery dataset with the service account email.

### Steps

1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Place `key.json` in the project root directory.
4. Run the app:
   ```bash
   python app.py
   ```
5. Access the app on localhost on [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

## Alternative Dashboard

For a pre-built dashboard, connect BigQuery to a Looker Studio Dashboard. 
Here is one I setup for example:(https://lookerstudio.google.com/reporting/d58432a7-e04e-4eb5-a37f-ca45901be4a0).

---

## Contact

- **Name**: Eneko O'Kelly  
- **Email**: eneko.okelly@ucdconnect.ie
