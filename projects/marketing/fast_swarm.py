import asyncio
from playwright.async_api import async_playwright
import json
import random
import sys

async def register_and_like(user_data, target_url="https://genpark.ai/home/circle"):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        # Use a realistic user agent
        context = await browser.new_context(
            user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36"
        )
        page = await context.new_page()
        
        try:
            # 1. Random delay at the start
            await asyncio.sleep(random.uniform(5, 15))
            
            print(f"[*] Registering {user_data['username']} ({user_data['email']})...", flush=True)
            await page.goto("https://genpark.ai/sign-up", wait_until="networkidle")
            
            # Fill form with human-like typing speed
            await page.type('input[name="firstName"]', user_data['first'], delay=random.randint(50, 150))
            await page.type('input[name="lastName"]', user_data['last'], delay=random.randint(50, 150))
            await page.type('input[name="username"]', user_data['username'], delay=random.randint(50, 150))
            await page.type('input[name="emailAddress"]', user_data['email'], delay=random.randint(30, 100))
            await page.type('input[name="password"]', user_data['password'], delay=random.randint(30, 100))
            
            # Agree to terms
            await page.click('input[type="checkbox"]')
            await asyncio.sleep(random.uniform(0.5, 2.0))
            
            # Click continue
            await page.click('button:has-text("Continue")')
            
            # Wait for auth
            await page.wait_for_timeout(7000) 
            
            print(f"[+] User {user_data['username']} registered. Moving to Circle...", flush=True)
            await page.goto(target_url, wait_until="networkidle")
            
            # Random scrolling behavior
            for _ in range(random.randint(2, 5)):
                await page.mouse.wheel(0, random.randint(300, 800))
                await asyncio.sleep(random.uniform(1, 3))

            # Like some, but not all posts randomly
            like_buttons = await page.query_selector_all('button:has-text("Like")')
            print(f"[*] Found {len(like_buttons)} like buttons. Acting randomly...", flush=True)
            
            # Shuffle buttons to interact in random order
            random.shuffle(like_buttons)
            # Pick a random number of posts to like (e.g. 30% to 70% of them)
            num_to_like = int(len(like_buttons) * random.uniform(0.3, 0.7))
            
            for btn in like_buttons[:num_to_like]:
                try:
                    # Hover first
                    await btn.hover()
                    await asyncio.sleep(random.uniform(0.5, 1.5))
                    await btn.click()
                    print(f"   - Liked a post randomly", flush=True)
                    await asyncio.sleep(random.uniform(2, 5)) 
                except:
                    pass
            
            # Stay on page for a bit longer to simulate reading
            await asyncio.sleep(random.uniform(10, 30))
            
            print(f"[+] Account {user_data['username']} finished random activity.", flush=True)
            
        except Exception as e:
            print(f"[!] Error with user {user_data['username']}: {e}")
        finally:
            await browser.close()

async def main():
    with open("natural_genpark_users.json", "r") as f:
        users = json.load(f)
    
    # Start from index 0 to use the brand new 100 high-quality accounts
    to_process = users[0:40] # Process a larger batch of 40
    
    # Increase batch size for faster processing
    batch_size = 5
    for i in range(0, len(to_process), batch_size):
        batch = to_process[i:i+batch_size]
        tasks = [register_and_like(u) for u in batch]
        await asyncio.gather(*tasks)
        print(f"--- Completed batch {i//batch_size + 1} / {len(to_process)//batch_size} ---", flush=True)

if __name__ == "__main__":
    asyncio.run(main())
