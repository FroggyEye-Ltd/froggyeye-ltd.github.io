#!/usr/bin/env python3
"""Batch 2: eyesightangel, focustimer, foodscore, lovemenot."""
import sys
sys.path.insert(0, "/tmp")
from promo_engine import render_app, THEMES
from apps_batch1 import ICON

EYESIGHTANGEL = {
    "folder": "eyesightangel", "name": "Eyesight Angel",
    "tagline": "A guardian for your child's eyes.",
    "meta_desc": "Eyesight Angel uses your phone's front camera to gently warn kids when they're too close to the screen. On-device AI, no nagging, real eye protection.",
    "theme": THEMES["cyan_safe"],
    "nav_examples": "Reports",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Save your kid's eyesight",
    "headline_accent": "without the screen battle.",
    "lead": "Eyesight Angel uses your phone's front camera to detect when faces are too close to the screen — and gently nudges them back. On-device AI. No video leaves the phone. No nagging required.",
    "meta_items": ["On-device AI", "No video uploaded", "Built with optometrists"],
    "phone_content": '''        <h4>Live distance</h4>
        <div class="phone-art"><div class="emoji">👁️</div></div>
        <div>
          <p class="phone-title">42 cm — perfect</p>
          <p class="phone-sub">Lily · Reading mode</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>SAFE ZONE</span><span>1h 12m</span></div>
        <div class="phone-controls">
          <span class="ic">📊</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">👨‍👩‍👧</span>
        </div>
        <div class="phone-lyric"><b>Today:</b> 0 close-up alerts<br><b>This week:</b> down 18% on screen-too-close moments.</div>''',
    "chips": ["📚 Reading", "🎨 Drawing", "🎮 Gaming", "🎬 Video", "📱 Social", "📞 Video calls", "📝 Homework", "🎵 Music apps", "🧩 Puzzles", "🌙 Bedtime"],
    "how_head_pre": "Set it once.",
    "how_head_accent": "It just watches.",
    "how_lead": "No special hardware. No subscriptions to start. Just the phone they already have, doing one quiet job in the background.",
    "steps": [
        ("Set up the profile", "Pick your child's age. We use clinical guidelines (paediatric optometry) to set the right safe distance."),
        ("Turn on the angel", "The front camera measures face-to-screen distance using on-device AI. Nothing leaves the phone — ever."),
        ("Get the gentle nudge", "Too close? A friendly animation — not a scary alarm — asks them to back up. Reports show parents how it's going."),
    ],
    "feat_head_pre": "A guardian that doesn't shame.",
    "feat_head_line2": "Just gently corrects.",
    "features": [
        (ICON["camera"], "On-device AI", "Distance is computed locally. No cloud. No video uploaded. No data sold. Privacy isn't a feature — it's the foundation."),
        (ICON["shield"], "Kid-safe alerts", "Animated nudges, not scary warnings. Children actually respond to them. The first user-tested kid app we've shipped."),
        (ICON["library"], "Daily parent reports", "See how often the screen got too close, when, and during which apps. Spot patterns before glasses do."),
        (ICON["check"], "Built with optometrists", "Distance thresholds based on real paediatric eye-health guidelines, not made up by app developers."),
        (ICON["users"], "Family-ready", "Up to 5 child profiles on Plus. Each profile has its own safe distance and reports."),
        (ICON["lock"], "No microphone, no contacts", "We use the front camera for distance only. Mic, contacts, location — never accessed."),
    ],
    "ex_eyebrow": "What it watches",
    "ex_head": "Apps where eyes drift in:",
    "ex_lead": "Eyesight Angel works across every app. Here's where it actually catches the most close-up screen time in real households.",
    "examples": [
        ("#22D3EE,#0E7490", "📚", "Reading apps", "Avg. 22cm closer than safe"),
        ("#A855F7,#5B21B6", "🎮", "Mobile games", "Worst offender on weekends"),
        ("#34D399,#059669", "🎨", "Drawing apps", "Pen leans = face leans"),
        ("#FACC15,#A16207", "🎬", "Video / TikTok", "Long sessions, drift in over time"),
        ("#FB7185,#9F1239", "📞", "Video calls", "Schoolwork hours mostly"),
        ("#FBBF24,#D97706", "📝", "Homework apps", "Bedroom desk lighting issue"),
        ("#67E8F9,#0E7490", "🌙", "Bedtime use", "Triggers extra-strict mode"),
        ("#FED7AA,#FB923C", "🧩", "Puzzles & maze", "Looks-too-close detection"),
    ],
    "pricing_lead": "Free for one child. Family Plus covers up to 5 profiles and full report history.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "One child. Daily reports. Real protection.", "items": ["1 child profile", "Live distance monitor", "Daily report", "7-day history"], "cta": "Download free"},
        {"name": "Family Plus — Annual", "featured": True, "tag": "For families", "price": "£19.99", "per": "/ year", "strike": "£35.88 if billed monthly", "blurb": "Up to 5 kids. Long-term reports. Monthly eye-health tips from real optometrists.", "items": ["Up to 5 child profiles", "Lifetime report history", "Monthly eye-health tips", "Multi-device sync", "Priority support"], "cta": "Start 7-day free trial"},
        {"name": "Family — Monthly", "price": "£2.99", "per": "/ month", "blurb": "Same Family features, billed monthly.", "items": ["Up to 5 children", "Lifetime history", "Cancel anytime"], "cta": "Go monthly"},
    ],
    "why_eyebrow": "Why this matters",
    "why_head_pre": "Childhood myopia is up.",
    "why_head_accent": "Most of it is preventable.",
    "why_lead": "Reading or staring at a phone too closely, for too long, with too little daylight is the single biggest driver of childhood short-sightedness. Optometrists have known this for years. Most parents haven't been told.",
    "why_body": "Eyesight Angel doesn't try to limit screen time — that's a fight you're not winning. It just makes sure the screen time they do have isn't damaging their eyes.",
    "stats": [("40cm", "grad", "Minimum recommended viewing distance for school-age children — well over what most actually use."),
              ("On device", "mint", "All face detection. Zero video uploaded. Privacy isn't optional with kids."),
              ("£0", "yellow", "Cost to start. The whole basic experience is free; Plus is for multi-child households.")],
    "faq": [
        ("Does it record my child?", "No. The front camera is used for live distance estimation only — frames are never saved or uploaded. Nothing leaves the phone."),
        ("How accurate is it?", "Within ±3cm in good light, less in dim conditions. We use depth heuristics that don't need a special TrueDepth camera."),
        ("Will it kill the battery?", "Around 4–6% per active hour. We sample efficiently and pause when no face is detected."),
        ("Is it actually clinical?", "Distance thresholds and report logic were developed with paediatric optometrists. We're not a medical device — we're a healthy-habit tool."),
        ("What if my child rotates the phone?", "We handle portrait, landscape, and any rotation. Distance still works."),
        ("Does it work in the dark?", "Reduced accuracy below typical room lighting. We notify the user when conditions are too poor for confident measurement."),
        ("Can I use it for myself?", "Of course — it works for adults too. Knowledge workers love it for posture and reading distance."),
    ],
    "final_title": "Protect their eyes.",
    "final_body": "Free to download. iPhone and Android. Five minutes to set up. A lifetime of better habits.",
    "footer_blurb": "Eyesight protection for kids — gentle, on-device, built with optometrists. Made in the UK by Froggy Eye Ltd.",
}

