#!/usr/bin/env python3
"""Batch 1: apexroute, blipblobb, doordigest, eightball."""
import sys
sys.path.insert(0, "/tmp")
from promo_engine import render_app, THEMES

# Reusable feature SVGs (Lucide-style 24x24, stroked)
ICON = {
    "music":     '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M9 18V5l12-2v13"/><circle cx="6" cy="18" r="3"/><circle cx="18" cy="16" r="3"/></svg>',
    "check":     '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="9 11 12 14 22 4"/><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"/></svg>',
    "share":     '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    "shield":    '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z"/></svg>',
    "noads":     '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polyline points="3 6 5 6 21 6"/><path d="M19 6l-1 14a2 2 0 0 1-2 2H8a2 2 0 0 1-2-2L5 6"/><path d="M10 11v6M14 11v6"/></svg>',
    "library":   '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 2v20M17 5H9.5a3.5 3.5 0 0 0 0 7h5a3.5 3.5 0 0 1 0 7H6"/></svg>',
    "map":       '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="1 6 1 22 8 18 16 22 23 18 23 2 16 6 8 2 1 6"/><line x1="8" y1="2" x2="8" y2="18"/><line x1="16" y1="6" x2="16" y2="22"/></svg>',
    "compass":   '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polygon points="16.24 7.76 14.12 14.12 7.76 16.24 9.88 9.88 16.24 7.76"/></svg>',
    "speed":     '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="10"/><polyline points="12 6 12 12 16 14"/></svg>',
    "wifi":      '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12.55a11 11 0 0 1 14.08 0"/><path d="M1.42 9a16 16 0 0 1 21.16 0"/><path d="M8.53 16.11a6 6 0 0 1 6.95 0"/><line x1="12" y1="20" x2="12.01" y2="20"/></svg>',
    "lock":      '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="11" width="18" height="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>',
    "users":     '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M17 21v-2a4 4 0 0 0-4-4H5a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M23 21v-2a4 4 0 0 0-3-3.87"/><path d="M16 3.13a4 4 0 0 1 0 7.75"/></svg>',
    "zap":       '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"/></svg>',
    "bell":      '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"/><path d="M13.73 21a2 2 0 0 1-3.46 0"/></svg>',
    "ai":        '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.65 1.65 0 0 0 .33 1.82l.06.06a2 2 0 0 1 0 2.83 2 2 0 0 1-2.83 0l-.06-.06a1.65 1.65 0 0 0-1.82-.33 1.65 1.65 0 0 0-1 1.51V21a2 2 0 0 1-4 0v-.09A1.65 1.65 0 0 0 9 19.4a1.65 1.65 0 0 0-1.82.33l-.06.06a2 2 0 0 1-2.83 0 2 2 0 0 1 0-2.83l.06-.06a1.65 1.65 0 0 0 .33-1.82 1.65 1.65 0 0 0-1.51-1H3a2 2 0 0 1 0-4h.09A1.65 1.65 0 0 0 4.6 9a1.65 1.65 0 0 0-.33-1.82l-.06-.06a2 2 0 0 1 0-2.83 2 2 0 0 1 2.83 0l.06.06a1.65 1.65 0 0 0 1.82.33H9a1.65 1.65 0 0 0 1-1.51V3a2 2 0 0 1 4 0v.09a1.65 1.65 0 0 0 1 1.51 1.65 1.65 0 0 0 1.82-.33l.06-.06a2 2 0 0 1 2.83 0 2 2 0 0 1 0 2.83l-.06.06a1.65 1.65 0 0 0-.33 1.82V9a1.65 1.65 0 0 0 1.51 1H21a2 2 0 0 1 0 4h-.09a1.65 1.65 0 0 0-1.51 1z"/></svg>',
    "camera":    '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M23 19a2 2 0 0 1-2 2H3a2 2 0 0 1-2-2V8a2 2 0 0 1 2-2h4l2-3h6l2 3h4a2 2 0 0 1 2 2z"/><circle cx="12" cy="13" r="4"/></svg>',
    "video":     '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><polygon points="23 7 16 12 23 17 23 7"/><rect x="1" y="5" width="15" height="14" rx="2" ry="2"/></svg>',
    "home":      '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M3 9l9-7 9 7v11a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2z"/><polyline points="9 22 9 12 15 12 15 22"/></svg>',
    "search":    '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>',
    "sparkles":  '<svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M12 3v3M12 18v3M3 12h3M18 12h3M5.6 5.6l2 2M16.4 16.4l2 2M5.6 18.4l2-2M16.4 7.6l2-2"/></svg>',
}

