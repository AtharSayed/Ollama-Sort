from gmail_api import authenticate_gmail, fetch_latest_emails
from classifier import classify_email
from labeler import apply_label

# Define a confidence threshold. Any classification with a score below this
# will be marked for manual review.
CONFIDENCE_THRESHOLD = 0.85

def run_email_sorter():
    """
    Main function to run the email sorting process.
    - Authenticates with Gmail.
    - Fetches the latest emails.
    - Classifies each email with a confidence score.
    - Applies a definitive label or a 'Needs-Review' label based on the confidence.
    """
    service = authenticate_gmail()
    print("Successfully authenticated with Gmail.")
    print("Fetching the latest 10 emails...")
    emails = fetch_latest_emails(service, max_results=10)
    print(f"Found {len(emails)} emails to process.\n")

    for email in emails:
        subject = email['subject']
        snippet = email['snippet']
        email_id = email['id']
        
        # Get both the category and confidence score from the classifier.
        category, confidence = classify_email(subject, snippet)
        
        # Check if the confidence score is above the defined threshold.
        if confidence >= CONFIDENCE_THRESHOLD:
            final_label = category
            print(f"Classifying: '{subject}'")
            print(f"→ Confident classification: {final_label} (Confidence: {confidence:.2f})")
        else:
            final_label = 'Needs-Review'
            print(f"Classifying: '{subject}'")
            print(f"→ Low confidence. Marking as '{final_label}' (Confidence: {confidence:.2f})")
            
        # Apply the chosen label to the email.
        apply_label(service, email_id, final_label)
        print("-" * 20)

if __name__ == "__main__":
    run_email_sorter()
