import json
import argparse
from googleapiclient.discovery import build
import google.oauth2.credentials
from email.mime.text import MIMEText
import base64


parser = argparse.ArgumentParser()
parser.add_argument('message')
parser.add_argument('sender')
args = parser.parse_args()

token = "<access_token_here>"
client_id = ""
client_secret = ""

def sendMessage(message):
    credentials = google.oauth2.credentials.Credentials(token, client_id=client_id, client_secret=client_secret)
    service = build('gmail','v1', credentials=credentials)
    if service:
        print('Successfully connected to Gmail')
        print(service)
    
    response = (service.users().messages().send(userId=args.sender, body=message)).execute()
    print(f"Message sent with ID: {response['id']}")

    
def create_message(message_text):
    message = MIMEText(message_text)
    message['to'] = '<sender>'
    message['from'] = '<receiver>'
    message['subject'] = 'Test email'
    encoded_message = base64.urlsafe_b64encode(message.as_bytes())
    return { 'raw': encoded_message.decode()}

if __name__ == "__main__":
    message = create_message(args.message)
    sendMessage(message=message)