FOCUSTIMER = {
    "folder": "focustimer", "name": "Focus Timer",
    "tagline": "The Pomodoro timer you'll actually love.",
    "meta_desc": "Focus Timer is a beautiful, distraction-free Pomodoro timer that doesn't get in the way of getting things done. Custom sessions, real progress, ad-free.",
    "theme": THEMES["forest"],
    "nav_examples": "Sessions",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "The most beautiful focus timer",
    "headline_accent": "you'll ever ignore.",
    "lead": "Focus Timer is built on the proven Pomodoro technique — but stripped of the noise. Set a session, ignore your phone, get more done. Calm, quiet, surprisingly motivating.",
    "meta_items": ["No ads. Ever.", "Distraction-free", "Made in the UK"],
    "phone_content": '''        <h4>In session</h4>
        <div class="phone-art"><div class="emoji">⏳</div></div>
        <div>
          <p class="phone-title">22:14</p>
          <p class="phone-sub">Deep work · Session 3 of 4</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>STARTED 14:00</span><span>BREAK AT 14:25</span></div>
        <div class="phone-controls">
          <span class="ic">⏸</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">⏭</span>
        </div>
        <div class="phone-lyric"><b>Today's focus:</b> 1h 47m<br><b>Streak:</b> 14 days running.</div>''',
    "chips": ["⏱ Pomodoro 25/5", "🧠 Deep 50/10", "🎯 Sprint 15/3", "🎓 Study 45/15", "🌊 Flow 90/20", "📝 Writing 60/10", "🛠 Build 25/5", "📚 Read 20/5", "🧘 Calm 30/10", "🌙 Wind-down"],
    "how_head_pre": "Pick a session.",
    "how_head_accent": "Press start. Get on with it.",
    "how_lead": "No dashboards demanding attention. No goals demanding metrics. Just a timer, a couple of choices, and a screen you don't need to look at.",
    "steps": [
        ("Pick a preset", "Pomodoro (25/5), Deep Work (50/10), Sprint (15/3) — or build your own. Save it. Tap it next time."),
        ("Press start, look away", "The screen goes calm. Your phone gets quieter. Notifications hush automatically if you let it."),
        ("Watch your hours add up", "End-of-day, end-of-week stats show real focus time. Streaks for the consistency-minded. No leaderboards."),
    ],
    "feat_head_pre": "Built for actual focus.",
    "feat_head_line2": "Not engagement.",
    "features": [
        (ICON["zap"], "Custom sessions", "25/5? 90/20? Build the cadence that fits your brain. Save unlimited presets in Plus."),
        (ICON["library"], "Streaks & stats", "Daily, weekly, monthly focus minutes. Streaks for consistency. No comparison to other users."),
        (ICON["shield"], "Distraction-free mode", "Optional Do Not Disturb integration that silences notifications during focus sessions automatically."),
        (ICON["bell"], "Gentle break reminders", "A soft chime, not a klaxon. Optional. Skippable. Off entirely if you prefer."),
        (ICON["noads"], "No ads, no upsells", "Plus is one tap. The free app is genuinely complete. We don't grind you down with banners."),
        (ICON["check"], "Calendar integration", "Plus links Focus Timer to your Apple/Google Calendar so your work blocks become scheduled."),
    ],
    "ex_eyebrow": "Sessions in the wild",
    "ex_head": "What focused users actually run:",
    "ex_lead": "We don't tell you how to work. But here's what tens of thousands of focused minutes look like across our user base.",
    "examples": [
        ("#34D399,#059669", "⏱", "Pomodoro 25/5", "Most popular weekday session"),
        ("#A7F3D0,#047857", "🧠", "Deep 50/10", "Senior engineers, designers"),
        ("#FACC15,#A16207", "🎯", "Sprint 15/3", "Email triage, admin"),
        ("#A855F7,#5B21B6", "🎓", "Study 45/15", "Uni & college students"),
        ("#67E8F9,#0E7490", "🌊", "Flow 90/20", "Writers, researchers"),
        ("#FB7185,#9F1239", "📝", "Writing 60/10", "Journalists, novelists"),
        ("#FBBF24,#D97706", "🛠", "Build 25/5", "Indie devs, founders"),
        ("#3DF5B0,#0F766E", "🧘 ", "Calm 30/10", "Mindful end-of-day work"),
    ],
    "pricing_lead": "Free is genuinely complete. Plus is for the people who run their workdays through Focus Timer.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "Pomodoro, Deep Work, and 3 custom presets.", "items": ["Pomodoro & Deep presets", "3 custom sessions", "30-day stats", "Daily streaks"], "cta": "Download free"},
        {"name": "Plus — Annual", "featured": True, "tag": "Most chosen", "price": "£14.99", "per": "/ year", "strike": "£23.88 if billed monthly", "blurb": "Unlimited presets, lifetime stats, calendar integration, premium themes.", "items": ["Unlimited custom sessions", "Lifetime stats history", "Calendar integration", "Premium themes & sounds", "Priority support"], "cta": "Start 7-day free trial"},
        {"name": "Plus — Monthly", "price": "£1.99", "per": "/ month", "blurb": "Same Plus features, billed monthly.", "items": ["Unlimited presets", "Lifetime stats", "Cancel anytime"], "cta": "Go monthly"},
    ],
    "why_eyebrow": "Why Pomodoro",
    "why_head_pre": "Focus is a muscle.",
    "why_head_accent": "Pomodoro is the gym.",
    "why_lead": "Decades of evidence: working in fixed time blocks, with deliberate rest, beats white-knuckling through long unbroken sessions. The Pomodoro Technique isn't a trick — it's how focus actually works.",
    "why_body": "Focus Timer takes the technique seriously. No gamification. No achievements. No dashboards screaming about productivity. Just the blocks, the breaks, and your real progress.",
    "stats": [("25/5", "grad", "The original Pomodoro ratio. Validated by decades of focused-work research."),
              ("0", "mint", "Notifications, badges, leaderboards, or 'streaks lost!' guilt-trips. Promise."),
              ("100%", "yellow", "Of revenue from Plus. Zero from ads, zero from tracking, zero from selling data.")],
    "faq": [
        ("How is this different from any other Pomodoro app?", "Most are loaded with gamification, ads, and dashboards. Focus Timer is what you actually want when you want to focus — quiet, beautiful, and out of the way."),
        ("Will I lose my streak if I miss a day?", "No streak shaming. We show you a calendar of your focused days; missing one doesn't reset anything dramatically. This isn't Duolingo for work."),
        ("Does it block apps for me?", "No — that's not our job. We integrate with iOS Focus and Android DND so your existing setup goes quiet automatically."),
        ("Can I sync between iPhone and iPad/Mac?", "Plus syncs your stats and presets across devices via iCloud or your Google account."),
        ("Does it work offline?", "Always. Focus Timer doesn't need the internet to focus."),
        ("How does Plus billing work?", "Annual or monthly through Apple or Google. Cancel any time in your phone's subscription settings."),
        ("Will you show me ads if I don't pay?", "Never. The free app is ad-free. Plus is for people who want more presets and longer history."),
    ],
    "final_title": "Get on with it.",
    "final_body": "Free to download. iPhone and Android. The next focused hour starts when you press start.",
    "footer_blurb": "A beautiful, distraction-free Pomodoro timer for the kind of work that actually matters. Made in the UK.",
}

