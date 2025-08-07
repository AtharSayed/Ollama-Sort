# Automated Gmail Sorter

## 📧 Project Overview

This Python project is an automated email sorter that connects to your Gmail account, fetches recent emails, and uses a local large language model (LLM) via `ollama` to classify them. Based on the classification, it automatically applies a corresponding label to the email and moves it out of your primary inbox.

The system is designed to be robust, using a confidence score from the LLM to identify emails that may be misclassified. If the model's confidence in a classification is below a set threshold or it returns an unexpected category, the email is labeled `Needs-Review` so you can handle it manually.

## 🚀 Features

* **Email Classification**: Categorizes emails into predefined categories such as `Work`, `Personal`, `Spam`, `Promotions`, `Urgent`, or `Social`.
* **Confidence-Based Review**: Uses a confidence score to flag emails that need manual review, preventing misclassification.
* **Automatic Labeling**: Creates and applies Gmail labels for each category.
* **Inbox Management**: Archives classified emails by removing the `INBOX` label, keeping your primary inbox clean.
* **Local LLM Integration**: Uses `ollama` and a local model (like `mistral`) for privacy-preserving classification.

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.x**
* **Ollama**: Follow the installation instructions on the [Ollama website](https://ollama.ai/).
* **Git**: For cloning the repository.
* **A Google Cloud Project**: You'll need to create one to get your `credentials.json` file.

## ⚙️ Setup and Installation

### 1. Clone the repository

First, clone this project to your local machine:

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
```

### 2. Install Python dependencies

Install the required Python libraries using `pip`:

```bash
pip install -r requirements.txt
```

### 3. Set up Google API credentials

1.  Follow the [Gmail API Quickstart Guide](https://developers.google.com/gmail/api/quickstart/python) to create a Google Cloud Project and enable the Gmail API.
2.  Download the `credentials.json` file from your Google Cloud Project.
3.  Place the `credentials.json` file in the root directory of this project.

### 4. Run Ollama

Make sure your `ollama` server is running and that you have a model downloaded. The project defaults to using the `mistral` model, so you can pull it by running:

```bash
ollama run mistral
```

This command will download the model and start a local server. You can keep this terminal window open while the script runs.

## ▶️ Usage

To run the email sorter, execute the `main.py` file from your terminal:

```bash
python main.py
```

The first time you run the script, a web browser will open, prompting you to authorize the application. After you grant permission, a `token.json` file will be saved. This token allows the script to access your Gmail account without re-authentication for future runs.

The script will then:
1.  Fetch the 10 most recent emails from your inbox.
2.  Classify each email using the LLM.
3.  Print the classification results, including the confidence score.
4.  Apply the appropriate label to the email and move it out of the inbox.

You can adjust the `max_results` variable in `main.py` to process more or fewer emails per run.

## 🎨 Project Structure

* `main.py`: The main script that orchestrates the entire process. It authenticates with Gmail, fetches emails, calls the classifier, and applies labels.
* `gmail_api.py`: Contains functions for authenticating with the Gmail API and fetching emails.
* `classifier.py`: Connects to the `ollama` service to classify emails and returns the category and a confidence score. This file also contains the `VALID_CATEGORIES` list.
* `labeler.py`: Contains a function to apply a label to an email and remove it from the inbox. It will create a new label if it doesn't already exist.
* `requirements.txt`: Lists the necessary Python libraries.
* `credentials.json`: Your private API credentials from Google Cloud.
* `token.json`: Automatically generated file storing your OAuth 2.0 token after the first successful authentication.
