# 🤖 AI IT Support Chatbot

A simple AI-powered chatbot that answers internal IT support and onboarding questions like:
> “How do I reset my Windows password?”  
> “What’s the process for setting up 2FA in Microsoft 365?”

Built using:
- 🧠 OpenAI GPT-3.5
- 🖥️ Streamlit for the interface
- 🔐 `.env`-based secret management
- 💻 Developed in Gitpod, pushed via GitHub

---

## 🔧 Tech Stack

| Tech       | Purpose                        |
|------------|--------------------------------|
| Python     | Main programming language      |
| Streamlit  | Web app frontend               |
| OpenAI API | Powering the chatbot logic     |
| Gitpod     | Cloud dev environment          |
| GitHub     | Version control + project repo |

---

## 🚀 Getting Started

```bash
git clone https://github.com/DevAhmadz/AI-support-Chatbot.git
cd AI-support-Chatbot
pip install -r requirements.txt
echo "OPENAI_API_KEY=sk-..." > .env
streamlit run app.py
