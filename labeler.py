def apply_label_and_move_from_inbox(service, msg_id, label_name, inbox_label_id):
    """
    Applies a given label to an email and removes it from the inbox.
    Creates the label if it doesn't exist.

    Args:
        service (googleapiclient.discovery.Resource): The authenticated Gmail service object.
        msg_id (str): The ID of the email message to label.
        label_name (str): The name of the label to apply.
        inbox_label_id (str): The ID of the 'INBOX' label to remove.
    """
    # First, check if the label already exists.
    labels = service.users().labels().list(userId='me').execute()
    label_id = next((label['id'] for label in labels['labels'] if label['name'] == label_name), None)

    if not label_id:
        # If the label does not exist, create it.
        label = service.users().labels().create(userId='me', body={
            'name': label_name,
            'labelListVisibility': 'labelShow',
            'messageListVisibility': 'show'
        }).execute()
        label_id = label['id']

    # Apply the new label AND remove the 'INBOX' label.
    # This is how an email is moved out of the primary inbox in Gmail.
    service.users().messages().modify(
        userId='me',
        id=msg_id,
        body={
            'addLabelIds': [label_id],
            'removeLabelIds': [inbox_label_id]
        }
    ).execute()
