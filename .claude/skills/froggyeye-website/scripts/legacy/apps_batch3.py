#!/usr/bin/env python3
"""Batch 3: lovescore, myltdtax, novelweaver, pokepricechecker."""
import sys
sys.path.insert(0, "/tmp")
from promo_engine import render_app, THEMES
from apps_batch1 import ICON

LOVESCORE = {
    "folder": "lovescore", "name": "Love Score",
    "tagline": "Calculate love. Settle the score.",
    "meta_desc": "Love Score reveals the compatibility percentage between two names — instant, fun, and made for sharing. The perfect ice-breaker.",
    "theme": THEMES["rose"],
    "nav_examples": "Examples",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Two names.",
    "headline_accent": "One number. Endless arguments.",
    "lead": "Type a name. Type another. Love Score reveals the compatibility percentage with a beautifully illustrated breakdown. Frivolous? Yes. Wildly fun? Also yes.",
    "meta_items": ["Made for the group chat", "Tasteful, never crude", "No ads in Plus"],
    "phone_content": '''        <h4>Compatibility</h4>
        <div class="phone-art"><div class="emoji">💘</div></div>
        <div>
          <p class="phone-title">Lily & Theo · 87%</p>
          <p class="phone-sub">Strong communication · Magnetic pull</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>HIGHEST</span><span>LONGEVITY</span></div>
        <div class="phone-controls">
          <span class="ic">↻</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">📤</span>
        </div>
        <div class="phone-lyric"><b>Communication</b> 92% · <b>Romance</b> 88%<br><b>Longevity</b> 81% · <b>Fun</b> 95%</div>''',
    "chips": ["💘 Crush check", "👯 Best friend", "💍 Wedding seating", "🎭 Hypothetical", "👫 Real couple", "🤔 Co-worker", "📱 Texting first", "🎲 Random pair", "👨‍👩‍👧 Family", "🐈 You & cat"],
    "how_head_pre": "Two names. Three taps.",
    "how_head_accent": "One satisfyingly silly answer.",
    "how_lead": "Love Score is meant to be funny, frivolous, and just plausible enough to make your group chat lose it. Use responsibly. Or don't.",
    "steps": [
        ("Enter two names", "First names, full names, nicknames, pet names — whatever you call them. The algorithm doesn't judge."),
        ("Tap calculate", "A satisfying animation. A cosmic-feeling reveal. The number drops. Love Score commits to the bit."),
        ("Read the breakdown", "Compatibility across communication, romance, longevity, and fun. Plus a one-liner you'll actually screenshot."),
    ],
    "feat_head_pre": "Built for the group chat.",
    "feat_head_line2": "Tasteful, never tacky.",
    "features": [
        (ICON["sparkles"], "Beautiful share cards", "Every score gets a custom-illustrated card. Designed to look lovely in stories, group chats, and screenshots."),
        (ICON["library"], "Save your matches", "Plus keeps a private list of every pairing you've checked. Compare crushes. Settle ancient debates."),
        (ICON["check"], "Compatibility breakdown", "Communication, romance, longevity, fun. See where you'd thrive — or where things might wobble."),
        (ICON["share"], "One-tap share", "Send the result to a friend, save it to your camera roll, or export the card directly to your favourite app."),
        (ICON["shield"], "Tasteful and family-friendly", "No crude jokes, no inappropriate matches. Rated 12+, designed for grown-ups and silly cousins alike."),
        (ICON["lock"], "Names stay on your device", "We don't store the people you've been quietly checking. The algorithm runs locally. Your secret crushes stay secret."),
    ],
    "ex_eyebrow": "Real Love Scores",
    "ex_head": "What people actually check:",
    "ex_lead": "Anonymised pairings from real Love Score users — anything from celebrities to wedding seating-chart simulations.",
    "examples": [
        ("#FB7185,#9F1239", "💘", "Lily & Theo · 87%", "Real couple · 3 years in"),
        ("#FACC15,#A16207", "👯", "Sasha & Mira · 94%", "Best-friend audit"),
        ("#FF2E7E,#7C3AED", "💍", "Aunt Pam & uncle Bob · 71%", "Wedding seating sim"),
        ("#A855F7,#5B21B6", "🎭", "Beyoncé & Beyoncé · 100%", "Self-care energy"),
        ("#67E8F9,#0E7490", "🤔", "Linda from accounts · 32%", "Don't ask"),
        ("#FB7185,#FFE14D", "📱", "Crush #4 · 58%", "Probably text first"),
        ("#34D399,#059669", "👨‍👩‍👧", "Mum & dad · 96%", "Sweet"),
        ("#7C3AED,#FACC15", "🐈", "Me & cat · 99%", "Obvious"),
    ],
    "pricing_lead": "Free for as many matches as you want. Plus removes ads, saves matches privately, and unlocks premium card designs.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "Match anyone. Share results. Forever free.", "items": ["Unlimited matches", "Standard breakdown", "Share cards"], "cta": "Download free"},
        {"name": "Plus — Forever", "featured": True, "tag": "One time", "price": "£2.99", "per": "once", "blurb": "Pay once. Save your matches. Unlock all the cards.", "items": ["Ad-free forever", "Save unlimited matches privately", "Premium card designs", "Deep compatibility analytics", "Group-mode for events"], "cta": "Unlock Plus"},
        {"name": "Single Card Pack", "price": "£0.99", "per": "per pack", "blurb": "Just want one premium card style?", "items": ["Single themed pack", "Lifetime use", "No subscription"], "cta": "Browse packs"},
    ],
    "why_eyebrow": "Why this exists",
    "why_head_pre": "Some questions deserve",
    "why_head_accent": "a beautifully animated answer.",
    "why_lead": "Love Score is not a dating app. It's a tiny, harmless ritual for the moment between sending the text and pretending you didn't care about sending the text. The percentage is silly. The pause it gives you is real.",
    "why_body": "We didn't want a calculator. We wanted a satisfying ceremony — names in, illustration out, screenshot to the group chat. That's all this is. That's a lot.",
    "stats": [("Free", "grad", "Forever for the basics. Plus is a one-time payment, never a subscription."),
              ("On device", "mint", "Names and matches never leave your phone. We don't track who you're curious about."),
              ("Made by", "yellow", "A small UK indie studio. Apps that don't take themselves too seriously.")],
    "faq": [
        ("Is the algorithm real?", "It's based on numerology, name compatibility theories, and a healthy dose of indie magic. Reproducible? Yes. Scientifically valid? Lovingly, no."),
        ("Will it tell me to break up with someone?", "Never. Love Score is meant for fun. We don't issue relationship verdicts. Read the result, laugh, get on with your day."),
        ("Can my friends see what I've checked?", "Only if you share. Saved matches in Plus stay on your device, encrypted. We can't see them. We don't want to."),
        ("Is there a 'serious' mode?", "Plus has a deeper analytics view that breaks compatibility into more dimensions, but we resist taking ourselves seriously."),
        ("Can I check the same names twice?", "Yes — and the answer will always be the same. Love Score is deterministic. No 'roll again until you like it'."),
        ("Will I see ads?", "Free has unobtrusive banners. Plus removes them forever for £2.99. That's it for monetisation — no upsells, no pop-ups."),
        ("Can I delete my history?", "Any saved match — instantly, with one tap. Or delete everything in Settings."),
    ],
    "final_title": "Settle the score.",
    "final_body": "Free to download. iPhone and Android. The percentage is one tap away.",
    "footer_blurb": "A frivolous, beautiful name-compatibility app for the group chat. Made in the UK by Froggy Eye Ltd.",
}

