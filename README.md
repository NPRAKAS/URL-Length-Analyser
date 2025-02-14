# URL Length Analyzer

## Overview
The **URL Length Analyzer** is a Python-based tool that analyzes URLs to determine their legitimacy. It classifies URLs as either "Legitimate" or "Suspicious" based on their length and the presence of specific suspicious keywords.

## Features
- Accepts multiple URLs as input (comma-separated)
- Parses URLs to extract components like scheme, domain, path, and query parameters
- Checks for suspicious keywords such as "login," "secure," "verify," "payment," etc.
- Classifies URLs as **Legitimate** or **Suspicious** based on length and keywords
- Generates a **pie chart visualization** of the results

## Technologies Used
- Python
- Pandas (for handling tabular data)
- Matplotlib (for data visualization)
- Flask (for web-based UI)

## Installation
### Prerequisites
Ensure you have Python installed on your system. You can install the required dependencies using:
```sh
pip install pandas matplotlib flask
```

## Usage
1. Clone the repository:
```sh
git clone https://github.com/your-username/URL-Length-Analyser.git
cd URL-Length-Analyser
```

2. Run the script:
```sh
python app.py
```

3. Enter URLs manually (comma-separated) or upload a CSV file with URLs.

4. View the results on the web interface with classifications and a pie chart visualization.

## Example Input
```
https://example.com, https://secure-login.com, https://free-gifts.com
```

## Example Output
| URL | Classification |
|------|---------------|
| https://example.com | Legitimate |
| https://secure-login.com | Suspicious |
| https://free-gifts.com | Suspicious |

## Future Enhancements
- Add real-time URL scanning via third-party APIs
- Enhance keyword detection using AI-based techniques
- Improve UI with additional visual elements

## Contributions
Contributions are welcome! Feel free to submit issues and pull requests.

## License
This project is licensed under the MIT License.
