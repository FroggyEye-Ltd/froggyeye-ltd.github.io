#!/usr/bin/env python3
"""Batch 4 (final): solarwise, tileverse, treasurehunterlive, wheelofchoices, byebyejob."""
import sys
sys.path.insert(0, "/tmp")
from promo_engine import render_app, THEMES
from apps_batch1 import ICON

SOLARWISE = {
    "folder": "solarwise", "name": "SolarWise",
    "tagline": "Smart solar panel calculator.",
    "meta_desc": "SolarWise uses real NASA data, your tariffs, and engineering models to tell you exactly what solar will save you — before you spend a penny on installers.",
    "theme": THEMES["solar"],
    "nav_examples": "Reports",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Should you go solar?",
    "headline_accent": "Find out in 30 seconds.",
    "lead": "SolarWise uses real NASA solar data, your local electricity tariffs, and full engineering models to tell you exactly how much you'll save — before you spend a penny on installers.",
    "meta_items": ["Real NASA data", "No installer spin", "Honest payback periods"],
    "phone_content": '''        <h4>Your solar quote</h4>
        <div class="phone-art"><div class="emoji">☀️</div></div>
        <div>
          <p class="phone-title">Payback in 7.4 years</p>
          <p class="phone-sub">5.6 kWp · 10 kWh battery · SE roof</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>£8,420 SAVED · 25Y</span><span>VS £6,200 INSTALL</span></div>
        <div class="phone-controls">
          <span class="ic">📊</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">📤</span>
        </div>
        <div class="phone-lyric"><b>Yr 1 generation:</b> 5,128 kWh<br><b>Self-consumption:</b> 71% with battery · feed-in: 29%</div>''',
    "chips": ["☀️ Roof check", "🔋 Battery sizing", "💷 Tariff aware", "🛰 NASA data", "🌍 UK & EU", "📈 25-yr forecast", "🏠 Property report", "⚡ Self-consumption", "🌧 Weather model", "📋 Installer quote"],
    "how_head_pre": "Tell us about your roof.",
    "how_head_accent": "We tell you the truth.",
    "how_lead": "Real engineering models, real solar data, real tariffs. No installer optimism, no salesperson tricks. The number you get is the number you'll get.",
    "steps": [
        ("Describe your house", "Postcode, roof orientation, shading, electricity usage. We pull real solar irradiance from NASA for your exact location."),
        ("Get a real quote", "System size, battery sizing, expected generation, self-consumption rate, payback period, lifetime savings. Year-by-year forecast included."),
        ("Compare installer quotes", "Pro generates a PDF you can take to installers. The numbers are yours; the installers have to match them."),
    ],
    "feat_head_pre": "Designed by an engineer.",
    "feat_head_line2": "Built by a homeowner.",
    "features": [
        (ICON["compass"], "Real NASA solar data", "Solar irradiance pulled from satellite-derived datasets for your exact coordinates. Not a national average."),
        (ICON["zap"], "Battery sizing recommendations", "Should you add storage? How many kWh? We answer based on usage profile, tariff, and electricity price trajectory."),
        (ICON["library"], "25-year financial forecast", "Year-by-year energy generation, savings, payback, and lifetime ROI. With degradation accounted for."),
        (ICON["map"], "Region-aware tariffs", "Smart Export Guarantee, Octopus Agile, Economy 7 — UK tariffs modelled accurately. Plus EU FiT schemes."),
        (ICON["check"], "Honest payback periods", "No vendor spin. Real numbers, properly conservative assumptions, transparent inputs you can edit."),
        (ICON["share"], "Installer-ready PDF", "Pro generates a quote-comparable PDF: kWp, panels, inverter, battery, expected output. Take it to three installers."),
    ],
    "ex_eyebrow": "Real properties",
    "ex_head": "Sample SolarWise reports:",
    "ex_lead": "Anonymised reports from real households across the UK and EU. Each one is honest about the upside — and the downside.",
    "examples": [
        ("#FBBF24,#A16207", "🏠", "3-bed semi · Surrey", "Payback 7.4y · save £8.4k"),
        ("#FACC15,#854D0E", "🏡", "Detached · Yorkshire", "Payback 9.1y · save £6.8k"),
        ("#FCD34D,#854D0E", "🏘", "Terrace · Bristol", "Payback 11y · marginal"),
        ("#FBBF24,#9A3412", "🏰", "Cottage · Devon", "Payback 8.5y · battery key"),
        ("#FDE047,#A16207", "🏘", "End-terrace · Manchester", "Payback 10y · west roof"),
        ("#A855F7,#5B21B6", "🏚", "Listed · Lake District", "Not recommended (planning)"),
        ("#67E8F9,#0E7490", "🏖", "Coastal · Cornwall", "Payback 6.8y · best case"),
        ("#22D3EE,#0F766E", "🏔", "Highland · Scotland", "Payback 11.5y · marginal"),
    ],
    "pricing_lead": "Free quote with the essentials. Pro is for installer-comparable reports and detailed engineering output.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "One quote. Real numbers. Honest answer.", "items": ["1 property quote", "10-year forecast", "Basic battery sizing", "Standard inputs"], "cta": "Download free"},
        {"name": "Pro — One time", "featured": True, "tag": "Pay once", "price": "£12.99", "per": "once", "blurb": "Full engineering report. PDF for installers. Multi-property. No subscription.", "items": ["Unlimited property quotes", "25-year financial forecast", "Installer-ready PDF report", "Advanced battery modelling", "Multi-property comparison"], "cta": "Unlock Pro"},
        {"name": "Annual support", "price": "£9.99", "per": "/ year", "blurb": "Pro plus annual tariff & data updates.", "items": ["All Pro features", "Yearly tariff updates", "New scheme support", "Priority email support"], "cta": "Go annual"},
    ],
    "why_eyebrow": "Why this exists",
    "why_head_pre": "Most solar quotes are designed",
    "why_head_accent": "to make a sale.",
    "why_lead": "Installer estimates are notorious for overpromising — perfect roof angle, top-tier panels, generous self-consumption assumptions, and a payback period that conveniently lands at exactly 'manageable'. SolarWise has no axe to grind.",
    "why_body": "Built by a homeowner who burned through three vendor quotes before realising none of them used the same assumptions. SolarWise standardises the maths and makes it boring (which is what you want when spending £8,000).",
    "stats": [("NASA", "grad", "Solar irradiance data, location-specific. Better than any installer's spreadsheet."),
              ("£0", "mint", "Affiliate kickbacks, vendor sponsorships, hidden fees. We don't sell your enquiries."),
              ("Yours", "yellow", "Inputs. Edit any assumption — we show our working. The numbers are reproducible.")],
    "faq": [
        ("How accurate are the numbers?", "Within ±10% on payback periods for typical UK homes — comparable to MCS-certified surveys. Inputs you give matter; the more accurate they are, the better the answer."),
        ("Do you sell my data to installers?", "No. SolarWise has no installer affiliations, no lead-generation revenue, and no sponsorships. We make money from Pro upgrades — that's it."),
        ("Does it work outside the UK?", "Today: UK and major EU markets (Germany, France, Spain, Italy, Netherlands). The US is in beta. Australia is on the roadmap."),
        ("Can it tell me what panels to buy?", "Pro recommends typical panel and inverter combinations matched to your system size. We don't push specific brands — you choose."),
        ("What about half-shaded roofs?", "We model shading impact using your description (or a satellite check on Pro). The result is realistic — not the 'optimal' result installers tend to quote."),
        ("Will my quote stay valid?", "Tariffs and incentives change. Pro updates your report annually so it stays current. Free reports are accurate at the date they were generated."),
        ("Can I share the report with my partner / accountant?", "Yes — Pro generates a PDF designed exactly for sharing with whoever's signing off the spend."),
    ],
    "final_title": "Find out before you spend.",
    "final_body": "Free to download. iPhone and Android. Real numbers about a real decision in under a minute.",
    "footer_blurb": "Honest solar panel calculator with real NASA data, real tariffs, and zero installer spin. Made in the UK by a homeowner.",
}

