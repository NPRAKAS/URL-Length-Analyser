from flask import Flask, request, render_template
from urllib.parse import urlparse
import pandas as pd
import matplotlib.pyplot as plt
import os
import io
import base64

app = Flask(__name__)

# Threshold value to classify a URL as suspicious based on its length
THRESHOLD = 75
# List of suspicious keywords
SUSPICIOUS_KEYWORDS = ["login", "secure", "verify", "account", "free", "update", "payment", "bank", "auth"]

# Function to analyze a single URL
def analyze_url(url):
    parsed = urlparse(url)
    url_length = len(url)
    contains_suspicious_keywords = any(keyword in url.lower() for keyword in SUSPICIOUS_KEYWORDS)
    classification = "Suspicious" if url_length > THRESHOLD or contains_suspicious_keywords else "Legitimate"
    return {
        "URL": url,
        "Scheme": parsed.scheme,
        "Domain": parsed.netloc,
        "Path": parsed.path,
        "Query Params": parsed.query,
        "Fragment": parsed.fragment,
        "Total Length": url_length,
        "Contains Suspicious Keywords": "Yes" if contains_suspicious_keywords else "No",
        "Classification": classification,
    }

# Function to analyze multiple URLs
def analyze_urls(urls):
    results = [analyze_url(url.strip()) for url in urls if url.strip()]
    return pd.DataFrame(results)

# Function to generate a pie chart
def generate_pie_chart(df):
    classification_counts = df["Classification"].value_counts()
    plt.figure(figsize=(6, 6))
    plt.pie(
        classification_counts,
        labels=classification_counts.index,
        autopct="%1.1f%%",
        startangle=90,
        colors=["skyblue", "lightcoral"],
    )
    plt.title("Legitimacy vs Suspiciousness of URLs")
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    chart_data = base64.b64encode(buf.getvalue()).decode()
    buf.close()
    return chart_data

@app.route("/", methods=["GET", "POST"])
def index():
    results_table = None
    pie_chart = None

    if request.method == "POST":
        # Handle URLs input from the text field
        urls_input = request.form.get("urls_input", "").strip()
        urls = urls_input.split(",") if urls_input else []

        # Handle file upload
        file = request.files.get("file_input")
        if file and file.filename.endswith(".csv"):
            df_file = pd.read_csv(file)
            if "URL" not in df_file.columns:
                return render_template("index.html", error="CSV file must contain a 'URL' column.")
            urls.extend(df_file["URL"].tolist())

        # Perform analysis if there are URLs
        if urls:
            df_results = analyze_urls(urls)
            results_table = df_results.to_html(classes="table table-striped", index=False)
            pie_chart = generate_pie_chart(df_results)

    return render_template("index.html", results_table=results_table, pie_chart=pie_chart)

if __name__ == "__main__":
    app.run(debug=True)