# ---------------- ApexRoute ----------------
APEXROUTE = {
    "folder": "apexroute",
    "name": "ApexRoute",
    "tagline": "Driving routes built for enthusiasts.",
    "meta_desc": "ApexRoute generates twisty, scenic, apex-hunting driving routes Google Maps would never offer. Then records every drive so you can relive it.",
    "theme": THEMES["ember"],
    "nav_examples": "Routes",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Find the road that makes you",
    "headline_accent": "feel alive.",
    "lead": "ApexRoute generates twisty backroads, scenic detours, and proper apex-hunting drives — the routes Google Maps would never offer. Record every run, save your favourites, and chase a better drive.",
    "meta_items": ["Built for drivers", "Offline maps", "Free to start"],
    "phone_content": '''        <h4>Today's drive</h4>
        <div class="phone-art"><div class="emoji">🛣️</div></div>
        <div>
          <p class="phone-title">The Snake Pass Loop</p>
          <p class="phone-sub">42 mi · 1h 12m · ★★★★☆</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>RECORDING</span><span>17.4 mi</span></div>
        <div class="phone-controls">
          <span class="ic">⏮</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">⏭</span>
        </div>
        <div class="phone-lyric"><b>Twisties ahead — 4.2 mi</b><br>Average lean: 22°. Top road in your county this month.</div>''',
    "chips": ["🛣️ Twisties", "⛰️ Mountain", "🏖️ Coastal", "🌳 Backroad", "🌅 Scenic", "🌀 Hairpins", "🪨 Pass", "🛤️ B-road", "🎯 Apex hunt", "🌙 Night run"],
    "how_head_pre": "Phone in. Banger road out.",
    "how_head_accent": "In about 30 seconds.",
    "how_lead": "No more dragging Maps around hoping for the good stuff. Tell ApexRoute what you want, get a route built around it, drive.",
    "steps": [
        ("Tell it the vibe", "Distance, twistiness, scenery. ApexRoute uses your starting point and finds roads that match — not the fastest, the best."),
        ("Hit Drive", "Live in-app navigation, with corner counts, gradient previews, and a heads-up display that doesn't shout at you."),
        ("Keep the memory", "Every drive recorded with route, telemetry, and notes. Replay it, share it, beat your own line next time."),
    ],
    "feat_head_pre": "Built by drivers.",
    "feat_head_line2": "Not by route planners.",
    "features": [
        (ICON["map"], "Routes that find roads", "Real-world data on twistiness, gradient and scenery — you get a drive worth waking up early for."),
        (ICON["video"], "Drive recording", "GPS, speed, lean angle, and corner-by-corner telemetry. Replay any drive on a map."),
        (ICON["compass"], "Heads-up nav", "Quiet, glanceable, and built for the road. No 'in 200 yards bear left for 35 yards.'"),
        (ICON["share"], "Share with mates", "Send a route to a friend. Convoy mode keeps you together. Argue about the line later."),
        (ICON["shield"], "Stays offline", "Maps download once and stay yours — even in the valleys and Highlands where signal disappears."),
        (ICON["library"], "Your library", "Favourites, recents, and 'my best ever drives'. Build the personal road book you wish you had."),
    ],
    "ex_eyebrow": "Roads worth the detour",
    "ex_head": "Sounds like:",
    "ex_lead": "A taste of routes ApexRoute users have driven, recorded, and rated this season.",
    "examples": [
        ("#FF4D2E,#7C2D12", "🌀", "Snake Pass Reverse", "Peak District · 42 mi"),
        ("#FBBF24,#D97706", "🏖️", "Coastal Hairpins", "Cornwall · 67 mi"),
        ("#A855F7,#5B21B6", "⛰️", "Buttertubs Loop", "Yorkshire Dales · 58 mi"),
        ("#FF4D2E,#FBBF24", "🌅", "Sunset B-road", "Mid Wales · 38 mi"),
        ("#22D3EE,#3B82F6", "🌀", "Highland Twisties", "Glencoe · 84 mi"),
        ("#34D399,#059669", "🌳", "Forest Pass", "Dean Forest · 29 mi"),
        ("#F43F5E,#9F1239", "🪨", "Stelvio Tribute", "Lake District · 72 mi"),
        ("#0EA5E9,#0369A1", "🌙", "Midnight Mountain", "Snowdonia · 51 mi"),
    ],
    "pricing_lead": "7-day free trial on Plus. Cancel anytime in your phone's subscription manager. No ads either way.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "Three new routes a month. Save them. Drive them.", "items": ["3 routes / month", "Drive recording", "Save favourites"], "cta": "Download free"},
        {"name": "Plus — Annual", "featured": True, "tag": "Best value", "price": "£24.99", "per": "/ year", "strike": "£47.88 if billed monthly", "blurb": "Unlimited routes, unlimited drives, full telemetry. The proper kit.", "items": ["Unlimited route generation", "Full drive history", "Advanced telemetry", "Offline maps", "Priority support"], "cta": "Start 7-day free trial"},
        {"name": "Plus — Monthly", "price": "£3.99", "per": "/ month", "blurb": "Same Plus features, billed month to month.", "items": ["Unlimited route generation", "Full drive history", "Cancel anytime"], "cta": "Go monthly"},
    ],
    "why_eyebrow": "Why bother",
    "why_head_pre": "The road is half the car.",
    "why_head_accent": "ApexRoute makes the half worth chasing.",
    "why_lead": "Most maps optimise for arriving. ApexRoute optimises for the drive — the corners, the rhythm, the road that makes you stop the playlist and just listen to the engine.",
    "why_body": "Three years in, our routes have been driven across the UK, the Alps, the Dolomites, Big Sur, and the Tail of the Dragon. The algorithm gets sharper every drive.",
    "stats": [("100%", "grad", "Route choices controlled by you — no sponsored detours, no hidden cost."),
              ("<30s", "mint", "From input to a brand-new route. Faster than checking your phone at lights."),
              ("Offline", "yellow", "Maps download once. Your drive doesn't depend on cellular signal.")],
    "faq": [
        ("Is this a sat-nav replacement?", "For commuting, no — Maps wins on traffic. For weekend drives, yes. ApexRoute is built around the kind of road you'd take a longer way to find."),
        ("Does it work in [country]?", "If your country has real road data we cover it: UK, Ireland, France, Germany, Switzerland, Italy, Spain, Austria, Netherlands, Belgium, Norway, Sweden, plus the US, Canada, Australia, and New Zealand."),
        ("Is recording my drive safe?", "Recording happens on your phone. Telemetry stays private until you choose to share. You can delete any drive in one tap."),
        ("What about traffic, road closures, fuel?", "Plus shows live traffic on your route plus fuel stops and rest points. We surface what matters; we don't drown you in clutter."),
        ("Can I import a route I made elsewhere?", "Yes — GPX import is supported. Drive it, rate it, get your telemetry alongside it."),
        ("Is this safe to use while driving?", "Heads-up navigation is voice + glanceable visuals only. We won't bury anything important behind a tap. Eyes on the road, always."),
        ("How do I cancel?", "Cancel any time in your phone's subscription settings — Apple ID or Google Play. We don't pull dark patterns."),
    ],
    "final_title": "Drive better.",
    "final_body": "Free to download. Free to try. iPhone and Android. Your next great road is one tap away.",
    "footer_blurb": "Driving routes built for enthusiasts, not commuters. Made in the UK by Froggy Eye Ltd.",
}