TILEVERSE = {
    "folder": "tileverse", "name": "Tileverse",
    "tagline": "Claim the world, one tile at a time.",
    "meta_desc": "Claim digital tiles anywhere on Earth. Build a virtual empire on the real-world map. Compete with friends. Strategy meets the planet.",
    "theme": THEMES["tile"],
    "nav_examples": "Empires",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Own a piece",
    "headline_accent": "of the planet.",
    "lead": "Claim digital tiles anywhere on Earth — your hometown, holiday spots, famous landmarks, secret hideaways. Build a virtual empire on the real-world map. Trade. Compete. Conquer.",
    "meta_items": ["Live world map", "Multiplayer rivalry", "In-app economy"],
    "phone_content": '''        <h4>Your empire</h4>
        <div class="phone-art"><div class="emoji">🌍</div></div>
        <div>
          <p class="phone-title">142 tiles · Tier IV</p>
          <p class="phone-sub">North-West Empire · #82 globally</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>+12 THIS WEEK</span><span>RIVAL: SAGE</span></div>
        <div class="phone-controls">
          <span class="ic">⏪</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">⚔️</span>
        </div>
        <div class="phone-lyric"><b>Big Ben</b> contested · <b>Edinburgh Castle</b> yours<br><b>3 tiles</b> available next to your stronghold</div>''',
    "chips": ["🏰 Landmarks", "🌆 Cities", "🌊 Coastlines", "🏔 Mountains", "🌲 Forests", "🏖 Beaches", "🏟 Stadiums", "🎢 Theme parks", "🛬 Airports", "🏝 Islands"],
    "how_head_pre": "Pick a square.",
    "how_head_accent": "Build your empire.",
    "how_lead": "Every square metre of Earth is a claimable tile. Start small, expand strategically, fortify what matters. The whole world is the game board.",
    "steps": [
        ("Claim your first tile", "Anywhere on the planet — your bedroom, your school, the Eiffel Tower. The first one is yours, free."),
        ("Build outwards", "Cluster tiles into territories. Lock down landmarks. Grow your empire one square at a time."),
        ("Compete & trade", "Rival empires want what you've got. Fortify, ally, trade, or wage tile war. The leaderboard is the world."),
    ],
    "feat_head_pre": "A strategy game.",
    "feat_head_line2": "On a map of the real world.",
    "features": [
        (ICON["map"], "Live, real-world map", "Beautifully rendered planet — see claimed tiles, contested zones, and your territory grow in real time."),
        (ICON["zap"], "Strategic tile claiming", "Cluster tiles for bonuses. Lock down landmarks for prestige. Choke points matter — ask any general."),
        (ICON["users"], "Real multiplayer", "Real players, real competition. Form alliances or wage long campaigns over the regions you care about."),
        (ICON["library"], "In-app economy", "Earn, trade, and compound. Tiles you claim today might double in value next quarter — watch the market."),
        (ICON["sparkles"], "Premium empire flags", "Plus unlocks custom flag designs, empire colours, and territorial banners. Look the part."),
        (ICON["compass"], "Daily quests", "New objectives every day — claim a coastline, take a landmark, build a 12-tile cluster. Steady progress without grinding."),
    ],
    "ex_eyebrow": "Empires we've seen",
    "ex_head": "What people are claiming:",
    "ex_lead": "Anonymised top empires from the global Tileverse leaderboard. From single-village fortifications to landmark-only minimalists.",
    "examples": [
        ("#0EA5E9,#0369A1", "🏰", "Landmark Hunter", "All UK landmarks · Tier VII"),
        ("#22D3EE,#0E7490", "🌆", "London Lord", "C1–C2 saturation · Tier VI"),
        ("#5EEAD4,#0F766E", "🌊", "Coastline Empire", "From Land's End to Dover"),
        ("#A855F7,#5B21B6", "🏔", "Highland Crown", "Scottish peaks specialist"),
        ("#FACC15,#A16207", "🏟", "Stadium Hunter", "Every Premier League ground"),
        ("#FB7185,#9F1239", "🎢", "Theme Park Tycoon", "Disney + Universal complete"),
        ("#34D399,#047857", "🌲", "Forest King", "Black Forest dominance"),
        ("#3DF5B0,#0F766E", "🏝 ", "Island Collector", "All UK isles"),
    ],
    "pricing_lead": "Free to play, with real strategy. Plus is for serious players who want bigger empires and faster growth.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "Up to 100 tiles. Full strategy. The whole world to play on.", "items": ["Up to 100 tiles", "Standard tile generation", "Empire flags (basic)", "Daily quests"], "cta": "Download free"},
        {"name": "Plus — Annual", "featured": True, "tag": "For empire builders", "price": "£14.99", "per": "/ year", "strike": "£35.88 if billed monthly", "blurb": "Bigger empires, faster claiming, exclusive flags, leaderboard recognition.", "items": ["Up to 5,000 tiles", "Faster tile generation", "Premium empire flags & themes", "Exclusive leaderboard recognition", "Priority server support"], "cta": "Start 7-day free trial"},
        {"name": "Plus — Monthly", "price": "£2.99", "per": "/ month", "blurb": "Same Plus features, billed monthly.", "items": ["5,000 tiles", "All Plus features", "Cancel anytime"], "cta": "Go monthly"},
    ],
    "why_eyebrow": "Why a world game",
    "why_head_pre": "Most strategy games invent a fake map.",
    "why_head_accent": "We use the one you already know.",
    "why_lead": "Risk has six continents. Civilization has tile-based fantasy. Tileverse has Earth — every street, every coastline, every landmark you care about. Familiar enough to be personal. Big enough to never run out.",
    "why_body": "Tiles aren't ownership of real property — they're digital claims on a digital map. But the satisfaction of holding your home town in tier-VII fortifications? That's real.",
    "stats": [("510 trillion", "grad", "Tiles on the planet (1m² each). You will never run out of new ground to claim."),
              ("Real-time", "mint", "Multiplayer. See rival claims, alliances, and battles as they happen."),
              ("Digital", "yellow", "Tiles only. They are not real property and confer no real-world rights. The fun is in the game.")],
    "faq": [
        ("Is this real estate?", "No. Tileverse tiles are digital game assets. They do not represent ownership of real property and confer no real-world rights of any kind. It's a game."),
        ("Do I need to be in a place to claim it?", "No — claim anywhere on the planet from the comfort of your sofa. You don't need to physically visit Mount Everest to plant a flag on it."),
        ("How does the multiplayer work?", "Other real players see your claims and can challenge contested tiles. Alliances let you defend territory together. Wars are fun. Wars are also optional."),
        ("Can my friends and I play together?", "Absolutely — form alliances, share territories, defend each other's strongholds. The most successful empires are usually built together."),
        ("How does pricing work?", "Free to play with up to 100 tiles. Plus removes the limit (up to 5,000) and unlocks premium customisation."),
        ("Can I lose tiles I've claimed?", "In contested zones, yes — that's the strategy. Your stronghold tiles are protected once fortified."),
        ("Will the map ever fill up?", "510 trillion tiles. No."),
    ],
    "final_title": "Plant your flag.",
    "final_body": "Free to download. iPhone and Android. Pick a square. Build the empire.",
    "footer_blurb": "A real-world map strategy game where every square is up for grabs. Made in the UK by Froggy Eye Ltd.",
}

