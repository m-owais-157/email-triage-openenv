 # 📧 Smart Email Triage Environment (OpenEnv) 

# # 🚀 Overview
This project implements a **reinforcement learning environment** for email classification using the OpenEnv standard.

An agent interacts with the environment to classify emails into:
- 📌 Important
- 📧 Normal
- 🚫 Spam

The goal is to **maximize reward** through correct classification.

---

# # 🌐 Live Deployment
- 🔗 Hugging Face Space:  
  https://m-owais-7-email-triage-env-v1.hf.space

---

# # 🧠 Environment Design

# # # 🔁 Endpoints

| Endpoint | Description |
|--------|------------|
| `/reset` | Initialize environment with emails |
| `/step` | Perform classification action |
| `/state` | Get current state |
| `/health` | Check environment health |
| `/metadata` | Environment info |
| `/schema` | Action/State definitions |
| `/mcp` | JSON-RPC compatibility |

---

# # 🎯 Task

Classify each email into:
- `"important"`
- `"normal"`
- `"spam"`

---

 # # 🧾 Example Email

```json
{
  "id": 2,
  "text": "Congrats! You won ₹10 lakh lottery. Click link now!"
}A rule-based agent is implemented in `inference.py` to interact with the environment.

## 🏁 Goal
Maximize total reward across all steps.
