import requests
import os
from dotenv import load_dotenv

load_dotenv()

ZAMMAD_URL = os.getenv("ZAMMAD_URL")
TOKEN = os.getenv("ZAMMAD_API_TOKEN")

headers = {
    "Authorization": f"Token token={TOKEN}",
    "Content-Type": "application/json"
}

def add_note(ticket_id, note):
    url = f"{ZAMMAD_URL}/ticket_articles"

    payload = {
        "ticket_id": ticket_id,
        "body": note,
        "type": "note",
        "internal": True
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code not in [200, 201]:
        print("Error adding note:", response.text)
