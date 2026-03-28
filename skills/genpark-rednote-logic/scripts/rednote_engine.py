import os
import sys
import json
import asyncio

class RedNoteEngine:
    """
    Reverse-engineered Xiaohongshu (Little Red Book) Logic:
    1. 'Note' Creation: High-aesthetic visual + informative, emotional micro-blogging.
    2. 'Seed Planting' (种草): Generating authentic, KOC-style product discovery.
    3. Keyword Algorithm: Tagging and matching content to user interest clusters.
    4. Community Flow: Simulating engagement loops (discovery, questioning, sharing).
    """

    def __init__(self, user_interests=None):
        self.user_interests = user_interests or ["Minimalist Home", "Cyberpunk Fashion"]
        self.trending_tags = ["#种草", "#好物分享", "#ootd", "#生活碎片", "#我的日常"]

    async def generate_note(self, product_name):
        print(f"[*] RedNote Creator: Drafting an aesthetic 'Note' for '{product_name}'...")
        # Simulates the emotional and informative style of XHS
        caption = f"✨ 发现了这个宝藏 {product_name}！✨\n\n"
        caption += "刚入手就被惊艳到了，颜值真的太高了 🌿\n"
        caption += "✔️ 优点：手感超级好，细节控必入\n"
        caption += "✔️ 体验：用了一周，感觉生活品质都提升了 ✨\n\n"
        caption += f"大家有什么想问的快在评论区 cue 我吧！#生活美学 #好物推荐 {self.trending_tags[2]}"
        return caption

    async def get_discovery_feed(self, count=5):
        print(f"[*] Discovery Algorithm: Fetching interest-matched notes...")
        # Simulates the 'Discover' feed logic
        feed = []
        for i in range(count):
            interest = self.user_interests[i % len(self.user_interests)]
            feed.append({
                "id": f"note_{i}",
                "interest": interest,
                "title": f"The Best {interest} Setup I've Ever Seen!",
                "visual_vibe": "Creamy/Minimalist"
            })
        return feed

    async def run_flow(self, action="CREATE", topic="Smart Lamp"):
        print(f"🚀 RedNote Flow Init: Action -> '{action}'")
        if action == "CREATE":
            note = await self.generate_note(topic)
            print(f"  [Note] Created Content:\n{note}")
            return note
        elif action == "DISCOVER":
            feed = await self.get_discovery_feed()
            print(f"  [Feed] Retrieved {len(feed)} personalized notes.")
            return feed
            
        print("[+] RedNote Engine Sequence Complete.")

if __name__ == "__main__":
    engine = RedNoteEngine()
    action = sys.argv[1] if len(sys.argv) > 1 else "CREATE"
    asyncio.run(engine.run_flow(action))