# ---------------- BlipBlobb ----------------
BLIPBLOBB = {
    "folder": "blipblobb",
    "name": "BlipBlobb",
    "tagline": "Group chats. No internet required.",
    "meta_desc": "BlipBlobb creates instant local chats over WiFi. No accounts, no servers, no signal. Conferences, festivals, classrooms — stay in sync with the room.",
    "theme": THEMES["ocean"],
    "nav_examples": "Use cases",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Group chats that work",
    "headline_accent": "even when the internet doesn't.",
    "lead": "BlipBlobb creates instant local chats over WiFi — no signups, no servers, no signal. Open the app, join the room, talk to everyone in it.",
    "meta_items": ["Made for events", "Zero data collection", "Works offline"],
    "phone_content": '''        <h4>Local rooms</h4>
        <div class="phone-art"><div class="emoji">📡</div></div>
        <div>
          <p class="phone-title">FogCon · Sat Hall A</p>
          <p class="phone-sub">62 nearby · 4 active threads</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>WIFI</span><span>62 PEERS</span></div>
        <div class="phone-controls">
          <span class="ic">💬</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">📎</span>
        </div>
        <div class="phone-lyric"><b>Mira:</b> queue moved, panel starts in 4<br><b>Dev:</b> save me a seat ❤️</div>''',
    "chips": ["🎤 Conferences", "🎉 Festivals", "💍 Weddings", "🏫 Classrooms", "🚌 Tour groups", "🏕️ Campsites", "🚢 Cruises", "✈️ In-flight", "🏟️ Stadiums", "🏔️ Off-grid"],
    "how_head_pre": "Three taps in.",
    "how_head_accent": "Talking to the room.",
    "how_lead": "No signup. No phone number. No QR codes. Open the app and you're discovered by everyone on the same WiFi.",
    "steps": [
        ("Open BlipBlobb", "Pick a name. Pick a colour. That's the entire setup. Takes about ten seconds."),
        ("Join a room", "Anyone on your WiFi shows up automatically. Or hit Create Room and share a passcode for privacy."),
        ("Chat without limits", "Text, voice notes, photos, files. No cellular, no servers, no someone-else's-cloud."),
    ],
    "feat_head_pre": "Built for the room.",
    "feat_head_line2": "Not the cloud.",
    "features": [
        (ICON["wifi"], "Local-first messaging", "Messages travel device-to-device over the WiFi you're already on. No relay servers, no dependency."),
        (ICON["lock"], "No accounts, ever", "No phone number. No email. No login. Your name lasts as long as the chat does."),
        (ICON["users"], "Auto-discover peers", "Anyone on the same WiFi appears in the room list. Ad-hoc social network on demand."),
        (ICON["share"], "Files & voice notes", "Send photos, voice notes, and documents at WiFi speed. No upload bar, no '0%'."),
        (ICON["shield"], "Encrypted in transit", "Private rooms are end-to-end encrypted. Even if someone's snooping the network, they're snooping noise."),
        (ICON["zap"], "No bandwidth waste", "Messages stay local — nothing goes to the wider internet. Perfect when the venue WiFi is on its knees."),
    ],
    "ex_eyebrow": "Where it shines",
    "ex_head": "Made for these moments:",
    "ex_lead": "BlipBlobb is the chat for situations regular messengers were never built for — places where signal is poor, formal apps fail, and you just need to talk to whoever's nearby.",
    "examples": [
        ("#00D4FF,#3B82F6", "🎤", "Conference floor", "FogCon · 1,200 attendees"),
        ("#5EEAD4,#0087B3", "🎉", "Festival camp", "Glasto · 3 nearby tents"),
        ("#FACC15,#D97706", "💍", "Wedding venue", "Reception · 80 guests"),
        ("#A855F7,#5B21B6", "🏫", "Year 10 trip", "Mr. Davies' class · 28 students"),
        ("#FB7185,#9F1239", "🚌", "Coach tour", "Day 3 Italy · 42 travellers"),
        ("#34D399,#059669", "🏕️", "Campsite", "Lake Coniston · 6 vans"),
        ("#FBBF24,#A16207", "🚢", "Cruise deck", "Aurora-A · poker night"),
        ("#22D3EE,#0E7490", "🏔️", "Off-grid hut", "Lake hut · no signal at all"),
    ],
    "pricing_lead": "Free for casual chat. Plus is for organisers who need bigger rooms and history.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "Up to 12 people in a room. The chat that just works.", "items": ["Rooms up to 12", "Text, voice, photos", "Auto-discover peers", "Forever free"], "cta": "Download free"},
        {"name": "Plus — Annual", "featured": True, "tag": "For organisers", "price": "£12.99", "per": "/ year", "strike": "£23.88 if billed monthly", "blurb": "Run real events. Save the conversation. Brand the room.", "items": ["Rooms up to 500 people", "Persistent chat history", "Custom event branding", "Pinned messages", "Priority support"], "cta": "Start 7-day free trial"},
        {"name": "Plus — Monthly", "price": "£1.99", "per": "/ month", "blurb": "Same Plus features, billed monthly. Cancel any time.", "items": ["Rooms up to 500 people", "Persistent history", "Custom branding"], "cta": "Go monthly"},
    ],
    "why_eyebrow": "Why local",
    "why_head_pre": "The wider internet isn't always there.",
    "why_head_accent": "The room always is.",
    "why_lead": "Cloud chat fails the moment signal does — at festivals, on coaches, in basements, mid-flight, in any venue with overloaded WiFi. BlipBlobb cuts the cloud out entirely.",
    "why_body": "Your conversation lives on the devices in the room and nowhere else. Faster, more private, more reliable when it counts.",
    "stats": [("0", "grad", "Servers your messages touch. The chat is the network."),
              ("~10s", "mint", "From open-app to chatting. Pick a name and you're in."),
              ("End-to-end", "yellow", "Encryption on private rooms. The venue WiFi can't read what you send.")],
    "faq": [
        ("Does it really work without internet?", "Yes — as long as devices are on the same WiFi network or hotspot. The internet is only used optionally for software updates."),
        ("Do I need to make an account?", "Never. Pick a display name, you're in. Nothing about you is stored on our servers — because there are no servers."),
        ("How big can a room get?", "Free rooms up to 12 people. Plus rooms up to 500. Beyond that, message us — we can support festival-scale rooms."),
        ("What if my WiFi is locked down?", "BlipBlobb works on any open or password-protected WiFi as long as you're on it. If client isolation is on, we fall back to phone-to-phone Bluetooth."),
        ("Is it actually private?", "Yes. Private rooms are end-to-end encrypted. We don't see your messages because they don't touch our infrastructure."),
        ("Will my battery die?", "BlipBlobb uses peer discovery sparingly. A typical day in a busy room is about 3–5% battery."),
        ("Can I use it for sensitive things?", "Plus has end-to-end encryption and pinned messages, but BlipBlobb isn't a Signal replacement. For anything genuinely confidential, use a dedicated secure messenger."),
    ],
    "final_title": "Talk to the room.",
    "final_body": "Free to download. Free to use. iPhone and Android. Open it, you're in.",
    "footer_blurb": "Local group chat that works without signal. Built for events, festivals, classrooms, and anywhere the internet gives up.",
}

