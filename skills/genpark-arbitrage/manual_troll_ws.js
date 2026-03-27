const { chromium } = require('playwright');
const http = require('http');

(async () => {
    try {
        console.log("🚀 ACTIVATING SINGLE TROLL (Manual Mode) 🚀");
        const browser = await chromium.connectOverCDP('ws://127.0.0.1:18792/cdp');
        const defaultContext = browser.contexts()[0];
        const page = defaultContext.pages()[0]; // Re-use exact tab
        
        // Anti-dialog block
        page.on('dialog', async dialog => await dialog.accept());
        
        const t = {"first": "Chad", "last": "Thunder", "user": "chad_thunder_cock", "email": "gymbro_420@gmail.com", "pass": "DoYouEvenLiftBro!"};
        console.log(`[+] Registering: ${t.user}`);
            
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
        await page.waitForTimeout(3000); // Breathe
                
        await page.waitForSelector('input[name="firstName"]', { timeout: 15000 });
                
        // Fill
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
                
        await page.waitForTimeout(1000);
        await page.click('button:has-text("Continue")');
                
        let success = false;
        for (let i = 0; i < 20; i++) {
            await page.waitForTimeout(1000);
            if (page.url().includes('preference') || page.url().includes('onboarding') || page.url().includes('home')) {
                success = true;
                break;
            }
        }
                
        if (success) {
            console.log(`    ✅ SUCCESS: ${t.user} entered the matrix.`);
        } else {
            console.log(`    ❌ [FAIL] Stuck at: ${page.url()}`);
        }
            
        await browser.disconnect();
    } catch (e) {
        console.log(`Fatal Error: ${e}`);
    }
})();
