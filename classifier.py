import ollama
import json

def classify_email(subject, body, model='mistral'):
    """
    Classifies an email and returns the category and a confidence score.

    The prompt is designed to ask the LLM to return a JSON object with
    a 'category' and a 'confidence' key. This structured output is more
    reliable for automated processing.

    Args:
        subject (str): The subject line of the email.
        body (str): The snippet or body of the email.
        model (str): The name of the ollama model to use.

    Returns:
        tuple: A tuple containing (category, confidence_score).
               Returns ("Unknown", 0.0) if classification fails.
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
        # The ollama.chat function is used to interact with the model.
        # It's expected to return a JSON string based on our prompt.
        response = ollama.chat(model=model, messages=[{"role": "user", "content": prompt}])
        json_string = response['message']['content'].strip()
        
        # Parse the JSON response from the model.
        classification_result = json.loads(json_string)
        
        category = classification_result.get('category', 'Unknown')
        confidence = float(classification_result.get('confidence', 0.0))
        
        # Ensure confidence is within a valid range.
        if not 0.0 <= confidence <= 1.0:
            confidence = 0.0

        return category, confidence

    except (json.JSONDecodeError, KeyError, ValueError) as e:
        print(f"Error classifying email: {e}")
        # Return a default value in case of an error to prevent the script from crashing.
        return "Unknown", 0.0