# ---------------- DoorDigest ----------------
DOORDIGEST = {
    "folder": "doordigest",
    "name": "DoorDigest",
    "tagline": "AI summaries of every doorbell event.",
    "meta_desc": "DoorDigest reads your Ring doorbell events and writes you a clear daily summary — so you know exactly what happened at your door without scrubbing footage.",
    "theme": THEMES["purple_dawn"],
    "nav_examples": "Examples",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Stop scrubbing doorbell footage.",
    "headline_accent": "Read the digest.",
    "lead": "DoorDigest watches your Ring events, picks out what mattered, and sends you a clear, written summary every day. Less paranoia, less footage, more peace of mind.",
    "meta_items": ["Works with Ring", "AI does the watching", "You get the headlines"],
    "phone_content": '''        <h4>Today's digest</h4>
        <div class="phone-art"><div class="emoji">🚪</div></div>
        <div>
          <p class="phone-title">14 events · 3 worth knowing</p>
          <p class="phone-sub">Tuesday · Front door</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>QUIET DAY</span><span>3 ALERTS</span></div>
        <div class="phone-controls">
          <span class="ic">📅</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">📨</span>
        </div>
        <div class="phone-lyric"><b>09:14</b> · Amazon delivery · package left in porch<br><b>14:02</b> · Postwoman · letters posted, no parcel</div>''',
    "chips": ["📦 Deliveries", "👥 Visitors", "🐈 Cats", "🚗 Cars", "🚶 Walkers", "🌧️ Weather", "🌙 Late-night", "📨 Mail", "🐕 Dogs", "🚨 Suspicious"],
    "how_head_pre": "Connect once.",
    "how_head_accent": "Get your day, summarised.",
    "how_lead": "We do the watching. You read a clean summary on your terms — daily, weekly, or only when something actually matters.",
    "steps": [
        ("Connect Ring", "One-tap login to your Ring account. We pull events securely and respect your existing subscriptions and recordings."),
        ("AI watches the events", "Every clip is analysed: people, packages, vehicles, animals, time of day, length of stay. The boring 99% gets summarised; the interesting 1% gets flagged."),
        ("You get the headlines", "Daily digest in plain English. Optional smart alerts the moment something unusual happens. Search history any time."),
    ],
    "feat_head_pre": "Less scrubbing.",
    "feat_head_line2": "More knowing.",
    "features": [
        (ICON["ai"], "Plain-English summaries", "Each event gets a one-line description. 'Amazon driver, 4s on porch, package left.' That's it."),
        (ICON["bell"], "Smart alerts only", "We alert on what's odd: late-night activity, repeat strangers, missing-package patterns. Not on every cat."),
        (ICON["search"], "Search your door history", "'When did the postwoman come last week?' Type it. Get the moment. Open the clip."),
        (ICON["camera"], "Multi-camera friendly", "Front door, side gate, garage. DoorDigest summarises across all of them in one digest."),
        (ICON["shield"], "Privacy by default", "Footage stays on Ring. We process metadata and a thumbnail strip — never long-term recordings."),
        (ICON["library"], "Weekly review", "Sundays you get a clean weekly recap: total events, anomalies, packages received, repeat visitors."),
    ],
    "ex_eyebrow": "Real digests",
    "ex_head": "Sounds like:",
    "ex_lead": "Examples of how DoorDigest writes up a typical day at the door — calm, useful, and never alarmist for the sake of it.",
    "examples": [
        ("#A855F7,#5B21B6", "📦", "Tuesday — 14 events", "Mostly post & deliveries"),
        ("#67E8F9,#0E7490", "🐈", "Wednesday — 6 events", "Quiet · neighbour's cat ×3"),
        ("#FACC15,#A16207", "🚨", "Friday — 22 events", "Late-night repeat visitor flagged"),
        ("#A855F7,#FACC15", "🌧️", "Saturday — 3 events", "Storm · false motion ×many"),
        ("#FB7185,#9F1239", "👥", "Sunday — 11 events", "Family visit weekend"),
        ("#34D399,#059669", "📨", "Monday — 9 events", "Postie ran early today"),
        ("#22D3EE,#3B82F6", "🚗", "Holiday — 28 events", "Long away · all reviewed"),
        ("#FDE047,#D97706", "📅", "Weekly recap", "47 events · 4 worth knowing"),
    ],
    "pricing_lead": "Free trial on Pro. Pro is what makes it worth opening daily — but the basics genuinely work for one camera.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "One camera. Daily digest. The headlines.", "items": ["1 camera", "Daily digest", "Basic event tagging", "7-day history"], "cta": "Download free"},
        {"name": "Pro — Annual", "featured": True, "tag": "For households", "price": "£29.99", "per": "/ year", "strike": "£59.88 if billed monthly", "blurb": "Every camera, full history, smart alerts, search.", "items": ["Unlimited cameras", "Full history search", "Smart anomaly alerts", "Weekly recaps", "Priority processing"], "cta": "Start 7-day free trial"},
        {"name": "Pro — Monthly", "price": "£4.99", "per": "/ month", "blurb": "Same Pro features, billed monthly.", "items": ["Unlimited cameras", "Full history search", "Smart alerts"], "cta": "Go monthly"},
    ],
    "why_eyebrow": "Why a digest",
    "why_head_pre": "Doorbell apps were built to grab your attention.",
    "why_head_accent": "DoorDigest gives it back.",
    "why_lead": "Most camera apps poke you for every twitch — every neighbour's cat, every car turning around, every leaf blowing past. The result isn't more security; it's banner-ad fatigue.",
    "why_body": "DoorDigest takes the firehose, sips it, and tells you what's there. The only alerts that survive are the ones you'd genuinely want at 11pm.",
    "stats": [("90%+", "grad", "Of doorbell events most homes don't actually need to see in real time."),
              ("~30s", "mint", "Average time to read your daily digest. Replaces 10 minutes of scrubbing."),
              ("Privacy-first", "yellow", "Footage stays on Ring. We process metadata and a small preview strip.")],
    "faq": [
        ("Does this replace Ring?", "No — Ring keeps the cameras and footage. DoorDigest sits on top, watches what comes in, and writes the summary you actually read."),
        ("Do you have my video?", "Only thumbnails and metadata, briefly, to generate the digest. Long-term footage stays on Ring's servers."),
        ("Will I miss a real emergency?", "Smart alerts fire in real time on suspicious activity (late-night visitors, package thefts, repeated unknowns). Everything else is in the digest."),
        ("Is it accurate?", "We get the obvious right (deliveries, post, family) reliably. Edge cases get flagged for your review rather than guessed at."),
        ("How many cameras can I connect?", "Free: one. Pro: as many as your Ring account has."),
        ("Cancel any time?", "Yes — through your phone's subscription settings. Your digests stay accessible until your billing period ends."),
        ("Does it work with cameras other than Ring?", "Ring first — Nest and Eufy support is in beta for Pro users. Tell us your setup and we'll prioritise."),
    ],
    "final_title": "Read your day.",
    "final_body": "Free to download. iPhone and Android. Connect Ring once and stop scrubbing footage forever.",
    "footer_blurb": "AI summaries of every doorbell event so you know what happened at your door without scrubbing footage. Made in the UK.",
}