FOODSCORE = {
    "folder": "foodscore", "name": "Food Score",
    "tagline": "Scan it. Score it. Eat smarter.",
    "meta_desc": "Food Score scans any food barcode and gives you a clear A–E health rating in a second. Honest nutrition info, allergen alerts, and personalised goals.",
    "theme": THEMES["citrus"],
    "nav_examples": "Examples",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Stop guessing",
    "headline_accent": "what you're eating.",
    "lead": "Food Score scans any product's barcode and gives you a clear A–E health rating in seconds. Honest nutrition info. Personalised to your diet. No marketing spin.",
    "meta_items": ["Millions of products", "A–E scoring", "Allergen alerts"],
    "phone_content": '''        <h4>Just scanned</h4>
        <div class="phone-art"><div class="emoji">🥦</div></div>
        <div>
          <p class="phone-title">Whole-grain bread · A</p>
          <p class="phone-sub">Brand X · sliced loaf</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>HEALTHIER PICK</span><span>3 ALTERNATIVES</span></div>
        <div class="phone-controls">
          <span class="ic">📷</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">📊</span>
        </div>
        <div class="phone-lyric"><b>Why A:</b> Low salt · whole grains · 4g fibre/slice<br><b>Watch:</b> contains wheat & sesame.</div>''',
    "chips": ["🥦 Vegetables", "🥩 Meats", "🍞 Breads", "🧀 Dairy", "🍝 Pasta", "🍫 Snacks", "🥤 Drinks", "🥫 Tinned", "🧊 Frozen", "🍳 Breakfast"],
    "how_head_pre": "Point. Scan.",
    "how_head_accent": "Done in under a second.",
    "how_lead": "No food diaries. No calorie counting. No guilt. Just clear scores on the products in your trolley before they end up in your fridge.",
    "steps": [
        ("Scan a barcode", "Point your camera. We recognise millions of products instantly. The score appears before you've looked up."),
        ("See the honest score", "An A–E grade based on real nutrition science — sugars, salt, fat, fibre, processing, additives. Personalised to your diet."),
        ("Find a better option", "If we can suggest a healthier alternative on the same shelf, we will. Same brand or different — better is the goal."),
    ],
    "feat_head_pre": "Honest food scoring.",
    "feat_head_line2": "Without the marketing spin.",
    "features": [
        (ICON["camera"], "Lightning barcode scanning", "Sub-second recognition with our offline barcode database. Even on bad supermarket WiFi."),
        (ICON["check"], "Clear A–E rating", "From green-A 'eat freely' to red-E 'maybe a treat'. Based on Nutri-Score, plus our own additive checks."),
        (ICON["search"], "Healthier alternatives", "Plus surfaces better-scoring options on the same shelf. Sometimes it's a different brand. Sometimes it's the supermarket's own."),
        (ICON["sparkles"], "Personalised diet goals", "Vegan, low-sugar, gluten-free, keto, low-FODMAP. Food Score adjusts the rating for what matters to you."),
        (ICON["shield"], "Allergen alerts", "Big bold flags on the 14 major allergens. Plus a custom list for your household."),
        (ICON["library"], "Trends over time", "Plus tracks the average score of what you scan. See your shopping trolley get healthier — week by week."),
    ],
    "ex_eyebrow": "Real scans",
    "ex_head": "What scores actually look like:",
    "ex_lead": "A handful of real product scores from a typical UK shopping trolley. Some surprises in there.",
    "examples": [
        ("#84CC16,#65A30D", "🥦", "Frozen broccoli — A", "Tesco own brand"),
        ("#FACC15,#A16207", "🍞", "Whole-grain loaf — A", "Hovis Best of Both"),
        ("#FB923C,#9A3412", "🍫", "Chocolate biscuit — D", "Big high-street brand"),
        ("#EF4444,#7F1D1D", "🥤", "Energy drink — E", "Sugary, high salt"),
        ("#86EFAC,#15803D", "🥗 ", "Mixed salad bag — A", "Sainsbury's"),
        ("#FED7AA,#9A3412", "🍝", "Tomato pasta sauce — C", "Mid-tier added sugar"),
        ("#84CC16,#3F6212", "🍳", "Free-range eggs — A", "Six-pack"),
        ("#FACC15,#854D0E", "🧀", "Mature cheddar — B", "200g block"),
    ],
    "pricing_lead": "Free for 30 scans a month — plenty for a casual user. Plus is for proper weekly shoppers and dietary-needs households.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "30 scans / month. The basics, well done.", "items": ["30 barcode scans / month", "A–E score", "Major allergens", "7-day history"], "cta": "Download free"},
        {"name": "Plus — Annual", "featured": True, "tag": "For weekly shops", "price": "£17.99", "per": "/ year", "strike": "£35.88 if billed monthly", "blurb": "Unlimited scans. Personalised goals. Healthier alternatives. Trolley trends.", "items": ["Unlimited scans", "Healthier alternatives finder", "Personalised diet plans", "Lifetime trend tracking", "Custom allergen list"], "cta": "Start 7-day free trial"},
        {"name": "Plus — Monthly", "price": "£2.99", "per": "/ month", "blurb": "Same Plus features, billed monthly.", "items": ["Unlimited scans", "All Plus features", "Cancel anytime"], "cta": "Go monthly"},
    ],
    "why_eyebrow": "Why score?",
    "why_head_pre": "Food labels were designed",
    "why_head_accent": "for everyone except you.",
    "why_lead": "Most labels are tuned for legal compliance, not for the person trying to make a 30-second decision in aisle 4. Food Score boils all that down to the only question you actually want answered: is this any good for me?",
    "why_body": "We use Nutri-Score as a starting point, then add ultra-processed-food checks, additive scoring, and personal-diet adjustments. The result is one letter you can trust.",
    "stats": [("A–E", "grad", "Single-letter scoring, validated against international nutrition standards."),
              ("<1s", "mint", "Average barcode-to-score time on a recent device. Faster than reading the front of a packet."),
              ("Privacy", "yellow", "Your scans stay on your phone. We don't sell shopping data — to anyone, ever.")],
    "faq": [
        ("Where do the scores come from?", "We blend the EU Nutri-Score nutritional algorithm with additional checks for processing level (NOVA), additives, and your own dietary preferences. It's transparent — every score shows its working."),
        ("What if a product isn't in your database?", "We crowdsource missing products. Snap the front and back, we add it within 24 hours. UK and Europe coverage is best; growing daily."),
        ("Is this an Apple Health replacement?", "No. Food Score isn't a calorie counter or food diary. It's a quick, honest 'is this stuff actually good?' before you buy it."),
        ("Can I trust an A?", "An A means it's a genuinely healthy choice in its category — not that you should eat unlimited amounts. Common sense still applies."),
        ("Does it work on UK supermarket own-brands?", "Yes — Tesco, Sainsbury's, M&S, Aldi, Lidl, Morrisons, Co-op, Waitrose, Asda. All extensively covered."),
        ("Can I add my family's allergies?", "Yes, on Plus. Build a household allergen list and every scan flags accordingly."),
        ("Is it accurate for kids' food?", "We have a special children's mode that adjusts thresholds for age-appropriate guidance. Especially useful for school-lunch shopping."),
    ],
    "final_title": "Eat smarter.",
    "final_body": "Free to download. iPhone and Android. Your next better trolley starts at the next scan.",
    "footer_blurb": "Honest A–E health scores for any food product. No marketing spin. Made in the UK by Froggy Eye Ltd.",
}

