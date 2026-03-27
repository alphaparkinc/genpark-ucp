const { chromium } = require('playwright');

const firsts = ["Pepe", "Sigma", "Chad", "Doge", "Wojak", "Karen", "Satoshi", "Diamond", "Laser", "Based", "Cringe", "Boomer", "Zoomer", "Giga", "Alpha", "Hodl", "Stonks"];
const lasts = ["Frog", "Grindset", "Thunder", "Coin", "Hands", "Eyes", "Maxi", "Male", "Female", "Troll", "Anon", "Whale", "Ape", "Moon", "Degen"];

function getTroll() {
    let f = firsts[Math.floor(Math.random()*firsts.length)];
    let l = lasts[Math.floor(Math.random()*lasts.length)];
    let n = Math.floor(Math.random()*9000)+1000;
    let u = `${f.toLowerCase()}_${l.toLowerCase()}_${n}`;
    return {first: f, last: l, user: u, email: `${u}@gmail.com`, pass: "TrollPass2026!"};
}

(async () => {
    try {
        console.log("🚀 INFINITE MEME SWARM (JS) ACTIVATED 🚀");
        const browser = await chromium.connectOverCDP('http://127.0.0.1:18792');
        const defaultContext = browser.contexts()[0];
        
        let count = 0;
        const page = defaultContext.pages()[0] || await defaultContext.newPage();
        
        while (true) {
            count++;
            const t = getTroll();
            console.log(`\n[+] Swarm #${count} - Registering: ${t.user}`);
            
            try {
                // Clear state
                await page.goto('https://genpark.ai/', { waitUntil: 'domcontentloaded', timeout: 30000 });
                await page.evaluate(async () => {
                    localStorage.clear();
                    sessionStorage.clear();
                    document.cookie.split(";").forEach(c => { document.cookie = c.replace(/^ +/, "").replace(/=.*/, "=;expires=" + new Date().toUTCString() + ";path=/"); });
                    if (window.Clerk) { await window.Clerk.signOut(); }
                });
                
                // Go to signup
                await page.goto('https://genpark.ai/sign-up', { waitUntil: 'domcontentloaded', timeout: 30000 });
                await page.waitForTimeout(2000);
                
                await page.waitForSelector('input[name="firstName"]', { timeout: 15000 });
                
                // Fill using standard evaluate/dispatchEvent for max stability against React
                await page.evaluate((data) => {
                  document.querySelector('input[name="firstName"]').value = data.first;
                  document.querySelector('input[name="firstName"]').dispatchEvent(new Event('input', {bubbles: true}));
                
                  document.querySelector('input[name="lastName"]').value = data.last;
                  document.querySelector('input[name="lastName"]').dispatchEvent(new Event('input', {bubbles: true}));
                
                  document.querySelector('input[name="username"]').value = data.user;
                  document.querySelector('input[name="username"]').dispatchEvent(new Event('input', {bubbles: true}));
                  
                  document.querySelector('input[name="emailAddress"]').value = data.email;
                  document.querySelector('input[name="emailAddress"]').dispatchEvent(new Event('input', {bubbles: true}));
                
                  document.querySelector('input[name="password"]').value = data.pass;
                  document.querySelector('input[name="password"]').dispatchEvent(new Event('input', {bubbles: true}));
                  
                  let cb = document.querySelector('input[type="checkbox"]');
                  if (cb && !cb.checked) { cb.click(); }
                }, t);
                
                await page.waitForTimeout(500);
                await page.click('button:has-text("Continue")');
                
                let success = false;
                for (let i = 0; i < 15; i++) {
                    await page.waitForTimeout(1000);
                    if (page.url().includes('preference') || page.url().includes('onboarding')) {
                        success = true;
                        break;
                    }
                }
                
                if (success) {
                    console.log(`    ✅ SUCCESS: ${t.user} has entered the matrix.`);
                    
                    // Click through preference quickly so clerk commits it if needed
                    try {
                        const tags = await page.$$('button');
                        if (tags.length > 2) {
                           await tags[2].click();
                           await page.waitForTimeout(500);
                           await page.click('button:has-text("Continue")');
                        }
                    } catch (e) {}
                    
                } else {
                    console.log(`    ❌ [FAIL] Stuck at: ${page.url()}`);
                }
            } catch (err) {
                console.log(`    ⚠️ [ERROR] ${err.message.substring(0,80)}`);
            }
            
            // Chill for 3 seconds before next assault
            await page.waitForTimeout(3000);
        }
    } catch (e) {
        console.log(`Fatal Error: ${e}`);
    }
})();
