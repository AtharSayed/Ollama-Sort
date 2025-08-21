# Automated Gmail Sorter

## 📧 Project Overview

This Python project is an automated email sorter that connects to your Gmail account, fetches recent emails, and uses a local large language model (LLM) via `ollama` to classify them. Based on the classification, it automatically applies a corresponding label to the email and moves it out of your primary inbox.

The system is designed to be robust, using a **confidence score** from the LLM to identify emails that may be misclassified. If the model's confidence in a classification is below a set threshold or it returns an unexpected category, the email is labeled `Needs-Review` so you can handle it manually.

## 🚀 Features

* **Email Classification**: Categorizes emails into predefined categories such as `Work`, `Personal`, `Spam`, `Promotions`, `Urgent`, or `Social`.
* **Confidence-Based Review**: Uses a confidence score to flag emails that need manual review, preventing misclassification.
* **Automatic Labeling**: Creates and applies Gmail labels for each category.
* **Inbox Management**: Archives classified emails by removing the `INBOX` label, keeping your primary inbox clean.
* **Local LLM Integration**: Uses `ollama` and a local model (like `mistral`) for privacy-preserving classification.
* **Docker Support**: Containerized deployment using Docker and Docker Compose for seamless environment setup.

---

## 🛠️ Prerequisites

Before you begin, ensure you have the following installed:

* **Python 3.x** (if running locally)
* **Ollama**: Follow the installation instructions on the [Ollama website](https://ollama.ai/)
* **Git**: For cloning the repository
* **A Google Cloud Project**: You'll need to create one to get your `credentials.json` file
* **Docker & Docker Compose** (optional, for containerized usage)

---

## ⚙️ Setup and Installation

### 1. Clone the repository

```bash
git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
cd your-repo-name
````

### 2\. Install Python dependencies (if running locally)

```bash
pip install -r requirements.txt
```

### 3\. Set up Google API credentials

Follow the Gmail API Quickstart Guide to create a Google Cloud Project and enable the Gmail API.
Download the **credentials.json** file from your Google Cloud Project.
Place the `credentials.json` file in the root directory of this project.

### 4\. Run Ollama

Make sure your `ollama` server is running and that you have a model downloaded. The project defaults to using the `mistral` model, so you can pull it by running:

```bash
ollama run mistral
```

This command will download the model and start a local server. Keep this terminal window open while the script runs.

-----

### 🐳 Optional: Running with Docker and Docker Compose

You can run this project inside Docker containers to avoid local setup hassles and ensure consistent environments.

**Prerequisites for Docker usage**

  * Install Docker
  * Install Docker Compose

**Steps to run with Docker Compose**

1.  Ensure your **credentials.json** file is placed in the project root directory.
2.  Run the following command to build and start both your app container and the Ollama model container:

<!-- end list -->

```bash
docker-compose up --build
```

Docker Compose will:

  * Start the Ollama container with the LLM model server.
  * Build and start your app container.
  * Connect your app to Ollama internally via Docker networking.

On the first run, follow the logs for Gmail OAuth authorization. After authorizing, the token will be saved inside the container.

**Notes on Docker setup**

  * The app container connects to Ollama via hostname `ollama` on port `11434`.
  * The `OLLAMA_HOST` environment variable is set inside the container for this connection.
  * Ollama model data is persisted with Docker volumes to avoid repeated downloads.
  * This setup enables seamless sharing of the Docker image without requiring Python or Ollama locally.

-----

## ▶️ Usage (Local or Docker)

To run locally (without Docker):

```bash
python main.py
```

Or, to run with Docker Compose:

```bash
docker-compose up
```

The script will:

  * Fetch the 10 most recent emails from your inbox.
  * Classify each email using the LLM.
  * Print classification results including confidence scores.
  * Apply the appropriate label and move emails out of the inbox.

You can adjust the `max_results` variable in `main.py` to change how many emails are processed per run.

-----

## 🎨 Project Structure

  * `main.py`: The main script that orchestrates the entire process. It authenticates with Gmail, fetches emails, calls the classifier, and applies labels.
  * `gmail_api.py`: Contains functions for authenticating with the Gmail API and fetching emails.
  * `classifier.py`: Connects to the `ollama` service to classify emails and returns the category and a confidence score. This file also contains the `VALID_CATEGORIES` list.
  * `labeler.py`: Contains a function to apply a label to an email and remove it from the inbox. It will create a new label if it doesn't already exist.
  * `requirements.txt`: Lists the necessary Python libraries.
  * `Dockerfile`: Defines how to build the app Docker image.
  * `docker-compose.yml`: Sets up a multi-container environment (app + Ollama).
  * `.dockerignore`: Files excluded during Docker build.
  * `credentials.json`: Your private API credentials from Google Cloud.
  * `token.json`: Automatically generated file storing your OAuth 2.0 token after the first successful authentication.

-----

## 📮 Feedback or Contributions?

Feel free to open issues or submit pull requests to improve this project\!

```
```