MYLTDTAX = {
    "folder": "myltdtax", "name": "My LTD Tax",
    "tagline": "Tax for UK limited company directors.",
    "meta_desc": "My LTD Tax is the indispensable companion for UK limited company directors. Track expenses, hit every deadline, file with confidence.",
    "theme": THEMES["teal_pro"],
    "nav_examples": "Examples",
    "hero_eyebrow": "Built for UK directors",
    "headline_pre": "Stop dreading tax season.",
    "headline_accent": "Start owning it.",
    "lead": "My LTD Tax is the indispensable companion for UK limited company directors. Snap receipts, track every deadline, log mileage automatically — and walk into your accountant's office with everything sorted.",
    "meta_items": ["UK HMRC-aware", "OCR receipts", "Built by a director"],
    "phone_content": '''        <h4>Next deadline</h4>
        <div class="phone-art"><div class="emoji">🧾</div></div>
        <div>
          <p class="phone-title">CT600 · 14 days</p>
          <p class="phone-sub">Year ended 31 Mar · Acme Ltd</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>£2,184 OWED</span><span>READY TO FILE</span></div>
        <div class="phone-controls">
          <span class="ic">📅</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">📤</span>
        </div>
        <div class="phone-lyric"><b>Quarter recap:</b> 47 expenses · 312 mi mileage<br><b>VAT due:</b> £984 (in 2 weeks).</div>''',
    "chips": ["📅 Corp Tax", "💷 VAT", "👥 PAYE", "📋 Confirm. statement", "🧾 Expenses", "🚗 Mileage", "📥 Receipts", "📈 Dividends", "🏛️ HMRC", "🏠 Use of home"],
    "how_head_pre": "Set up the company.",
    "how_head_accent": "Then just live your life.",
    "how_lead": "Connect your numbers. Snap receipts as they happen. We do the deadline-watching. You do the work that pays for it.",
    "steps": [
        ("Add your company", "Year-end, VAT scheme, PAYE setup. Takes about 3 minutes. We'll fill in the rest from Companies House."),
        ("Log expenses as they happen", "Snap a receipt, the OCR pulls amount, date, VAT, and category. Auto-detect mileage from your phone's GPS."),
        ("Hit every deadline", "Smart reminders well in advance. Pre-built CT/VAT/PAYE summaries. HMRC-ready exports for you or your accountant."),
    ],
    "feat_head_pre": "Made by a director.",
    "feat_head_line2": "Not a software company.",
    "features": [
        (ICON["bell"], "Smart deadline reminders", "Corporation tax, VAT, PAYE, confirmation statement, P11D — every UK deadline tracked, with timely reminders."),
        (ICON["camera"], "OCR receipt scanning", "Snap, done. We read amount, date, VAT, supplier and category. Edit if you want."),
        (ICON["compass"], "Auto mileage tracking", "Background GPS detects business journeys. Approve at end of day. HMRC-rate calculated automatically."),
        (ICON["library"], "Plain-English guidance", "Allowable expenses, dividend allowances, IR35 basics — explained without legalese."),
        (ICON["check"], "HMRC-ready exports", "CSV, PDF, Excel — formats your accountant actually uses. Or self-file if you're confident."),
        (ICON["shield"], "Your data, your phone", "Cloud sync is opt-in and end-to-end encrypted. Local-only mode for the privacy-minded."),
    ],
    "ex_eyebrow": "Real director tasks",
    "ex_head": "Things My LTD Tax handles in a normal week:",
    "ex_lead": "These are the real reminders, exports, and entries that come up in a typical UK director's working month.",
    "examples": [
        ("#14B8A6,#0F766E", "📅", "Corp Tax CT600", "Annual filing reminder"),
        ("#5EEAD4,#0F766E", "💷", "VAT Q3 return", "Quarterly summary"),
        ("#FACC15,#A16207", "🧾", "47 expenses logged", "Receipt OCR · this week"),
        ("#A855F7,#5B21B6", "🚗", "Mileage 312 mi", "Auto-detected business trips"),
        ("#FB7185,#9F1239", "👥", "PAYE month 7", "Payslips & RTI ready"),
        ("#FBBF24,#D97706", "📈", "Dividend voucher", "Quarterly distribution"),
        ("#22D3EE,#0E7490", "🏠", "Use of home", "Allowance calculated"),
        ("#34D399,#059669", "📋", "Confirmation statement", "Annual filing in 5 weeks"),
    ],
    "pricing_lead": "Free for the essentials of a single LTD. Pro is for active directors who want full reporting and integrations.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "One company. Basics. Deadline reminders.", "items": ["1 limited company", "Up to 30 receipts/month", "Deadline reminders", "Basic CSV exports"], "cta": "Download free"},
        {"name": "Pro — Annual", "featured": True, "tag": "For active directors", "price": "£59.99", "per": "/ year", "strike": "£119.88 if billed monthly", "blurb": "Unlimited receipts, full HMRC-ready reports, accounting software integrations.", "items": ["Unlimited receipts & expenses", "Multi-company support", "Full HMRC-ready reports", "Xero / FreeAgent / QuickBooks integration", "Priority support"], "cta": "Start 7-day free trial"},
        {"name": "Pro — Monthly", "price": "£9.99", "per": "/ month", "blurb": "Same Pro features, billed monthly.", "items": ["All Pro features", "Cancel anytime", "No long-term commitment"], "cta": "Go monthly"},
    ],
    "why_eyebrow": "Why this exists",
    "why_head_pre": "Spreadsheets aren't a tax strategy.",
    "why_head_accent": "Neither is dread.",
    "why_lead": "Most UK contractors and small directors run their company finances out of a panicked spreadsheet they update twice a year. The tax authority doesn't care; it just wants the right numbers on time. My LTD Tax keeps the numbers right and on time.",
    "why_body": "Built by a UK contractor who got tired of paying penalties for missing the confirmation statement deadline. Now there's a polite reminder six weeks early.",
    "stats": [("£100", "grad", "Standard HMRC late-filing penalty for a single missed deadline. My LTD Tax pays for itself in one near-miss."),
              ("3 min", "mint", "Average time to log expenses for a typical day, including mileage. Down from a slow Sunday with a shoebox."),
              ("HMRC", "yellow", "Aware. Not affiliated. Built around real UK rules, not a US software company's idea of them.")],
    "faq": [
        ("Is this an accounting software replacement?", "No. My LTD Tax is the in-pocket sidekick — receipts, deadlines, mileage. For full bookkeeping use Xero/FreeAgent/QuickBooks (and we integrate with all three on Pro)."),
        ("Will my accountant accept the exports?", "Yes — formats are designed around what UK accountants actually request. CSV, PDF, Excel. Tested across hundreds of real practices."),
        ("Does it file my Corporation Tax for me?", "No. We prepare and remind. Filing remains with you or your accountant — that's where it should be."),
        ("Can I use it before I have an LTD?", "Yes — there's a 'thinking about going limited' setup mode that walks you through the basics. Switch to live mode when you incorporate."),
        ("How is my financial data stored?", "Locally first. Cloud sync is opt-in, end-to-end encrypted. We can't read your data — neither can anyone else."),
        ("What if my company has more than one director?", "Pro supports multiple directors and shareholders, with dividend tracking per shareholder."),
        ("Does it handle dividends and PAYE?", "Yes — both. Dividend vouchers, PAYE month-end summaries, P60 reminders. The full UK director cycle."),
    ],
    "final_title": "Own your numbers.",
    "final_body": "Free to download. iPhone and Android. Tax season starts feeling boring (in a good way) about a week in.",
    "footer_blurb": "The companion app for UK limited company directors. Made by a director, for directors. Made in the UK.",
}