# ---------------- Eight Ball Wisdom ----------------
EIGHTBALL = {
    "folder": "eightball",
    "name": "Eight Ball Wisdom",
    "tagline": "Ask. Shake. Believe.",
    "meta_desc": "The classic Magic 8 Ball, beautifully reimagined. Real shake physics, cinematic animations, and 20 classic answers (with a few new twists).",
    "theme": THEMES["mystic"],
    "nav_examples": "Themes",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Ask anything.",
    "headline_accent": "The ball already knows.",
    "lead": "The classic Magic 8 Ball, reimagined for the phone era. Real shake physics. Stunning animations. The same 20 cosmic answers, plus a few mischievous new ones.",
    "meta_items": ["Real shake physics", "Cinematic animations", "Premium themes"],
    "phone_content": '''        <h4>Ask the ball</h4>
        <div class="phone-art"><div class="emoji">🎱</div></div>
        <div>
          <p class="phone-title">"It is decidedly so."</p>
          <p class="phone-sub">The ball has spoken.</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>SHAKE TO ASK</span><span>20 ANSWERS</span></div>
        <div class="phone-controls">
          <span class="ic">↻</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">📜</span>
        </div>
        <div class="phone-lyric"><b>Q:</b> Should I text them first?<br><b>A:</b> "It is decidedly so." ✨</div>''',
    "chips": ["✨ Classic", "🌌 Cosmic", "💎 Crystal", "🌃 Neon", "🌹 Velvet", "🔮 Mystic", "🪐 Galaxy", "❄️ Frost", "🔥 Inferno", "🌸 Bloom"],
    "how_head_pre": "Ask. Shake.",
    "how_head_accent": "Believe (or don't).",
    "how_lead": "The same ritual that ate up your friend's bedroom in 1995, except now it lives in your pocket and looks like cinema.",
    "steps": [
        ("Hold the question", "Type it, say it, or just think it really hard. The ball doesn't judge. The ball is busy."),
        ("Shake the phone", "Real accelerometer-based shake. Tilt it. Flick it. Bash it dramatically. The ink swirls accordingly."),
        ("Read the answer", "Twenty classic responses rise from the inky depths in cinematic detail. Reroll if you don't like the first one. We won't tell."),
    ],
    "feat_head_pre": "It looks unreasonable.",
    "feat_head_line2": "It feels obscene. It's so much fun.",
    "features": [
        (ICON["sparkles"], "Real shake physics", "Accelerometer-driven motion. The ball, the ink, the bubbles all behave like the real thing — but better."),
        (ICON["video"], "Cinematic animations", "Watch the answer rise from depths in slow, satisfying focus. We tuned every frame."),
        (ICON["library"], "20 classic answers", "All the originals — 'Most Likely', 'Don't Count On It', 'Ask Again Later'. Plus a few additions only Eight Ball Wisdom knows."),
        (ICON["sparkles"], "Premium themes", "Switch from classic black to crystal, cosmic, neon, velvet, frost. Same wisdom; different wardrobe."),
        (ICON["bell"], "Quick-decide widget", "Home screen widget. One tap. One answer. For when you don't even have time to open the app."),
        (ICON["lock"], "Question history", "Re-read your past questions and what fate said. Some patterns are surprisingly accurate. Or terrifying."),
    ],
    "ex_eyebrow": "Themed balls",
    "ex_head": "Same wisdom. Different vibe.",
    "ex_lead": "Eight Ball Wisdom ships with one classic theme. Plus unlocks the lot.",
    "examples": [
        ("#1E1B4B,#A855F7", "🎱", "Classic Black", "The original"),
        ("#67E8F9,#A78BFA", "💎", "Crystal", "Translucent, refracts light"),
        ("#A855F7,#FF2E7E", "🌌", "Cosmic", "Stars swirl in the ink"),
        ("#FF2E7E,#FACC15", "🌃", "Neon", "Tokyo at 3am"),
        ("#FB7185,#7C3AED", "🌹", "Velvet", "Deep, plush, royal"),
        ("#22D3EE,#0E7490", "❄️", "Frost", "Icy, crisp, mountain-lake"),
        ("#FACC15,#FF4D2E", "🔥", "Inferno", "Lava in the answer well"),
        ("#FB7185,#FACC15", "🌸", "Bloom", "Petals drift around the orb"),
    ],
    "pricing_lead": "Free with the classic ball. One Plus unlock removes ads forever and opens the rest of the cosmos.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "Classic theme. 20 answers. The full ritual.", "items": ["Classic black ball", "All 20 answers", "Real shake physics", "Question history (last 20)"], "cta": "Download free"},
        {"name": "Plus — Forever", "featured": True, "tag": "One time", "price": "£3.99", "per": "once", "blurb": "Pay once. Unlock everything. No subscription.", "items": ["Ad-free forever", "All 9 premium themes", "Custom answer packs", "Unlimited history", "Home-screen widget", "Haptic feedback engine"], "cta": "Unlock Plus"},
        {"name": "Theme Pack", "price": "£0.99", "per": "per pack", "blurb": "Just want one theme? Buy it on its own.", "items": ["Single themed ball", "Lifetime use", "No subscription"], "cta": "Browse themes"},
    ],
    "why_eyebrow": "Why a Magic 8 Ball",
    "why_head_pre": "Sometimes you don't want advice.",
    "why_head_accent": "You want the dice rolled for you.",
    "why_lead": "There's a reason the original sold over a billion units. The Magic 8 Ball isn't fortune-telling; it's a tiny ritual that lets you off the hook of having to choose.",
    "why_body": "Should you text first? Pizza or curry? Take the job or wait? Sometimes the answer doesn't matter half as much as just deciding. The ball decides for you. Then you find out how you feel about it.",
    "stats": [("20", "grad", "Classic answers, all hand-balanced. 10 yes, 5 no, 5 'ask again later' — like the original."),
              ("9", "mint", "Hand-crafted ball themes in Plus. From Crystal to Inferno to Bloom."),
              ("0", "yellow", "Subscriptions. Plus is one one-time payment. Fair's fair.")],
    "faq": [
        ("Is this just the Magic 8 Ball app?", "It's the Magic 8 Ball app done properly. Real physics, beautiful art, no ad-stuffing. The version we wanted to exist."),
        ("Why pay for a Magic 8 Ball?", "You don't have to — the free version is genuinely complete. Plus exists if you want all the themes and you'd rather pay once than see ads."),
        ("Does it actually predict the future?", "It actually does not. Probability says it'll be right slightly under 50% of the time. The fun is in the ritual, not the result."),
        ("Can my kids use it?", "Yes — no inappropriate answers, no scary themes, rated 4+/Everyone. Bedtime questions encouraged."),
        ("Does it work offline?", "Always. Shake works on a plane, in a tent, on the moon."),
        ("Will I get pestered with notifications?", "Never. Eight Ball Wisdom doesn't push notifications. The ball waits for you."),
        ("Refund if I don't like it?", "Plus is one cheap one-off. If you want a refund within 14 days, message us — done, no fuss."),
    ],
    "final_title": "Shake it.",
    "final_body": "Free to download. iPhone and Android. The ball is waiting.",
    "footer_blurb": "The Magic 8 Ball, reimagined. Real shake physics, cinematic answers, beautifully crafted. Made in the UK.",
}

for app in [APEXROUTE, BLIPBLOBB, DOORDIGEST, EIGHTBALL]:
    out, sz = render_app(app)
    print(f"Wrote {out}  ({sz:,} bytes)")
