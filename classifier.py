import os
import json
import ollama

# Set the base URL for the Ollama client to the correct service
ollama_host = os.getenv("OLLAMA_HOST", "http://localhost:11434")
ollama.base_url = ollama_host

def classify_email(subject, body, model='mistral'):
    """
    Classifies an email and returns the category and a confidence score.
    """
    prompt = f"""
You are an email sorting assistant. Categorize the email below into one of these categories:
['Work', 'Personal', 'Spam', 'Promotions', 'Urgent', 'Social']

Provide your response as a JSON object with two keys:
- 'category': The category you have chosen.
- 'confidence': A floating-point number between 0.0 and 1.0 representing your confidence in the classification.

Subject: {subject}
Body: {body}
"""
    try:
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
        json_string = response['message']['content'].strip()
        
        classification_result = json.loads(json_string)
        
        category = classification_result.get('category', 'Unknown')
        confidence = float(classification_result.get('confidence', 0.0))
        
        if not 0.0 <= confidence <= 1.0:
            confidence = 0.0

        return category, confidence

    except (json.JSONDecodeError, KeyError, ValueError) as e:
        print(f"Error classifying email: {e}")
        return "Unknown", 0.0