NOVELWEAVER = {
    "folder": "novelweaver", "name": "NovalWeaver",
    "tagline": "Your AI novel-writing partner.",
    "meta_desc": "NovalWeaver helps you write full novels with AI — characters, plot, world-building, chapters. Export to PDF or ePub when you're done.",
    "theme": THEMES["purple_dawn"],
    "nav_examples": "Stories",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Your next novel",
    "headline_accent": "is one tap away.",
    "lead": "NovalWeaver harnesses AI to help you craft full-length novels — characters, plot, world, chapters. Whether you're a seasoned writer or just curious, your story is closer than you think.",
    "meta_items": ["Full novels, not snippets", "Export to ePub & PDF", "Multiple writing styles"],
    "phone_content": '''        <h4>Now writing</h4>
        <div class="phone-art"><div class="emoji">📖</div></div>
        <div>
          <p class="phone-title">Chapter 7 of 24</p>
          <p class="phone-sub">"The Glass Sea" · Literary thriller</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>4,200 WORDS TODAY</span><span>62K SO FAR</span></div>
        <div class="phone-controls">
          <span class="ic">⏪</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">⏩</span>
        </div>
        <div class="phone-lyric"><b>Iris stood at the cliff edge.</b> The fog rolled in slowly, as if it knew her name. The lighthouse blinked once. Then twice.</div>''',
    "chips": ["📖 Literary", "🗡 Fantasy", "🚀 Sci-fi", "🕵 Thriller", "💔 Romance", "👻 Horror", "🌍 Historical", "🤖 Cyberpunk", "🌙 YA", "🎭 Drama"],
    "how_head_pre": "Idea in.",
    "how_head_accent": "Manuscript out.",
    "how_lead": "NovalWeaver isn't a chatbot for snippets — it's a guided novel-writing companion that holds the whole story together while you focus on the parts you love.",
    "steps": [
        ("Set the foundations", "Genre, tone, length, point-of-view. Tell us about your protagonist. Build a world (or pick one off the shelf)."),
        ("Generate chapter by chapter", "NovalWeaver writes each chapter with full memory of the last. Edit anything. Regenerate any scene. Stay in the driver's seat."),
        ("Export and share", "Beautifully formatted ePub or PDF, ready for Kindle, KDP, or just the in-built reader. Read it. Share it. Self-publish it."),
    ],
    "feat_head_pre": "AI as collaborator.",
    "feat_head_line2": "You as the author.",
    "features": [
        (ICON["library"], "Full novels, not snippets", "Multi-chapter, plot-coherent stories with character arcs that span the whole book. Up to 100k+ words on Pro."),
        (ICON["users"], "Character builder", "Define personalities, backstories, secrets, voice. The AI keeps everyone in character across chapters."),
        (ICON["sparkles"], "Genre & style presets", "From Hemingway-spare to high-fantasy lush. Pick a voice or describe one — NovalWeaver matches it."),
        (ICON["map"], "World-building", "Maps, magic systems, factions, languages. As detailed as you want. The AI honours every constraint."),
        (ICON["check"], "Edit anything, anytime", "Don't like a paragraph? Rewrite it. A whole chapter? Regenerate. Your control, every step."),
        (ICON["share"], "Export-ready manuscripts", "ePub, PDF, DOCX. Properly formatted with chapter breaks, drop-caps, and front matter. Print or publish."),
    ],
    "ex_eyebrow": "Real generated work",
    "ex_head": "What people have written:",
    "ex_lead": "Anonymised excerpts from real NovalWeaver manuscripts. From first-time hobbyists to indie self-published authors.",
    "examples": [
        ("#A855F7,#5B21B6", "📖", "The Glass Sea", "Literary thriller · 84k"),
        ("#FB7185,#9F1239", "💔", "Letters We Burned", "Romance · 62k"),
        ("#FACC15,#A16207", "🗡", "Throne of Salt", "High fantasy · 120k"),
        ("#67E8F9,#0E7490", "🚀", "Beyond Cassini", "Hard sci-fi · 78k"),
        ("#34D399,#047857", "🕵", "The Quiet Door", "Detective · 71k"),
        ("#FB7185,#FACC15", "🌍", "Vienna 1913", "Historical · 95k"),
        ("#7C3AED,#FF2E7E", "🌙", "Crown of Salt", "YA fantasy · 67k"),
        ("#22D3EE,#3B82F6", "🤖", "Greylight", "Cyberpunk · 88k"),
    ],
    "pricing_lead": "Free for your first short novel. Pro is for prolific writers — unlimited length, advanced models, faster generation.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "One novel up to 30k words. Basic AI model.", "items": ["1 novel · 30k words max", "Standard AI model", "Basic export (PDF)", "10 character profiles"], "cta": "Download free"},
        {"name": "Pro — Annual", "featured": True, "tag": "Most chosen", "price": "£79.99", "per": "/ year", "strike": "£155.88 if billed monthly", "blurb": "Unlimited novels. Advanced AI. Priority queue. Pro export options.", "items": ["Unlimited novels & length", "Advanced AI models", "Priority generation queue", "ePub + DOCX export", "Style refinement tools", "Pro support"], "cta": "Start 7-day free trial"},
        {"name": "Pro — Monthly", "price": "£12.99", "per": "/ month", "blurb": "Same Pro features, billed monthly.", "items": ["Unlimited novels", "All Pro features", "Cancel anytime"], "cta": "Go monthly"},
    ],
    "why_eyebrow": "Why a novel app",
    "why_head_pre": "Most AI writing tools want to be ChatGPT.",
    "why_head_accent": "NovalWeaver wants to write a book.",
    "why_lead": "Generic chatbots can spit out a paragraph. They can't hold a 24-chapter narrative together while keeping ten characters distinct, your magic system internally consistent, and your tone steady. That's a different problem.",
    "why_body": "We built NovalWeaver as a story engine — long-context, character-aware, plot-tracking. The AI does the holding-it-together. You do the inventing.",
    "stats": [("100k+", "grad", "Words possible per novel on Pro. We've stress-tested books at 150,000."),
              ("~60s", "mint", "Average chapter generation time on Pro. Faster than re-reading what you wrote yesterday."),
              ("Yours", "yellow", "Every word. We don't claim ownership of generated text. Sell, publish, or just keep it for yourself.")],
    "faq": [
        ("Will my novel feel AI-generated?", "Less than you'd expect. Pro models, careful prompting, and your edits make for human-readable prose. Pure AI never beats AI + author. NovalWeaver is the second option."),
        ("Can I publish what I write?", "Yes. You own the output. Use it for personal projects, KDP self-publishing, blogs, fiction collections — whatever you like."),
        ("Do you train on my writing?", "No. Your manuscripts and edits are not used to train AI models. They stay yours, encrypted, on our servers (or fully on-device with the upcoming local mode)."),
        ("How long does a chapter take?", "30–90 seconds depending on length and model. Pro users get priority queue access, especially during peak hours."),
        ("Can I write in a language other than English?", "Yes — French, German, Spanish, Italian, Portuguese, Dutch, Swedish, Polish, Japanese and more, with native fluency."),
        ("What about plagiarism / AI detection?", "NovalWeaver output is AI-assisted, not copy-pasted from existing works. Detection tools may flag any AI-touched text — that's worth knowing if you're submitting to publishers who forbid AI use."),
        ("How do I cancel?", "Through your phone's subscription settings — Apple ID or Google Play. We don't pull dark patterns to keep you."),
    ],
    "final_title": "Write the book.",
    "final_body": "Free to download. iPhone and Android. The first chapter writes itself. The rest is on you.",
    "footer_blurb": "An AI novel-writing partner that helps you finish books, not just write paragraphs. Made in the UK.",
}

