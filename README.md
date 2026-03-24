# AI Support Copilot

A simple AI-powered automation project that integrates with Zammad to analyze support tickets in real time and add debugging notes automatically.

---

## 🚀 What it does

- Listens to new tickets using webhook  
- Sends ticket data to AI  
- Generates issue analysis  
- Adds a note back to the ticket  

---

## 🧱 Flow

Zammad → Webhook → Python (Flask) → AI → Zammad (update ticket)

---

## 🛠️ Tech Used

- Python (Flask)
- Zammad
- OpenAI API
- ngrok

---

## ⚙️ Setup

### 1. Clone repo

git clone https://github.com/3degreearcsine/ai-zammad-support-copilot.git<br>
cd ai-zammad-support-copilot

### 2. Create virtual environment
python -m venv venv<br>
venv\Scripts\activate

### 3. Install dependencies
pip install requests openai python-dotenv flask

### 4. Create .env
ZAMMAD_URL=http://localhost:8081/api/v1
ZAMMAD_API_TOKEN=your_token
OPENAI_API_KEY=your_key

### 5. Run server
python webhook_server.py

### 6. Start ngrok
ngrok http 5000

### 7. Configure webhook in Zammad
- Use ngrok HTTPS URL
- Endpoint: /webhook
- Method: POST
- Trigger: Ticket Created

---

## 🧪 Demo

agentic-automation-demo-compressed.mp4

---

## 📌 Sample Output
Issue Type: API Issue  
Priority: High  
Root Cause: Backend failure  
Debug Steps:
- Check logs  
- Verify deployment  

---

## 🔮 Future Improvements

Auto priority update
Tagging (API / DB / Auth issues)
Markdown-based workflow

---