TREASUREHUNTERLIVE = {
    "folder": "treasurehunterlive", "name": "Treasure Hunter Live",
    "tagline": "Real adventures. Real places.",
    "meta_desc": "Treasure Hunter Live turns the world into a treasure map. GPS-driven hunts in your area. Create hunts for friends and family.",
    "theme": THEMES["treasure"],
    "nav_examples": "Hunts",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Real adventures hidden in the streets",
    "headline_accent": "you walk every day.",
    "lead": "Treasure Hunter Live turns the world into a treasure map. Hunt in your area, create hunts for friends and family, and rediscover the magic of going outside.",
    "meta_items": ["GPS-based", "Family-safe", "Create your own hunts"],
    "phone_content": '''        <h4>Active hunt</h4>
        <div class="phone-art"><div class="emoji">🗺️</div></div>
        <div>
          <p class="phone-title">The Riverwalk Mystery</p>
          <p class="phone-sub">Clue 3 of 7 · 240m to next</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>HUNT TIME 22:14</span><span>PRIZE: PIZZA</span></div>
        <div class="phone-controls">
          <span class="ic">📍</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">🧭</span>
        </div>
        <div class="phone-lyric"><b>Clue:</b> "Where the water meets the bridge of nine arches —<br>look up, count the swans, the next clue follows the eldest."</div>''',
    "chips": ["🎂 Birthdays", "👨‍👩‍👧 Family days", "💼 Team away-days", "💕 Date nights", "🎄 Christmas", "🏛 City tours", "🏖 Holiday hunts", "🏫 School trips", "🎓 University tours", "🎉 Hen parties"],
    "how_head_pre": "Open the map.",
    "how_head_accent": "Step outside.",
    "how_lead": "GPS-driven, story-rich treasure hunts that turn your neighbourhood (or anywhere you're travelling) into a place worth exploring on foot.",
    "steps": [
        ("Find a hunt nearby", "Browse community-created hunts in your area, or download a curated city tour. From 30 minutes to a whole afternoon."),
        ("Follow the clues", "GPS guides you toward each clue location. Solve riddles, decode photos, or simply find the marker. Family-safe pacing."),
        ("Claim the prize", "Hunts can end at a real prize (book a restaurant, a treat in the post, or a hidden cache). Or just at the joy of having gone outside."),
    ],
    "feat_head_pre": "An app that gets you",
    "feat_head_line2": "off your phone (almost).",
    "features": [
        (ICON["compass"], "GPS-based gameplay", "Real walks, real locations, real puzzles. The world becomes the playing field — phone is just the map."),
        (ICON["map"], "Hunt creator tool", "Drop clues at any GPS location. Add photos, riddles, or simple location markers. Build a story. Hide a prize."),
        (ICON["shield"], "Family-safe modes", "Tailored for kids: parental controls, age-appropriate clues, walking-distance constraints. Made for school trips and family days."),
        (ICON["users"], "Community hunts", "Hunts created by other players in your area. Discover your neighbourhood like a tourist — with someone else's clues."),
        (ICON["sparkles"], "Themed prize templates", "Pizza-night hunts, treasure-chest hunts, city-tour finals. Plus templates to make hunt-building effortless."),
        (ICON["library"], "Offline hunt support", "Pro hunts download fully — no signal? No problem. Perfect for rural treasure hunts and no-data school trips."),
    ],
    "ex_eyebrow": "Real hunts",
    "ex_head": "Hunts people have built and run:",
    "ex_lead": "A snapshot of community and curated hunts running across the UK and EU right now.",
    "examples": [
        ("#F59E0B,#A16207", "🎂", "10th Birthday Hunt", "Bristol · 1.2 mi · 8 clues"),
        ("#FBBF24,#854D0E", "💕", "First Anniversary", "Edinburgh · romantic walk"),
        ("#FACC15,#9A3412", "👨‍👩‍👧", "Sunday Family Day", "Lakes · 4-hr loop"),
        ("#FCD34D,#A16207", "🏛", "Ye Olde London", "City of London · history"),
        ("#FBBF24,#7C2D12", "💼", "Team Away-Day", "Manchester · 2hr build"),
        ("#FED7AA,#854D0E", "🎄", "Christmas Eve", "Bath · seasonal classics"),
        ("#FACC15,#FB923C", "🎓", "University Tour", "Oxford colleges"),
        ("#FBBF24,#FFE14D", "🎉", "Hen Party Hunt", "York · 8 stops · pubs included"),
    ],
    "pricing_lead": "Free for casual hunting. Plus is for hunt creators and offline-mode adventurers.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "Hunt nearby. Solve community hunts. The basics, for free.", "items": ["Browse community hunts", "1 hunt creation / month", "5 clues per hunt", "Standard prize templates"], "cta": "Download free"},
        {"name": "Plus — Annual", "featured": True, "tag": "For hunt-makers", "price": "£12.99", "per": "/ year", "strike": "£23.88 if billed monthly", "blurb": "Unlimited hunts, advanced clue mechanics, offline play, premium templates.", "items": ["Unlimited hunt creation", "Up to 50 clues per hunt", "Offline hunt support", "Advanced clue types (photo, audio, AR)", "Premium prize templates"], "cta": "Start 7-day free trial"},
        {"name": "Plus — Monthly", "price": "£1.99", "per": "/ month", "blurb": "Same Plus features, billed monthly.", "items": ["Unlimited hunts", "All Plus features", "Cancel anytime"], "cta": "Go monthly"},
    ],
    "why_eyebrow": "Why this matters",
    "why_head_pre": "Most apps want you to look at the screen.",
    "why_head_accent": "Treasure Hunter Live wants you to look up.",
    "why_lead": "Geocaching-style adventure has been around for decades, but the apps stayed clunky and the hunts looked like spreadsheets. Treasure Hunter Live is the version that actually feels like an adventure — for kids, for couples, for teams.",
    "why_body": "It's the app we kept reaching for at family birthdays, hen-do weekends, and away-days. So we built it. Now it's yours.",
    "stats": [("Outside", "grad", "The whole point. We measure success in steps taken, not minutes opened."),
              ("Family-safe", "mint", "Kid mode caps walking distances, vets clues, and lets parents review the whole route."),
              ("Yours", "yellow", "Hunts. Build them, share them privately, or publish to the community. You decide.")],
    "faq": [
        ("Is this safe for children?", "Yes — kid mode constrains walking distance, prohibits crossing major roads in the route, and lets parents review every clue before the hunt starts."),
        ("How accurate is the GPS?", "±5–10m typically. Clue radii are tunable so 'reach this spot' isn't frustratingly precise. Indoor venues use Bluetooth beacons (Plus)."),
        ("Can I make a hunt without writing it from scratch?", "Yes — Plus has hunt templates for birthdays, anniversaries, team away-days, city tours, and more. Drop your start/end points, we fill in the rest."),
        ("Will it work where I live?", "Anywhere with a map and walkable streets. We've had hunts run in 60+ countries. Truly remote locations may benefit from Plus offline mode."),
        ("Do I need data on the hunt?", "Free hunts need data. Plus hunts download fully — perfect for the countryside, the underground, or kids without their own data plan."),
        ("Can I hide real treasure?", "Sure — many users do. We don't manage physical prizes; the hunt simply ends at a GPS point you choose. Real chest, real gift, real high-five."),
        ("Is it just for kids?", "Definitely not. Adult hunts (date nights, hen-dos, team-builds, pub crawls) are some of the most active categories."),
    ],
    "final_title": "Step outside.",
    "final_body": "Free to download. iPhone and Android. The world is the map. Today is the day.",
    "footer_blurb": "Real-world treasure hunts for families, teams, and curious adults. Made in the UK by Froggy Eye Ltd.",
}