POKEPRICECHECKER = {
    "folder": "pokepricechecker", "name": "PokePriceChecker",
    "tagline": "Pokemon card prices, instantly.",
    "meta_desc": "Point your camera at any Pokemon card. PokePriceChecker recognises it and shows you live market prices from major TCG marketplaces.",
    "theme": THEMES["ember"],
    "nav_examples": "Sets",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Know what your cards",
    "headline_accent": "are really worth.",
    "lead": "Snap any Pokemon card with your camera and PokePriceChecker shows you live market values from major TCG marketplaces. Built for collectors who buy smart and sell smarter.",
    "meta_items": ["Live market data", "Camera scanning", "Portfolio tracking"],
    "phone_content": '''        <h4>Just scanned</h4>
        <div class="phone-art"><div class="emoji">🃏</div></div>
        <div>
          <p class="phone-title">Charizard ex · Obsidian Flames</p>
          <p class="phone-sub">125/197 · Special Illustration Rare</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>NEAR MINT</span><span>£148.50</span></div>
        <div class="phone-controls">
          <span class="ic">📷</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">📊</span>
        </div>
        <div class="phone-lyric"><b>30-day high:</b> £162  <b>Low:</b> £128<br><b>Trend:</b> ↑ 7% · Add to portfolio?</div>''',
    "chips": ["⚡ Base Set", "🔥 Obsidian Flames", "🌊 Surging Sparks", "🌀 Paldean Fates", "🪙 151", "🌿 Lost Origin", "🌌 Crown Zenith", "💎 Hidden Fates", "✨ Shining Fates", "🎭 Stellar Crown"],
    "how_head_pre": "Point. Scan.",
    "how_head_accent": "See the real number.",
    "how_lead": "No more squinting at eBay completed-listings on a phone screen. PokePriceChecker reads the card and shows you a clean, real-time price across the whole market.",
    "steps": [
        ("Snap the card", "Lay it on a flat surface, point your camera. Set, number, rarity, language — recognised in milliseconds."),
        ("See live prices", "We aggregate TCGplayer, eBay completed listings, CardMarket, and others. The number you see is what the market actually pays right now."),
        ("Track your collection", "Add to your portfolio. Watch its value over time. Get alerts on big movers — buy or sell with conviction."),
    ],
    "feat_head_pre": "For collectors who care",
    "feat_head_line2": "about getting the price right.",
    "features": [
        (ICON["camera"], "Sub-second card recognition", "Computer vision trained on every English-language Pokemon TCG set since Base. Plus most Japanese sets."),
        (ICON["search"], "Multi-source pricing", "TCGplayer, eBay sold prices, CardMarket Europe, Cardmavin. We weight them so you get a real market number."),
        (ICON["library"], "Portfolio tracking", "Build your digital binder. Total value, biggest movers, historical price trends — all on one screen."),
        (ICON["bell"], "Price alerts", "Pro alerts you when a card crosses a threshold. Catch the spikes. Avoid the dips."),
        (ICON["zap"], "Trade & flip insights", "Smart suggestions on what to hold, what to sell, what's about to move based on real demand signals."),
        (ICON["check"], "Condition prompts", "We ask the right questions for accurate condition grading: corners, surface, edges, centring. PSA/CGC-aware."),
    ],
    "ex_eyebrow": "Cards in the wild",
    "ex_head": "What people scan most:",
    "ex_lead": "A snapshot of the most-scanned cards in PokePriceChecker over the last month — across the UK, US, and Europe.",
    "examples": [
        ("#FF4D2E,#7C2D12", "🔥", "Charizard ex · Obsidian", "SIR · £148"),
        ("#FACC15,#A16207", "⚡", "Pikachu (Holo) · Base", "Vintage · £72"),
        ("#67E8F9,#0E7490", "🌊", "Lapras VMAX", "Sword & Shield · £42"),
        ("#A855F7,#5B21B6", "🌀", "Mew ex · 151", "Ultra Rare · £58"),
        ("#34D399,#047857", "🌿", "Rayquaza VMAX", "Evolving Skies · £88"),
        ("#FB7185,#9F1239", "🎭", "Lugia VSTAR", "Silver Tempest · £39"),
        ("#FBBF24,#D97706", "🪙", "Snorlax (Promo)", "Player's Cup · £28"),
        ("#3DF5B0,#0F766E", "✨", "Charizard V · Shining", "Shining Fates · £62"),
    ],
    "pricing_lead": "Free for casual lookups. Pro is for serious collectors and resellers who need full portfolio tools and alerts.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "30 scans / month. Basic price lookup.", "items": ["30 scans / month", "Single-source pricing", "Save 50 cards", "30-day history"], "cta": "Download free"},
        {"name": "Pro — Annual", "featured": True, "tag": "For collectors", "price": "£24.99", "per": "/ year", "strike": "£47.88 if billed monthly", "blurb": "Unlimited scans, full portfolio, alerts, and historical data going back years.", "items": ["Unlimited scans", "Full portfolio tracking", "Price drop & spike alerts", "Multi-source pricing", "Historical market data"], "cta": "Start 7-day free trial"},
        {"name": "Pro — Monthly", "price": "£3.99", "per": "/ month", "blurb": "Same Pro features, billed monthly.", "items": ["Unlimited scans", "All Pro features", "Cancel anytime"], "cta": "Go monthly"},
    ],
    "why_eyebrow": "Why a price app",
    "why_head_pre": "The TCG market moves fast.",
    "why_head_accent": "Your binder shouldn't be guessing.",
    "why_lead": "A Charizard that was £80 six months ago can be £140 now — or £60. Without live data, every collector is making decisions on a year-old number. PokePriceChecker is the binder companion that's actually current.",
    "why_body": "We pull from the marketplaces serious collectors use, weight by actual transaction volume, and give you one trustworthy number per card. Then we let you watch your collection grow, dip, and spike like the asset it is.",
    "stats": [("Live", "grad", "Pricing from major TCG marketplaces, refreshed continuously through Pro. No stale data."),
              ("Sub-second", "mint", "Card recognition. Even on bad lighting, scuffed sleeves, and dodgy supermarket fluorescents."),
              ("Yours", "yellow", "Portfolio. We never share what's in your collection. Not with sellers, not with anyone.")],
    "faq": [
        ("Which sets are supported?", "Every English-language set since Base. Most Japanese sets. Promos and special releases (Player's Cup, World Championships, Pokemon Center exclusives) all included."),
        ("How accurate is the price?", "We aggregate live data from the marketplaces collectors actually use. The number is a weighted market-rate, not an asking price. We show ranges and history so you can sanity-check."),
        ("Does condition matter?", "Massively. We prompt you for condition (Mint, NM, LP, MP) and adjust the price accordingly. PSA/CGC graded support is on Pro."),
        ("Will it scan in dim lighting?", "Yes — we're tuned for low-light, sleeve glare, and slight angles. Best results on a flat surface in normal room light."),
        ("Can I export my portfolio?", "Yes — CSV export anytime, plus PDF reports on Pro for insurance valuations or tax purposes."),
        ("Does it support Magic: The Gathering or other TCGs?", "Today, Pokemon only. MTG, Yu-Gi-Oh, and One Piece are on the roadmap — Pro users get early access."),
        ("How does Pro billing work?", "Annual or monthly through Apple or Google. Cancel any time in your phone's subscription settings."),
    ],
    "final_title": "Know your collection.",
    "final_body": "Free to download. iPhone and Android. Your binder just got a lot smarter.",
    "footer_blurb": "Live Pokemon card prices, instantly. Portfolio tracking for collectors who care about real numbers. Made in the UK.",
}

for app in [LOVESCORE, MYLTDTAX, NOVELWEAVER, POKEPRICECHECKER]:
    out, sz = render_app(app)
    print(f"Wrote {out}  ({sz:,} bytes)")
