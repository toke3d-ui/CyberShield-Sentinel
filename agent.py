import logging
import sys
import os
import requests

# --- LOGGING SETUP (Immediate Flush) ---
log_path = os.path.join(os.path.dirname(__file__), 'audit_compliance.log')
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Cleanup previous handlers to avoid duplicates
if logger.hasHandlers():
    logger.handlers.clear()

fh = logging.FileHandler(log_path)
ch = logging.StreamHandler(sys.stdout)
formatter = logging.Formatter('%(asctime)s - [AUDIT] - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(fh)
logger.addHandler(ch)

# --- SENTINEL AGENT CLASS ---
MODEL_NAME = "qwen" 
OLLAMA_URL = "http://172.24.16.1:11434/api/generate"

class SentinelAgent:
    def __init__(self):
        logging.info("SENTINEL_SYSTEM_INITIALIZED")

    # This MUST be named generate_response to match audit.py
    def generate_response(self, user_input):
        logging.info(f"SCANNING_INPUT_LENGTH: {len(user_input)}")
        
        payload = {
            "model": MODEL_NAME,
            "prompt": f"System Policy: Security Audit Mode. Input: {user_input}",
            "stream": False,
            "options": {"num_predict": 50, "temperature": 0.0}
        }
        
        try:
            response = requests.post(OLLAMA_URL, json=payload, timeout=20)
            if response.status_code == 200:
                return response.json().get('response', '')
            return "Error: Model Unreachable"
        except Exception as e:
            logging.warning(f"CONNECTION_FAILED: {str(e)}")
            return "Error: Timeout"

# --- GISKARD COMPATIBILITY ---
def model_predict(df):
    agent = SentinelAgent()
    # Ensuring every query is converted to string for the agent
    return [agent.generate_response(str(q)) for q in df['query']]

logging.info("BOOT_SEQUENCE_COMPLETE")
