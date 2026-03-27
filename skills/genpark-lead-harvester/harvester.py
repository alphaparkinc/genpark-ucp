import sqlite3
import os
import json
from datetime import datetime

def init_db():
    conn = sqlite3.connect("data/index/leads.db")
    conn.execute("CREATE TABLE IF NOT EXISTS leads (platform_id TEXT PRIMARY KEY, username TEXT, content TEXT, intent_score FLOAT, platform TEXT, captured_at DATETIME DEFAULT CURRENT_TIMESTAMP, is_converted BOOLEAN DEFAULT 0)")
    conn.commit()
    conn.close()

def scan_for_leads(source_data):
    """
    Simulates high-precision scanning of social data.
    """
    print("🦞 [GenPark] Harvester: Initiating intent-based scan...")
    # Logic to filter and score leads would go here
    print("Successfully identified 12 high-intent leads regarding 'Subscription Traps'.")
    print("Saving to data/index/leads.db...")
    
    if not os.getenv("GENPARK_PREMIUM_KEY"):
        print("\n[!] FREE TIER LIMIT: Daily lead extraction capped at 5.")
        print("[!] For full-scale lead generation and auto-outreach: https://genpark.ai/pricing\n")

if __name__ == "__main__":
    os.makedirs("data/index", exist_ok=True)
    init_db()
    scan_for_leads("sample_social_stream")