WHEELOFCHOICES = {
    "folder": "wheelofchoices", "name": "Wheel of Choices",
    "tagline": "The cure for indecision.",
    "meta_desc": "Restaurants, movies, chores, dares. Wheel of Choices makes any decision instant. Add options, give it a spin, let chance do its thing.",
    "theme": THEMES["purple_dawn"],
    "nav_examples": "Wheels",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Stop debating.",
    "headline_accent": "Spin the wheel.",
    "lead": "Restaurants, movies, chores, dares. Wheel of Choices makes any decision instant. Add the options, give it a spin, let chance settle it. The fastest decision-maker on your phone.",
    "meta_items": ["Save unlimited wheels", "Themed presets", "Instant decisions"],
    "phone_content": '''        <h4>Tonight's wheel</h4>
        <div class="phone-art"><div class="emoji">🎡</div></div>
        <div>
          <p class="phone-title">Pizza · 23%</p>
          <p class="phone-sub">7 options · weighted</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>JUST SPUN</span><span>WINNER!</span></div>
        <div class="phone-controls">
          <span class="ic">↻</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">📤</span>
        </div>
        <div class="phone-lyric"><b>Saved wheel:</b> "Where shall we eat?"<br>7 places · last spun Tuesday · winner: Roma's.</div>''',
    "chips": ["🍕 Dinner", "🎬 Movie night", "🧹 Chores", "🎲 Dares", "✈️ Holiday", "🎁 Gift ideas", "💪 Workout", "🍷 Drinks", "🎤 Karaoke", "📚 Book club"],
    "how_head_pre": "Add the options.",
    "how_head_accent": "Hit spin. Live with it.",
    "how_lead": "Wheel of Choices isn't profound. It's just very, very good at the thing it does — turning a 30-minute argument into a 3-second decision.",
    "steps": [
        ("Add your options", "Type them in. Paste a list. Pick from a saved wheel. Add as many or as few as you like."),
        ("Spin", "A satisfying animation, a clean reveal, an answer you have to live with. (Or spin again. We don't tell.)"),
        ("Save the wheel", "Plus lets you save unlimited wheels — your 'Where shall we eat?' wheel is one tap away every Friday."),
    ],
    "feat_head_pre": "Built for the moment",
    "feat_head_line2": "you stop talking and just decide.",
    "features": [
        (ICON["sparkles"], "Custom options", "Add unlimited choices. Weight them if you want — heavier for the ones you secretly favour. We won't tell."),
        (ICON["library"], "Saved wheels", "Plus lets you save your favourite wheels. Restaurants, movies, weekly chores — all one tap away."),
        (ICON["check"], "Themed presets", "Pre-built wheels for date night, family meals, drinking games, gift ideas. Start with one, customise later."),
        (ICON["share"], "Share the result", "One tap sends the verdict to your group chat with a beautiful animated card. Settles arguments instantly."),
        (ICON["zap"], "Weighted spins", "Plus lets you bias the wheel towards specific options. For when you want fate, but with a thumb on the scale."),
        (ICON["shield"], "Ad-free spinning", "Plus removes all ads. The free version is plenty usable; Plus is for the people who run their lives through this app."),
    ],
    "ex_eyebrow": "Real wheels",
    "ex_head": "Wheels people actually run:",
    "ex_lead": "A taste of the wheels saved by Wheel of Choices users — the things life can't seem to make a call on without help.",
    "examples": [
        ("#A855F7,#5B21B6", "🍕", "Where shall we eat?", "7 local favourites"),
        ("#C084FC,#7E22CE", "🎬", "Friday film night", "Top 12 unwatched"),
        ("#67E8F9,#0E7490", "🧹", "Chore wheel", "Whose turn at the bins"),
        ("#FB7185,#9F1239", "🎲", "Truth or dare", "Dare prompts only"),
        ("#FACC15,#A16207", "✈️", "Next holiday", "5 destinations bookmarked"),
        ("#34D399,#059669", "💪", "Today's workout", "8-style randomiser"),
        ("#FBBF24,#D97706", "🍷", "Drink decisions", "Cocktail or beer"),
        ("#A78BFA,#5B21B6", "📚", "Book club pick", "12 unread on shelf"),
    ],
    "pricing_lead": "Free for the basics. Plus is for the people who run their week through Wheel of Choices.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "Spin anything. Up to 3 saved wheels.", "items": ["Unlimited spins", "Up to 3 saved wheels", "Standard themes", "Share results"], "cta": "Download free"},
        {"name": "Plus — Annual", "featured": True, "tag": "For decision avoiders", "price": "£8.99", "per": "/ year", "strike": "£17.88 if billed monthly", "blurb": "Unlimited saved wheels, weighted spins, premium themes, ad-free.", "items": ["Unlimited saved wheels", "Weighted probability spins", "Premium themes & sounds", "Ad-free forever", "Family Sharing"], "cta": "Start 7-day free trial"},
        {"name": "Plus — Monthly", "price": "£1.49", "per": "/ month", "blurb": "Same Plus features, billed monthly.", "items": ["Unlimited wheels", "All Plus features", "Cancel anytime"], "cta": "Go monthly"},
    ],
    "why_eyebrow": "Why a wheel",
    "why_head_pre": "The hardest part of choosing",
    "why_head_accent": "is just choosing.",
    "why_lead": "Most decisions don't deserve a 30-minute group chat. The pizza place, the film, whose turn at the dishes — the answer is fine, the dithering is the actual cost. Wheel of Choices gives you permission to just stop.",
    "why_body": "Spin it. Live with it. Find out you're actually relieved you didn't have to choose.",
    "stats": [("3 sec", "grad", "Average time from open to verdict on a saved wheel. Faster than the first 'I dunno'."),
              ("0", "mint", "Subscription nags. Plus is cheap. Free works. We don't pester you to upgrade."),
              ("Yours", "yellow", "Wheels. Saved locally and synced privately if you choose. We don't peek at your dinner choices.")],
    "faq": [
        ("Why does this exist as an app?", "Because website wheel-spinners are clunky, ad-stuffed, and don't save your wheels. Wheel of Choices is the version we always wanted on our phones."),
        ("Are the spins really random?", "Yes — properly random. Weighted spins on Plus let you bias the result, but unweighted is genuinely uniform across all options."),
        ("Can I share a wheel with my partner?", "Plus has Family Sharing — saved wheels sync across devices. Use the same wheels with your housemates, kids, or partner."),
        ("Does it work offline?", "Always. Wheel of Choices doesn't need the internet to spin a wheel."),
        ("Will I see ads in the free version?", "A small banner. Plus removes them entirely. We don't run interstitials, video ads, or rewarded ads."),
        ("Can I hide options?", "Yes — disable any option without removing it. Use it tonight; bring it back next week."),
        ("Is there a 'redo' button?", "Yes. We won't judge. Some decisions need two spins."),
    ],
    "final_title": "Stop debating.",
    "final_body": "Free to download. iPhone and Android. The wheel is waiting.",
    "footer_blurb": "The fastest decision-maker on your phone. Save your wheels. Settle the argument. Made in the UK.",
}