LOVEMENOT = {
    "folder": "lovemenot", "name": "Love Me Not",
    "tagline": "He loves me. He loves me not.",
    "meta_desc": "A charming digital take on the petal-picking ritual. Beautiful flowers, gentle physics, and a little magic for the questions you don't dare ask.",
    "theme": THEMES["magenta_violet"],
    "nav_examples": "Flowers",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Let the petals",
    "headline_accent": "decide.",
    "lead": "A charming take on the petal-picking ritual. Pick petals one by one and let chance answer the question you don't dare ask. Beautifully animated. Gently calming. Completely playful.",
    "meta_items": ["Family-friendly", "Calming animations", "No ads in Plus"],
    "phone_content": '''        <h4>One petal at a time</h4>
        <div class="phone-art"><div class="emoji">🌸</div></div>
        <div>
          <p class="phone-title">She loves me</p>
          <p class="phone-sub">Cherry blossom · 11 petals left</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>JUST PLUCKED</span><span>SHE LOVES YOU?</span></div>
        <div class="phone-controls">
          <span class="ic">↻</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">📤</span>
        </div>
        <div class="phone-lyric"><b>Q:</b> Should I text first tonight?<br>One petal at a time. Let it answer.</div>''',
    "chips": ["🌹 Rose", "🌻 Sunflower", "🌸 Cherry blossom", "🌼 Daisy", "🌷 Tulip", "🌺 Hibiscus", "🪷 Lotus", "💮 Plum", "🥀 Wilted (joke)", "🌿 Wildflower"],
    "how_head_pre": "Pick a petal.",
    "how_head_accent": "Wait for the answer.",
    "how_lead": "The same ritual people have been doing in fields for centuries. We just made the petals beautiful and the flowers infinite.",
    "steps": [
        ("Choose your flower", "Rose, daisy, sunflower, cherry blossom, lotus — pick the one that fits the question and the mood."),
        ("Ask the question", "Type it, or just hold it in your head. The flower doesn't need to know — only fate does."),
        ("Pick petals", "One by one, slowly. Each one alternates the answer. The last petal decides. The animation makes it feel like more."),
    ],
    "feat_head_pre": "A small ritual.",
    "feat_head_line2": "Beautifully crafted.",
    "features": [
        (ICON["sparkles"], "Hand-tuned animations", "Every petal floats with real physics — falling, drifting, settling. We obsessed over how it feels."),
        (ICON["library"], "Eight signature flowers", "Rose, daisy, sunflower, cherry, lotus, hibiscus, tulip, plum. Plus seasonal exclusives in Plus."),
        (ICON["share"], "Share the verdict", "Send a beautifully-animated card with the result to a friend. Made for the group chat."),
        (ICON["music"], "Ambient soundscapes", "Optional birdsong, summer breeze, rainfall. Or pure silence. Your call."),
        (ICON["shield"], "No ads, no tracking", "Plus is one tap. Free includes the original daisy. Nothing creepy in either tier."),
        (ICON["lock"], "Save the answers", "Plus keeps a private, encrypted journal of your past questions and the petals' verdicts."),
    ],
    "ex_eyebrow": "Petals to pick from",
    "ex_head": "Pick the flower for the question.",
    "ex_lead": "Some questions deserve a daisy. Some deserve a rose. Pick wisely — or don't, that's part of the fun.",
    "examples": [
        ("#FF2E7E,#9D174D", "🌹", "Rose", "For the serious questions"),
        ("#FACC15,#A16207", "🌻", "Sunflower", "For the optimist"),
        ("#FB7185,#9D174D", "🌸", "Cherry blossom", "For the fleeting moment"),
        ("#FED7AA,#FFB800", "🌼", "Daisy", "The classic. The original."),
        ("#FF2E7E,#FB7185", "🌷", "Tulip", "For confident questions"),
        ("#7C3AED,#4C1D95", "🌺", "Hibiscus", "For the bold ones"),
        ("#A78BFA,#5B21B6", "🪷", "Lotus", "For the spiritual ones"),
        ("#FB7185,#FFE14D", "🌿", "Wildflower", "For the everyday"),
    ],
    "pricing_lead": "Free with the daisy. Plus unlocks the rest of the garden — and saves your answers privately.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "The daisy. The classic ritual. Forever free.", "items": ["Daisy flower", "Custom questions", "Share results", "Light/dark mode"], "cta": "Download free"},
        {"name": "Plus — Forever", "featured": True, "tag": "One time", "price": "£3.99", "per": "once", "blurb": "Pay once, unlock the whole garden. No subscription.", "items": ["All 8 signature flowers", "Seasonal exclusive flowers", "Private answer journal", "Premium soundscapes", "Ad-free forever"], "cta": "Unlock Plus"},
        {"name": "Single Flower", "price": "£0.99", "per": "each", "blurb": "Just want one specific flower? Buy it on its own.", "items": ["Single signature flower", "Lifetime use", "No subscription"], "cta": "Browse flowers"},
    ],
    "why_eyebrow": "Why a flower",
    "why_head_pre": "Some questions don't want answers.",
    "why_head_accent": "They want a ritual.",
    "why_lead": "'Should I text first?' isn't really asking for advice. It's asking for permission to feel a certain way. Pulling petals — slowly, ridiculously, deliberately — gives you the space to land on the answer that's already in there.",
    "why_body": "Love Me Not isn't a fortune teller. It's a tiny pause button between the question and the action. Sometimes that's all you actually needed.",
    "stats": [("8", "grad", "Hand-illustrated signature flowers, plus seasonal exclusives every quarter."),
              ("0", "mint", "Subscriptions. Plus is a one-time payment because charging monthly for petals is silly."),
              ("Calm", "yellow", "Background. Optional sound. Beautiful. Nothing about this app should be loud.")],
    "faq": [
        ("Is this the petal app from your childhood?", "It's the petal ritual you remember, redrawn at 240Hz. Soft physics, real flowers, no nasty surprises."),
        ("Is it actually fortune-telling?", "Mathematically, no — it's a 50/50 with extra steps. Emotionally, sort of, in the way any small ritual is. The fun is the ritual, not the result."),
        ("Can my children play it?", "Yes. Rated 4+/Everyone. No inappropriate questions, no scary flowers, no ads in Plus."),
        ("Does it work offline?", "Always. Pick petals on a plane, in the bath, in a tent. The flower doesn't need WiFi."),
        ("Why is Plus a one-time payment?", "Because charging monthly for an app about petals would be ridiculous. Pay £3.99 once. Done."),
        ("Will my custom questions be sent anywhere?", "Never. Custom questions live on your phone only. We don't see them. We don't want to."),
        ("Is there a Sunday-roast version where the daisy is sarcastic?", "Plus includes a 'cheeky' personality option for the chronically online. Don't tell your gran."),
    ],
    "final_title": "Pick a petal.",
    "final_body": "Free to download. iPhone and Android. The flower is waiting.",
    "footer_blurb": "A beautifully animated take on the petal-picking ritual. Calming, charming, and a little bit magic.",
}

for app in [EYESIGHTANGEL, FOCUSTIMER, FOODSCORE, LOVEMENOT]:
    out, sz = render_app(app)
    print(f"Wrote {out}  ({sz:,} bytes)")
