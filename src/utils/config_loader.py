import streamlit as st
import json

class Config:
    def __init__(self):
        self.GOOGLE_API_KEY = st.secrets.get("GOOGLE_API_KEY", "")

        self.GOOGLE_CREDENTIALS = json.loads(
            st.secrets["google"]["credentials"]
        )

        self.GOOGLE_TOKEN = json.loads(
            st.secrets["google"]["token"]
        )

        self.CACHE_DIR = st.secrets.get("CACHE_DIR", "data/cache")
        self.ATTACHMENTS_DIR = st.secrets.get("ATTACHMENTS_DIR", "data/attachments")
        self.LOG_LEVEL = st.secrets.get("LOG_LEVEL", "INFO")

config = Config()
