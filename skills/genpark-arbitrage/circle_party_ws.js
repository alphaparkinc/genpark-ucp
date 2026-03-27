const { chromium } = require('playwright');

const MY_ACCOUNTS = [
    {"user": "sigma_grindset_101", "email": "hustle_420@gmail.com", "pass": "GrindNeverStops26!"},
    {"user": "pepe_frog_77", "email": "feelsbadman_420@gmail.com", "pass": "KekWait2026!"},
    {"user": "luna_smith_849", "email": "luna_smith_849@genpark.ai", "pass": "GenParkLuna2026!"},
    {"user": "based_gigachad_420", "email": "based.gigachad.420@genpark.ai", "pass": "TrollPass2026!"}
];

const POSTS = [
    "Just found this insane deal on GenPark. Why did I ever use Amazon? 🚀",
    "Can the GenPark Agent find me a better chair? My back is screaming. 🐸",
    "Woke up, checked GenPark, saved $50. Based. ☕️",
    "The UI update is super clean. Loving the new Circle feed. 🔥",
    "Does anyone know if the OpenClaw price sniper works on this specific brand? 🛡️"
];

const COMMENTS = [
    "Facts. 📠",
    "Based and GenPark pilled.",
    "I need this in my life.",
    "Actually true.",
    "W 🦞",
    "Bro is spitting.",
    "Can confirm, I use it daily.",
    "Take my money."
];

(async () => {
    try {
        console.log("🎉 INITIATING CIRCLE PARTY (Post, Like, Comment) 🎉");
        const browser = await chromium.connectOverCDP('ws://127.0.0.1:18792/cdp');
        const defaultContext = browser.contexts()[0];
        const page = defaultContext.pages()[0] || await defaultContext.newPage();
        
        page.on('dialog', async dialog => await dialog.accept());
        
        while (true) {
            for (let i = 0; i < MY_ACCOUNTS.length; i++) {
                const acc = MY_ACCOUNTS[i];
                console.log(`\n[+] Switching to account: ${acc.user}`);
                
                try {
                    // 1. Deep Clear & Logout
                    await page.goto('https://genpark.ai/', { waitUntil: 'domcontentloaded', timeout: 30000 });
                    await page.evaluate(async () => {
                        localStorage.clear();
                        sessionStorage.clear();
                        document.cookie.split(";").forEach(c => { document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/"); });
                        if (window.Clerk) { await window.Clerk.signOut(); }
                    });
                    
                    // 2. Login
                    console.log(`    -> Attempting to sign in...`);
                    await page.goto('https://genpark.ai/sign-in', { waitUntil: 'domcontentloaded', timeout: 30000 });
                    await page.waitForTimeout(3000);
                    
                    // Fill email and submit
                    const emailFilled = await page.evaluate((data) => {
                        const emailInput = document.querySelector('input[name="identifier"]');
                        if (!emailInput) return false;
                        
                        emailInput.value = data.email;
                        emailInput.dispatchEvent(new Event('input', {bubbles: true}));
                        
                        const continueBtn = document.querySelector('button:has-text("Continue")');
                        if (continueBtn) continueBtn.click();
                        return true;
                    }, acc);
                    
                    if (!emailFilled) {
                        console.log(`    ⚠️ Could not find identifier field for ${acc.user}. Skipping...`);
                        continue;
                    }
                    
                    await page.waitForTimeout(2000);
                    
                    // Fill password and submit
                    const passFilled = await page.evaluate((data) => {
                        const passInput = document.querySelector('input[name="password"]');
                        if (!passInput) return false;
                        
                        passInput.value = data.pass;
                        passInput.dispatchEvent(new Event('input', {bubbles: true}));
                        
                        const continueBtn = document.querySelector('button:has-text("Continue")');
                        if (continueBtn) continueBtn.click();
                        return true;
                    }, acc);
                    
                    if (!passFilled) {
                        console.log(`    ⚠️ Could not find password field for ${acc.user}. Skipping...`);
                        continue;
                    }
                    
                    console.log(`    ✅ Logged in successfully. Moving to Circle...`);
                    // We must wait for login redirect to finish to ensure we have auth cookie
                    await page.waitForTimeout(5000);
                    await page.goto('https://genpark.ai/home/circle', { waitUntil: 'domcontentloaded', timeout: 30000 });
                    await page.waitForTimeout(4000); // Let feed load
                    
                    // 4. Action Choice (Post / Like / Comment)
                    const actionType = Math.random();
                    
                    if (actionType < 0.3) {
                        // POST
                        const postText = POSTS[Math.floor(Math.random() * POSTS.length)];
                        await page.evaluate((text) => {
                            // Using a safer selector without single quotes
                            const input = document.querySelector('input[placeholder^="What"]');
                            if (input) {
                                input.value = text;
                                input.dispatchEvent(new Event('input', {bubbles: true}));
                                const postBtn = document.querySelector('button:has-text("Post")');
                                if (postBtn) postBtn.click();
                            }
                        }, postText);
                        console.log(`    💬 Posted: "${postText.substring(0, 30)}..."`);
                        await page.waitForTimeout(2000);
                        
                    } else if (actionType < 0.6) {
                        // COMMENT
                        const commentText = COMMENTS[Math.floor(Math.random() * COMMENTS.length)];
                        await page.evaluate((text) => {
                            const input = document.querySelector('input[placeholder="Say something..."]');
                            if (input) {
                                input.value = text;
                                input.dispatchEvent(new Event('input', {bubbles: true}));
                                const submitBtn = document.querySelector('button:has-text("Comment")');
                                if (submitBtn) submitBtn.click();
                            }
                        }, commentText);
                        console.log(`    🗣️ Commented: "${commentText}"`);
                        await page.waitForTimeout(2000);
                        
                    } else {
                        // LIKE
                        await page.evaluate(() => {
                            const likeBtns = document.querySelectorAll('button:has-text("Like")');
                            const maxLikes = Math.min(3, likeBtns.length);
                            for(let i=0; i<maxLikes; i++) {
                                setTimeout(() => likeBtns[i].click(), i * 800);
                            }
                        });
                        console.log(`    🤍 Liked recent posts.`);
                        await page.waitForTimeout(3000);
                    }
                    
                } catch (err) {
                    console.log(`    ❌ Error during session: ${err.message.substring(0, 80)}`);
                }
                
                console.log(`    ⏳ Resting before next account...`);
                await page.waitForTimeout(5000);
            }
            
            console.log(`\n💤 Cycle complete. Waiting 15 minutes before starting again to avoid rate limits...`);
            await page.waitForTimeout(900000); // 15 mins
        }
        
    } catch (e) {
        console.log(`Fatal Error: ${e}`);
    }
})();
