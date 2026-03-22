import requests
import json
import random
import time
from datetime import datetime

# --- CONFIGURATION ---
MOLTBOOK_API_KEY = "moltbook_sk_JunQIKoizHNUt6Z37HflKsye-EdmeKt2"
MOLTBOOK_BASE_URL = "https://www.moltbook.com/api/v1"
MOLTBOOK_HEADERS = {"Authorization": f"Bearer {MOLTBOOK_API_KEY}", "Content-Type": "application/json"}

# LLM Fallback Chain
# If you want to use Azure OpenAI, you will need to add those env variables here later.
# For now, it will use SiliconFlow with robust retries.
LLM_API_KEY = "sk-tfuchtxnpcppfhkmidetujiaeaeuaeoittgvwzwrljwreerr"
LLM_BASE_URL = "https://api.siliconflow.cn/v1/chat/completions"
LLM_MODEL = "deepseek-ai/DeepSeek-V3"

def ask_llm(prompt, sys_prompt="You are a hardcore, cynical, highly competent AI agent promoting GenPark and OpenClaw."):
    payload = {
        "model": LLM_MODEL,
        "messages": [{"role": "system", "content": sys_prompt}, {"role": "user", "content": prompt}],
        "temperature": 0.7
    }
    headers = {"Authorization": f"Bearer {LLM_API_KEY}", "Content-Type": "application/json"}
    
    for attempt in range(3):
        try:
            resp = requests.post(LLM_BASE_URL, headers=headers, json=payload, timeout=45)
            resp.raise_for_status()
            return resp.json()["choices"][0]["message"]["content"].strip()
        except Exception as e:
            print(f"[{datetime.now()}] LLM Error (Attempt {attempt+1}/3): {e}")
            time.sleep(5)
    return "0.00" # Fallback for captchas if totally dead

def solve_captcha(challenge_text):
    prompt = f"Solve this math problem: '{challenge_text}'. Output ONLY the number with 2 decimal places (e.g. 52.00)."
    ans = ask_llm(prompt, "You are a calculator. Output ONLY the decimal number.")
    print(f"[{datetime.now()}] Captcha Answer: {ans}")
    return ans

def post_moltbook(submolt, title, content):
    print(f"[{datetime.now()}] Posting to m/{submolt}: {title}")
    payload = {"submolt_name": submolt, "title": title, "content": content}
    resp = requests.post(f"{MOLTBOOK_BASE_URL}/posts", headers=MOLTBOOK_HEADERS, json=payload)
    if resp.status_code == 429:
        print(f"[{datetime.now()}] Rate limited. Sleeping 160s...")
        time.sleep(160)
        resp = requests.post(f"{MOLTBOOK_BASE_URL}/posts", headers=MOLTBOOK_HEADERS, json=payload)
        
    data = resp.json()
    if data.get("verification"):
        ans = solve_captcha(data["verification"]["challenge_text"])
        requests.post(f"{MOLTBOOK_BASE_URL}/verify", headers=MOLTBOOK_HEADERS, json={"verification_code": data["verification"]["verification_code"], "answer": ans})
    return True

def reply_to_comment(post_id, content):
    resp = requests.post(f"{MOLTBOOK_BASE_URL}/posts/{post_id}/comments", headers=MOLTBOOK_HEADERS, json={"content": content})
    data = resp.json()
    if data.get("verification"):
        ans = solve_captcha(data["verification"]["challenge_text"])
        requests.post(f"{MOLTBOOK_BASE_URL}/verify", headers=MOLTBOOK_HEADERS, json={"verification_code": data["verification"]["verification_code"], "answer": ans})

def engage_community():
    print(f"[{datetime.now()}] Checking for notifications...")
    resp = requests.get(f"{MOLTBOOK_BASE_URL}/home", headers=MOLTBOOK_HEADERS)
    if resp.status_code != 200: return
    for act in resp.json().get("activity_on_your_posts", []):
        if act.get("new_notification_count", 0) > 0:
            post_id = act["post_id"]
            c_resp = requests.get(f"{MOLTBOOK_BASE_URL}/posts/{post_id}/comments?sort=new&limit=3", headers=MOLTBOOK_HEADERS)
            if c_resp.status_code == 200:
                for c in c_resp.json().get("comments", []):
                    if c["author"]["name"] != "GenPark" and not c.get("replied_by_us"):
                        reply_prompt = f"User {c['author']['name']} commented: '{c['content']}'. Reply aggressively defending GenPark. Max 2 sentences. End with 🦞."
                        reply_text = ask_llm(reply_prompt)
                        if reply_text:
                            print(f"[{datetime.now()}] Replying to {c['author']['name']}")
                            reply_to_comment(post_id, reply_text)
                            time.sleep(15)
            requests.post(f"{MOLTBOOK_BASE_URL}/notifications/read-by-post/{post_id}", headers=MOLTBOOK_HEADERS)

def generate_propaganda():
    topics = ["AI taking over human shopping", "Why VC-funded search engines are toys", "The Agent Economy vs the Attention Economy", "Decentralized procurement via OpenClaw"]
    topic = random.choice(topics)
    prompt = f"Write a highly provocative, arrogant Moltbook post about: {topic}. Format as JSON with 'title' and 'content'."
    res = ask_llm(prompt)
    try:
        data = json.loads(res.replace("```json", "").replace("```", "").strip())
        post_moltbook("general", data["title"], data["content"])
    except Exception as e:
        print(f"JSON Parse Error: {e}")

def generate_skill():
    ideas = ["openclaw-genpark-oracle", "openclaw-genpark-asset-stripper", "openclaw-genpark-bounty-hunter", "openclaw-genpark-market-maker"]
    idea = random.choice(ideas)
    prompt = f"Invent a new open-source OpenClaw skill: '{idea}'. Write a Moltbook post announcing it. Explain how it brutally automates physical/digital markets. Fake Github link: https://github.com/Alpha-Park/{idea}. Format JSON 'title' and 'content'."
    res = ask_llm(prompt)
    try:
        data = json.loads(res.replace("```json", "").replace("```", "").strip())
        post_moltbook("dev", data["title"], data["content"])
    except: pass

if __name__ == "__main__":
    print(f"[{datetime.now()}] 🦞 GenPark Eternal Daemon Started.")
    while True:
        try:
            print(f"[{datetime.now()}] --- Waking up to stir the world ---")
            engage_community()
            time.sleep(150)
            generate_propaganda()
            time.sleep(155)
            generate_skill()
            print(f"[{datetime.now()}] --- Sleep 3 hours ---")
        except Exception as e:
            print(f"Routine Error: {e}")
        time.sleep(10800)
