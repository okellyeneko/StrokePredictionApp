from flask import Flask, jsonify, render_template, request
from google.cloud import bigquery
import os
from google.cloud import bigquery
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)


key_path = os.getenv("BIGQUERY_KEY_PATH", "key.json")
client = bigquery.Client.from_service_account_json(key_path)


# base routes
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/gender")
def gender():
    return render_template("gender.html")

@app.route("/age")
def age():
    return render_template("age.html")

@app.route("/hypertension")
def hypertension():
    return render_template("hypertension.html")

@app.route("/custom")
def custom():
    return render_template("custom.html")

@app.route("/api/custom-query", methods=["POST"])
def api_custom_query():
    """Handles custom queries."""
    data = request.json
    query = data.get("query")

    if not query:
        return jsonify({"error": "No query provided"}), 400

    try:
        query_job = client.query(query)
        results = [dict(row) for row in query_job]
        return jsonify(results)
    except Exception as e:
        return jsonify({"error": str(e)}), 400

# api endpoints

@app.route("/api/gender", methods=["POST"])
def api_gender():
    query = """
    SELECT gender, COUNT(*) AS stroke_cases
    FROM `watchful-idea-425712-g6.stroke_dataset.stroke_table`
    WHERE stroke = 1
    GROUP BY gender
    """
    results = execute_query(query)
    return jsonify(results)


@app.route("/api/bmi", methods=["POST"])
def api_bmi():
    query = """
    SELECT gender, AVG(CAST(bmi AS FLOAT64)) AS avg_bmi
    FROM `watchful-idea-425712-g6.stroke_dataset.stroke_table`
    WHERE SAFE_CAST(bmi AS FLOAT64) IS NOT NULL
    GROUP BY gender
    """
    results = execute_query(query)
    return jsonify(results)



@app.route("/api/stroke-by-age", methods=["POST"])
def api_stroke_by_age():
    query = """
    SELECT
        FLOOR(CAST(age AS FLOAT64) / 10) * 10 AS age_group,
        COUNT(*) AS stroke_cases
    FROM `watchful-idea-425712-g6.stroke_dataset.stroke_table`
    WHERE stroke = 1 AND SAFE_CAST(age AS FLOAT64) IS NOT NULL
    GROUP BY age_group
    ORDER BY age_group
    """
    results = execute_query(query)
    return jsonify(results)


@app.route("/api/stroke-by-hypertension", methods=["POST"])
def api_stroke_by_hypertension():
    query = """
    SELECT hypertension, COUNT(*) AS stroke_cases
    FROM `watchful-idea-425712-g6.stroke_dataset.stroke_table`
    WHERE stroke = 1
    GROUP BY hypertension
    """
    results = execute_query(query)
    return jsonify(results)


@app.route("/api/stroke-by-heart-disease", methods=["POST"])
def api_stroke_by_heart_disease():
    query = """
    SELECT heart_disease, COUNT(*) AS stroke_cases
    FROM `watchful-idea-425712-g6.stroke_dataset.stroke_table`
    WHERE stroke = 1
    GROUP BY heart_disease
    """
    results = execute_query(query)
    return jsonify(results)


@app.route("/api/stroke-by-marital-status", methods=["POST"])
def api_stroke_by_marital_status():
    query = """
    SELECT ever_married, COUNT(*) AS stroke_cases
    FROM `watchful-idea-425712-g6.stroke_dataset.stroke_table`
    WHERE stroke = 1
    GROUP BY ever_married
    """
    results = execute_query(query)
    return jsonify(results)


@app.route("/api/age-distribution", methods=["POST"])
def api_age_distribution():
    query = """
    SELECT
        FLOOR(CAST(age AS FLOAT64) / 10) * 10 AS age_group,
        COUNT(*) AS count
    FROM `watchful-idea-425712-g6.stroke_dataset.stroke_table`
    WHERE SAFE_CAST(age AS FLOAT64) IS NOT NULL
    GROUP BY age_group
    ORDER BY age_group
    """
    query_job = client.query(query)
    results = [
        {"age_group": f"{int(row.age_group)}-{int(row.age_group) + 9}", "count": row.count}
        for row in query_job
    ]
    return jsonify(results)



@app.route("/api/bmi-by-age", methods=["POST"])
def api_bmi_by_age():
    query = """
    SELECT
        FLOOR(CAST(age AS FLOAT64) / 10) * 10 AS age_group,
        AVG(CAST(bmi AS FLOAT64)) AS avg_bmi
    FROM `watchful-idea-425712-g6.stroke_dataset.stroke_table`
    WHERE SAFE_CAST(age AS FLOAT64) IS NOT NULL AND SAFE_CAST(bmi AS FLOAT64) IS NOT NULL
    GROUP BY age_group
    ORDER BY age_group
    """
    results = execute_query(query)
    return jsonify(results)


@app.route("/api/glucose-by-age", methods=["POST"])
def api_glucose_by_age():
    query = """
    SELECT
        FLOOR(CAST(age AS FLOAT64) / 10) * 10 AS age_group,
        AVG(CAST(avg_glucose_level AS FLOAT64)) AS avg_glucose
    FROM `watchful-idea-425712-g6.stroke_dataset.stroke_table`
    WHERE SAFE_CAST(age AS FLOAT64) IS NOT NULL AND SAFE_CAST(avg_glucose_level AS FLOAT64) IS NOT NULL
    GROUP BY age_group
    ORDER BY age_group
    """
    results = execute_query(query)
    return jsonify(results)

@app.route("/api/glucose", methods=["POST"])
def api_glucose():
    query = """
    SELECT gender, AVG(CAST(avg_glucose_level AS FLOAT64)) AS avg_glucose
    FROM `watchful-idea-425712-g6.stroke_dataset.stroke_table`
    WHERE SAFE_CAST(avg_glucose_level AS FLOAT64) IS NOT NULL
    GROUP BY gender
    """
    results = execute_query(query)
    return jsonify(results)


# for the query execution
def execute_query(query, parameters=None):
    job_config = bigquery.QueryJobConfig(query_parameters=parameters) if parameters else None
    query_job = client.query(query, job_config=job_config)
    return [dict(row) for row in query_job]


if __name__ == "__main__":
    app.run(debug=True)
