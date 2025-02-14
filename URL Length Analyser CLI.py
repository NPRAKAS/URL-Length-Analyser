# Import required libraries
from urllib.parse import urlparse  # To parse URLs into components like scheme, domain, and path
import matplotlib.pyplot as plt  # For creating visualizations like pie charts
import pandas as pd  # For handling tabular data

# Threshold value to classify a URL as suspicious based on its length
THRESHOLD = 75

# List of suspicious keywords
SUSPICIOUS_KEYWORDS = ["login", "secure", "verify", "account", "free", "update", "payment", "bank", "auth"]

# Function to analyze a single URL
def analyze_url(url):

    parsed = urlparse(url)  # Parse the URL into components
    url_length = len(url)  # Calculate the total length of the URL
    
    # Check for suspicious keywords
    contains_suspicious_keywords = any(keyword in url.lower() for keyword in SUSPICIOUS_KEYWORDS)

    # Classification logic
    classification = "Suspicious" if url_length > THRESHOLD or contains_suspicious_keywords else "Legitimate"
    
    # Create a dictionary with extracted components and classification
    components = {
        "URL": url,
        "Scheme": parsed.scheme,  # Extract the scheme (e.g., http, https)
        "Domain": parsed.netloc,  # Extract the domain (e.g., example.com)
        "Path": parsed.path,  # Extract the path (e.g., /home/index)
        "Query Params": parsed.query,  # Extract query parameters (e.g., ?id=123)
        "Fragment": parsed.fragment,  # Extract the fragment (e.g., #section1)
        "Total Length": url_length,  # Add the total length of the URL
        "Contains Suspicious Keywords": "Yes" if contains_suspicious_keywords else "No",  # Check for suspicious keywords
        "Classification": classification  # Final classification
    }
    return components  # Return the analyzed data

# Function to analyze input URLs
def analyze_input(input_data):
    results = []  # List to store results for each URL
    
    # Split the input data by commas to handle multiple URLs
    urls = input_data.split(",")  

    # Process each URL
    for url in urls:
        url = url.strip()  # Remove leading/trailing whitespaces
        if url:  # Check if the URL is not empty
            results.append(analyze_url(url))  # Analyze the URL and add results to the list

    # Convert results to a pandas DataFrame
    df_results = pd.DataFrame(results)
    return df_results  # Return the DataFrame with results

# Function to generate a pie chart based on classification results
def generate_pie_chart(df):

    # Count the number of legitimate and suspicious URLs
    classification_counts = df["Classification"].value_counts()
    
    # Create a pie chart
    plt.figure(figsize=(6, 6))  # Set figure size
    plt.pie(
        classification_counts,  # Values to plot
        labels=classification_counts.index,  # Labels for the pie segments
        autopct='%1.1f%%',  # Show percentage on each segment
        startangle=90,  # Start the pie chart at 90 degrees
        colors=["skyblue", "lightcoral"]  # Set colors for the segments
    )
    plt.title("Legitimacy vs Suspiciousness of URLs")  # Add title to the chart
    plt.show()  # Display the pie chart

# Main function to handle user input and orchestrate the analysis process
if __name__ == "__main__":
    print("Welcome to URL Length Analyzer")  # Display a welcome message
    input_data = input("Enter multiple URLs separated by commas: ").strip()
    
    # Perform analysis on the provided input
    df_results = analyze_input(input_data)
    if df_results is not None:  # Check if analysis was successful
        print("\nAnalysis Results:")  # Display results
        print(df_results)

        # Generate a pie chart based on the analysis
        generate_pie_chart(df_results)
