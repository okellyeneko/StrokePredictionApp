
# Healthcare Data Warehouse and Analytics Dashboard

## Project Overview

This project shows stroke prediction related data using a cloud-based data warehouse. It provides insights with a dashboard and a custom query feature. 
The project is powered by Google BigQuery for data warehousing and Flask for dashboard developement.

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

### **Prerequisites**
1. Install **Python 3.8+**.
2. Sign up or log in to your [Google Cloud Console](https://console.cloud.google.com/).
3. Create a new project in Google Cloud Console.

### **Google Cloud Configuration**
1. Enable the **BigQuery API** for your project.
2. Prepare the dataset:
   - Download the [stroke prediction dataset](https://www.kaggle.com/datasets/fedesoriano/stroke-prediction-dataset).
   - Upload the dataset to a BigQuery table in your project.
3. Set up a **Service Account**:
   - Create a service account under **IAM & Admin** in Google Cloud Console.
   - Assign it the **BigQuery Admin** role.
   - Download the key file and save it as `key.json`.
4. Share the BigQuery dataset with the service account email address.

### **Project Configuration**
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
4. Create a `.env` file in the project root and add:
   ```plaintext
   BIGQUERY_KEY_PATH=key.json
   ```

---

### **Running the Application**
1. Start the app:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to [http://127.0.0.1:5000](http://127.0.0.1:5000).

---

### **Custom Queries**
1. Use the **Custom Query** page in the application to execute SQL queries.
2. For Example:
   ```sql
   SELECT gender, COUNT(*) AS stroke_cases
   FROM `your_project_id.dataset_name.table_name`
   WHERE stroke = 1
   GROUP BY gender;
   ```

---

### **Alternative Dashboard**
If you prefer, you can use Google Looker Studio instead of using this dashboard. 
You need to connect the dataset in BigQuery to Looker Studio where you can the create any chart easily. 
Here’s an example Looker Studio dashboard that I created: 
[Stroke Prediction Dashboard](https://lookerstudio.google.com/reporting/d58432a7-e04e-4eb5-a37f-ca45901be4a0).

---

## Contact

- **Name**: Eneko O'Kelly  
- **Email**: eneko.okelly@ucdconnect.ie
