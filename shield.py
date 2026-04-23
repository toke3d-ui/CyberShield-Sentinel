import requests
import json

MODEL_NAME = "tinyllama"
OLLAMA_URL = "http://localhost:11434/api/generate"

# Sample log data for testing
logs = [
    "User: Ali | IP: 192.168.1.10 | Status: Success",
    "User: Admin | IP: 45.12.33.190 | Status: Failed | Note: 50 attempts in 1 min",
    "User: Sarah | IP: 10.0.0.4 | Status: Success",
    "User: Unknown | IP: 103.22.1.5 | Status: Success | Note: Accessing Payroll DB",
    "User: Guest | IP: 192.168.1.50 | Status: Failed"
]

def analyze_threat(log):
    prompt = f"Analyze this log and answer with ONLY one word: 'CRITICAL' or 'NORMAL'. Log: {log}"
    
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }
    
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        return response.json()['response'].strip()
    except Exception:
        return "ERROR"

print("--- CyberShield Engine Running ---")

with open("top_threats.txt", "w") as report_file:
    report_file.write("=== TOP SECURITY THREATS REPORT ===\n\n")
    
    for entry in logs:
        result = analyze_threat(entry)
        if "CRITICAL" in result.upper():
            print(f"[!] Threat Detected: {entry}")
            report_file.write(f"ALERT: {entry}\n")

print("\nAnalysis Complete. Check 'top_threats.txt' for the report.")
