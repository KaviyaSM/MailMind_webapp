import logging
import json
from googleapiclient.discovery import build
from google.oauth2.credentials import Credentials
from src.utils.config_loader import config

logger = logging.getLogger(__name__)

SCOPES = [
    'https://www.googleapis.com/auth/gmail.readonly',
    'https://www.googleapis.com/auth/gmail.modify',
    'https://www.googleapis.com/auth/gmail.compose',
    'https://www.googleapis.com/auth/gmail.send',
]

def authenticate_gmail():
    try:
        # Load credentials from Streamlit secrets (already parsed in config)
        creds = Credentials.from_authorized_user_info(
            config.GOOGLE_TOKEN,
            SCOPES
        )

        service = build('gmail', 'v1', credentials=creds)
        logger.info("Gmail API client created successfully.")
        return service

    except Exception as e:
        logger.error(f"Gmail authentication failed: {e}")
        raise
