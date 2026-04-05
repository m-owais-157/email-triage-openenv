import requests

BASE_URL = "https://m-owais-7-email-triage-env-v1.hf.space"

def classify(text):
    text = text.lower()

    if any(word in text for word in ["urgent", "bank", "otp", "account", "deadline"]):
        return "important"
    elif any(word in text for word in ["lottery", "win", "free", "offer"]):
        return "spam"
    else:
        return "normal"

def run():
    state = requests.post(f"{BASE_URL}/reset").json()["state"]

    total_reward = 0

    for email in state["emails"]:
        action = {
            "email_id": email["id"],
            "label": classify(email["text"])
        }

        res = requests.post(f"{BASE_URL}/step", json=action).json()

        print({
            "action": action,
            "reward": res["reward"],
            "state": res["state"]
        })

        total_reward += res["reward"]

        if res["done"]:
            break

    print("TOTAL REWARD:", total_reward)

if __name__ == "__main__":
    run()
