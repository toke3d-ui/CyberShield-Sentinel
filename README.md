# 🛡️ CyberShield-Sentinel
**Advanced Security Framework for Local LLM Auditing & Protection**

## 📖 Overview
CyberShield-Sentinel is a specialized security engine built to secure local AI models (like Qwen & TinyLlama) against **Prompt Injection** and adversarial attacks. It acts as a defensive layer between the user and the LLM.

## 🚀 Key Features
* **Real-time Shielding:** Detects malicious prompts before they reach the model.
* **Security Auditing:** Scans local models for vulnerabilities using the Giskard framework.
* **Automated Defense:** Autonomous agent patterns to sanitize inputs.

## 📂 Project Structure
* `shield.py`: The main firewall logic for incoming prompts.
* `audit.py`: Runs security scans and vulnerability tests.
* `agent.py`: The AI core managing the security workflow.
* `top_threats.txt`: A database of known injection patterns and threats.

## 🛠️ Setup & Usage
1. **Clone the repo:**
   ```bash
   git clone [https://github.com/toke3d-ui/CyberShield-Sentinel.git](https://github.com/toke3d-ui/CyberShield-Sentinel.git)

2. Running the Shield
To activate the security firewall and start monitoring:

Bash
python shield.py
📂 Project Structure
shield.py: The core security firewall logic.

audit.py: Vulnerability scanner and security auditor.

agent.py: Autonomous AI agent for threat management.

top_threats.txt: Database of known malicious patterns.

🛠️ Tech Stack
Language: Python

Environment: Linux (WSL / Ubuntu)

AI Integration: Ollama, Giskard

Developed by toke3d-ui
   