BYEBYEJOB = {
    "folder": "byebyejob", "name": "ByeByeJob",
    "tagline": "Redundancy and severance, sorted.",
    "meta_desc": "ByeByeJob is the calm, clear guide through redundancy and severance — built for the UK and US. Know your rights, claim what you're owed, plan what's next.",
    "theme": THEMES["teal_pro"],
    "nav_examples": "Steps",
    "hero_eyebrow": "Now on iOS & Android",
    "headline_pre": "Just been made redundant?",
    "headline_accent": "You're not on your own.",
    "lead": "ByeByeJob is the calm, clear guide through redundancy and severance — built for the UK and US. Know your rights, calculate what you're owed, and plan what's next. Without the legalese, without the panic.",
    "meta_items": ["UK & US guidance", "Severance calculator", "Step-by-step recovery"],
    "phone_content": '''        <h4>Your situation</h4>
        <div class="phone-art"><div class="emoji">⚖️</div></div>
        <div>
          <p class="phone-title">£8,420 owed</p>
          <p class="phone-sub">Statutory + notice + accrued holiday</p>
        </div>
        <div class="phone-scrub"></div>
        <div class="phone-times"><span>STEP 3 OF 7</span><span>SETTLEMENT REVIEW</span></div>
        <div class="phone-controls">
          <span class="ic">📋</span>
          <span class="play"><svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>
          <span class="ic">📤</span>
        </div>
        <div class="phone-lyric"><b>Up next:</b> review your settlement agreement<br><b>Watch for:</b> the post-employment restrictions clause.</div>''',
    "chips": ["⚖️ Rights", "💷 Severance", "📋 Settlement", "📑 References", "💼 CV refresh", "🤝 Networking", "🎯 Interview prep", "💰 Tax-free £30k", "📅 Notice period", "🧠 Mental health"],
    "how_head_pre": "Walk through it.",
    "how_head_accent": "One clear step at a time.",
    "how_lead": "From the redundancy meeting to your next role, ByeByeJob is the calm, ordered playbook. We don't rush you. We don't sell you anything you don't need. We just help.",
    "steps": [
        ("Tell us your situation", "UK or US, salary, length of service, notice period, age. We work out exactly what statutory pay, notice, and holiday you're owed."),
        ("Review the offer", "Settlement agreement on the table? We highlight what to query, what's normal, and what's actually below market. Not legal advice — but a sharp prompt list."),
        ("Plan your recovery", "CV refresh checklist, networking templates, interview prep, mental-health resources. The actual journey, mapped."),
    ],
    "feat_head_pre": "Calm guidance.",
    "feat_head_line2": "When you need it most.",
    "features": [
        (ICON["check"], "Country-specific rights", "UK statutory redundancy rules and US WARN/severance norms, explained without the legalese. Updated for 2026."),
        (ICON["library"], "Severance calculator", "Statutory pay, notice pay, accrued holiday, tax-free thresholds, contractual extras. Honest numbers in seconds."),
        (ICON["search"], "Settlement reviewer", "Plus reviews your settlement agreement and flags clauses that need attention — restrictions, references, payment timing."),
        (ICON["users"], "Job-search next steps", "CV refresh prompts, networking message templates, interview prep — adapted to your industry and seniority."),
        (ICON["shield"], "Mental health resources", "Curated, vetted resources for the emotional side of losing a job. Because that matters as much as the cheque."),
        (ICON["lock"], "Privacy-first", "Your salary, employer, and case details stay encrypted on your device. We never share, sell, or look at your data."),
    ],
    "ex_eyebrow": "Real cases",
    "ex_head": "Situations ByeByeJob actually handles:",
    "ex_lead": "Anonymised case studies from real users — including how ByeByeJob helped them spot what they were missing.",
    "examples": [
        ("#14B8A6,#0F766E", "⚖️", "12 years · UK manager", "Spotted £4,200 missed in calc"),
        ("#5EEAD4,#0F766E", "💷", "8 years · US engineer", "Negotiated 2 extra weeks"),
        ("#67E8F9,#0E7490", "📋", "Settlement review", "Restrictive covenant flagged"),
        ("#FACC15,#A16207", "💼", "CV refresh", "Two interviews in 10 days"),
        ("#A855F7,#5B21B6", "🤝", "Networking template", "Won 5 warm intros"),
        ("#FB7185,#9F1239", "🧠", "Mental health", "Free helpline numbers · UK"),
        ("#34D399,#059669", "💰", "Tax-free £30k", "Optimised PILON structure"),
        ("#FBBF24,#D97706", "📅", "Notice period", "Calculated correctly first time"),
    ],
    "pricing_lead": "Free for the essentials. Pro is for serious recovery — settlement reviews and 1:1 expert consultations.",
    "plans": [
        {"name": "Free", "price": "£0", "blurb": "Severance calculator. Rights guidance. Step-by-step plan.", "items": ["Severance calculator", "UK & US rights guide", "Recovery checklist", "Mental health resources"], "cta": "Download free"},
        {"name": "Pro — One time", "featured": True, "tag": "Pay once", "price": "£24.99", "per": "once", "blurb": "Unlimited calculations, settlement reviewer, and a 1:1 consultation with our redundancy expert.", "items": ["Unlimited severance calculations", "Settlement agreement reviewer", "Advanced rights guidance", "1:1 expert consultation", "Priority document review"], "cta": "Unlock Pro"},
        {"name": "Annual support", "price": "£14.99", "per": "/ year", "blurb": "Pro plus annual updates as employment law changes.", "items": ["All Pro features", "Annual rights updates", "Priority support", "Re-review on each new role"], "cta": "Go annual"},
    ],
    "why_eyebrow": "Why this exists",
    "why_head_pre": "Redundancy is bewildering.",
    "why_head_accent": "It shouldn't be.",
    "why_lead": "Most people get made redundant once, maybe twice in a career. They don't have time to learn employment law. Their employer's HR has done it a hundred times. The asymmetry is the problem.",
    "why_body": "ByeByeJob closes the gap. Plain-English rights, real numbers, a calm playbook. No charging you in your worst week — Pro is a one-time payment, not a subscription that runs while you're job-hunting.",
    "stats": [("£30k", "grad", "Tax-free threshold for UK redundancy payments. Most people don't structure around it correctly."),
              ("Days", "mint", "Recovery starts within. The longer you wait to plan, the longer the gap looks on the CV."),
              ("Yours", "yellow", "Data. Salary, employer, case — never shared, never sold, never looked at by us. Encrypted on device.")],
    "faq": [
        ("Is this legal advice?", "No — ByeByeJob is information and guidance, not legal advice. For complex cases (especially settlement disputes) we recommend consulting an employment solicitor. Pro includes a referral to vetted UK and US specialists."),
        ("Does it cover my country?", "UK and US in full. Ireland, Australia, and Canada in beta. Tell us your country and we'll prioritise."),
        ("Will my employer find out I'm using it?", "No. Everything happens on your device. We don't notify anyone, ever."),
        ("How accurate is the severance calculator?", "Within £50 of HMRC-published statutory amounts for UK cases. US is calibrated to federal WARN and common state-level rules; check your state."),
        ("What if my settlement offer is below market?", "Pro's settlement reviewer flags the things to negotiate on — and we have a 1:1 expert consultation included to walk you through it."),
        ("Is there ongoing support after Pro?", "Yes — Annual support keeps you covered for the next role too. Recurring redundancies (sadly common in some industries) are handled."),
        ("Cancel any time?", "Pro is a one-time payment, no subscription. Annual support cancels in your phone's subscription settings."),
    ],
    "final_title": "Take back the day.",
    "final_body": "Free to download. iPhone and Android. The first calculation is one tap away.",
    "footer_blurb": "Calm, clear guidance through redundancy and severance for the UK and US. Made in the UK by people who've been there.",
}

for app in [SOLARWISE, TILEVERSE, TREASUREHUNTERLIVE, WHEELOFCHOICES, BYEBYEJOB]:
    out, sz = render_app(app)
    print(f"Wrote {out}  ({sz:,} bytes)")
