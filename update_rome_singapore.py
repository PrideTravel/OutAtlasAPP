#!/usr/bin/env python3
import json, re

def find_toplevel_city_range(lines, city_key):
    start = None
    for i, line in enumerate(lines):
        if re.match(rf'^  "{re.escape(city_key)}"\s*:\s*\{{', line):
            start = i
            break
    if start is None:
        return None, None
    depth = 0
    for i in range(start, len(lines)):
        depth += lines[i].count('{') - lines[i].count('}')
        if depth == 0:
            return start, i
    return start, len(lines) - 1

def build_toplevel_city_lines(city_key, city_data):
    lines = []
    lines.append(f'  "{city_key}": {{')
    keys = list(city_data.keys())
    for i, k in enumerate(keys):
        v = city_data[k]
        comma = ',' if i < len(keys) - 1 else ''
        lines.append(f'    "{k}": {json.dumps(v, separators=(", ", ": "))}{comma}')
    lines.append('  }')
    return lines

rome_data = {
    "baseFare": [500, 1000],
    "hotels": [
        {"name": "First Hotel Roma", "type": "Luxury", "tags": ["World Rainbow Hotels Member"]},
        {"name": "Hotel Art by the Spanish Steps", "type": "Luxury", "tags": ["World Rainbow Hotels Member"]},
        {"name": "W Rome", "type": "Luxury", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "Hotel de Russie", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel Bernini Bristol", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel Splendide Royal", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel Indigo Rome - St. George", "type": "Mid-Priced", "tags": ["IGLTA Accredited"]},
        {"name": "Hotel Artemide", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "The Hoxton, Rome", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "IQ Hotel Roma", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel IQ Roma", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Generator Rome", "type": "Budget", "tags": ["LGBTQ Friendly"]},
        {"name": "The RomeHello", "type": "Budget", "tags": ["LGBTQ Friendly"]},
        {"name": "YellowSquare Rome", "type": "Budget", "tags": ["LGBTQ Friendly"]},
        {"name": "B&B Second Floor", "type": "Moderate", "tags": ["LGBTQ Owned", "Gay Street"]}
    ],
    "iata": "FCO",
    "image": "&#127470;&#127481;",
    "lgbtqDistrict": "Gay Street (Via di San Giovanni in Laterano)",
    "lgbtqSafety": "Italy: Generally safe in tourist areas. Gay Street near the Colosseum is the heart of Rome's queer scene.",
    "monthlyWeather": {
        "0": {"high": "54°F", "low": "38°F", "summary": "Cold and crisp; damp mornings.", "gear": "Heavy coat, scarf, waterproof boots."},
        "1": {"high": "55°F", "low": "38°F", "summary": "Chilly with frequent winter rain.", "gear": "Wool coat, windproof umbrella."},
        "2": {"high": "61°F", "low": "42°F", "summary": "Variable spring air; breezy and bright.", "gear": "Trench coat, layered sweaters."},
        "3": {"high": "66°F", "low": "47°F", "summary": "Mild and bright; blooming gardens.", "gear": "Light jacket, scarf, jeans."},
        "4": {"high": "73°F", "low": "52°F", "summary": "Pleasant and sunny; peak comfort.", "gear": "T-shirts, light cardigans."},
        "5": {"high": "81°F", "low": "59°F", "summary": "Hot and dry summer start.", "gear": "Linen clothes, sunglasses, sun hat."},
        "6": {"high": "88°F", "low": "65°F", "summary": "Peak summer heat; intense sun.", "gear": "Light tanks, shorts, UV protection."},
        "7": {"high": "89°F", "low": "66°F", "summary": "Sizzling; warm nights for dining.", "gear": "Breathable fabrics, sandals."},
        "8": {"high": "81°F", "low": "59°F", "summary": "Cooling slightly; breezy autumn air.", "gear": "Light layers, jeans for evening."},
        "9": {"high": "72°F", "low": "54°F", "summary": "Mild and crisp; beautiful foliage.", "gear": "Sweaters, light jacket, boots."},
        "10": {"high": "63°F", "low": "46°F", "summary": "Chilly transition; rainy days return.", "gear": "Trench coat, warm scarf."},
        "11": {"high": "55°F", "low": "40°F", "summary": "Cold and damp; winter lights appear.", "gear": "Winter coat, thermal socks."}
    },
    "name": "Rome, Italy",
    "nightlife": [
        {"name": "Coming Out", "type": "Bar/Club", "tags": ["Iconic", "Gay Street", "Terrace"], "status": "Open"},
        {"name": "My Bar", "type": "Bar/Club", "tags": ["Karaoke", "Dance", "Gay Street"], "status": "Open"},
        {"name": "Company Roma", "type": "Bar/Club", "tags": ["Bears", "Social", "Cruise"], "status": "Open"},
        {"name": "Muccassassina", "type": "Bar/Club", "tags": ["Iconic Party", "Drag", "Large"], "status": "Active"},
        {"name": "Frutta e Verdura", "type": "Bar/Club", "tags": ["Electronic", "Afterhours", "Mixed"], "status": "Open"},
        {"name": "Garbo", "type": "Bar/Club", "tags": ["Cocktails", "Stylish", "Social"], "status": "Open"},
        {"name": "Frenesí e Frizzi", "type": "Bar/Club", "tags": ["Cocktails", "Social", "Trastevere"], "status": "Open"},
        {"name": "The Apartment", "type": "Bar/Club", "tags": ["Rooftop", "Social", "Students"], "status": "Open"},
        {"name": "Latte Fresco", "type": "Bar/Club", "tags": ["Drag Show", "Pop", "Fun"], "status": "Active"},
        {"name": "Macho Lato", "type": "Bar/Club", "tags": ["Men-only", "Cruise"], "status": "Open"},
        {"name": "Skyline Bar", "type": "Bar/Club", "tags": ["Video Bar", "Social"], "status": "Open"}
    ],
    "restaurants": [
        {"name": "Coming Out", "type": "Restaurant (Bistro / Social)"},
        {"name": "L'Elementare Trastevere", "type": "Restaurant (Pizza / Inclusive)"},
        {"name": "Antico Forno Roscioli", "type": "Bakery (Historic / Inclusive)"},
        {"name": "Ginger Sapori e Salute", "type": "Cafe (Healthy / Inclusive)"},
        {"name": "Barnum Roma", "type": "Cafe (Specialty Coffee / Artsy)"},
        {"name": "Etabli", "type": "Restaurant (Wine Bar / Social)"},
        {"name": "Pierluigi", "type": "Restaurant (Seafood / High-end)"},
        {"name": "Faro - Luminari del Caffè", "type": "Cafe (Specialty Coffee)"}
    ],
    "safetyScore": 7,
    "saunas": [
        {"name": "Apollion Sauna", "type": "Sauna", "tags": ["Central", "Modern", "Steam"]},
        {"name": "Sauna Mediterraneo", "type": "Sauna", "tags": ["Historic", "Large", "Cruising"]},
        {"name": "Adam Roma Sauna", "type": "Sauna", "tags": ["Wellness", "Social", "Cruising"]},
        {"name": "Bananon Sauna", "type": "Sauna", "tags": ["Local", "Mature", "Social"]}
    ],
    "stores": [
        {"name": "Mister B Rome", "type": "Store (Fetish / Apparel)"},
        {"name": "Forbidden Planet Rome", "type": "Store (Comics / Inclusive)"},
        {"name": "Open Door Bookshop", "type": "Store (Independent / Books)"},
        {"name": "Mercato Monti", "type": "Store (Urban Market / Designer)"},
        {"name": "Elvis Lives", "type": "Store (Boutique / T-shirts)"}
    ],
    "tours": [
        {"name": "Rome LGBTQ History Walking Tour", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Queer Vatican: Secret Art & History", "activityLevel": "Moderate", "estimatedTime": "3.5 Hours", "pricingGuide": "Moderate"},
        {"name": "Gay Nightlife & Bar Crawl", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Colosseum & Ancient Rome Express", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Budget"},
        {"name": "Vatican Museums & Sistine Chapel", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Trastevere Food Tasting Tour", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Rome Street Food & Jewish Ghetto", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Budget"},
        {"name": "Catacombs & Appian Way Bike Tour", "activityLevel": "High", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Pasta & Tiramisu Class with Wine", "activityLevel": "Low", "estimatedTime": "3.5 Hours", "pricingGuide": "Moderate"},
        {"name": "Tivoli: Villa d'Este & Hadrian's Villa", "activityLevel": "Moderate", "estimatedTime": "7 Hours", "pricingGuide": "Luxury"},
        {"name": "Pompeii & Amalfi Coast Private Day", "activityLevel": "Low", "estimatedTime": "12 Hours", "pricingGuide": "Luxury"},
        {"name": "Rome E-Bike Night Tour", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Capuchin Crypts & Roman Catacombs", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Villa Borghese Gallery Private Tour", "activityLevel": "Low", "estimatedTime": "2.5 Hours", "pricingGuide": "Luxury"},
        {"name": "Rome Sightseeing Golf Cart Tour", "activityLevel": "Low", "estimatedTime": "3 Hours", "pricingGuide": "Luxury"},
        {"name": "Underground Rome: Piazza Navona", "activityLevel": "Moderate", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"},
        {"name": "Rome Pizza Making Class", "activityLevel": "Low", "estimatedTime": "2.5 Hours", "pricingGuide": "Budget"}
    ]
}

singapore_data = {
    "baseFare": [900, 1800],
    "hotels": [
        {"name": "Swissôtel The Stamford", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Hilton Singapore Orchard", "type": "Luxury", "tags": ["LGBTQ Friendly", "IGLTA Member"]},
        {"name": "The Quincy Hotel", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Parkroyal Collection Pickering", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Paradox Singapore Merchant Court", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel Fort Canning", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Capella Singapore", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Rendezvous Hotel Singapore", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Ibis Singapore on Bencoolen", "type": "Budget", "tags": ["LGBTQ Friendly"]},
        {"name": "W Singapore - Sentosa Cove", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "The Fullerton Hotel Singapore", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "InterContinental Singapore", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Naumi Hotel", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "Lloyd's Inn", "type": "Moderate", "tags": ["LGBTQ Friendly", "Minimalist"]},
        {"name": "ST Signature Chinatown", "type": "Budget", "tags": ["LGBTQ Friendly", "Co-living"]}
    ],
    "iata": "SIN",
    "image": "&#127480;&#127468;",
    "lgbtqDistrict": "Tanjong Pagar / Chinatown",
    "lgbtqSafety": "Singapore: Caution advised. Same-sex relations were decriminalized in 2022 but public displays remain conservative. Scene exists but is discreet.",
    "monthlyWeather": {
        "0": {"high": "88°F", "low": "75°F", "summary": "Hot, humid, and rainy; monsoon tail.", "gear": "Light cotton, umbrella, waterproof bag."},
        "1": {"high": "88°F", "low": "75°F", "summary": "Pleasant and bright; less rain.", "gear": "T-shirts, light layers, sunglasses."},
        "2": {"high": "89°F", "low": "76°F", "summary": "Warm and sunny; driest month.", "gear": "Sun hat, light tanks, UV protection."},
        "3": {"high": "90°F", "low": "77°F", "summary": "Hot with afternoon showers.", "gear": "Hydration gear, light raincoat."},
        "4": {"high": "91°F", "low": "77°F", "summary": "Hottest and humid; tropical buzz.", "gear": "Moisture-wicking gear, portable fan."},
        "5": {"high": "91°F", "low": "77°F", "summary": "Intense heat; frequent sudden rain.", "gear": "Light fabrics, sandals, sunglasses."},
        "6": {"high": "88°F", "low": "76°F", "summary": "Humid and breezy; hazy days possible.", "gear": "Breathable shirts, jeans for AC rooms."},
        "7": {"high": "87°F", "low": "76°F", "summary": "Warm and overcast; festive season.", "gear": "Summer attire, light evening layer."},
        "8": {"high": "87°F", "low": "76°F", "summary": "Pleasant evenings; clearing skies.", "gear": "Cotton shorts, comfortable sneakers."},
        "9": {"high": "88°F", "low": "76°F", "summary": "Variable rain; warm afternoons.", "gear": "Versatile layers, portable poncho."},
        "10": {"high": "87°F", "low": "76°F", "summary": "Wet season start; heavy downpours.", "gear": "Sturdy umbrella, waterproof shoes."},
        "11": {"high": "86°F", "low": "75°F", "summary": "Rainiest month; monsoon season.", "gear": "Rain gear, quick-dry clothes."}
    },
    "name": "Singapore",
    "nightlife": [
        {"name": "Tantric Bar", "type": "Bar/Club", "tags": ["Iconic", "Popular", "Social"], "status": "Open"},
        {"name": "Dorothy's Bar", "type": "Bar/Club", "tags": ["Terrace", "Strong Drinks", "Cozy"], "status": "Open"},
        {"name": "Backstage Bar", "type": "Bar/Club", "tags": ["Staple", "Pop", "Indoor/Outdoor"], "status": "Open"},
        {"name": "Lluvia Pub & Bar", "type": "Bar/Club", "tags": ["Bear-friendly", "Karaoke"], "status": "Open"},
        {"name": "ébar", "type": "Bar/Club", "tags": ["Karaoke", "Social Lounge"], "status": "Open"},
        {"name": "EPI (Upstairs)", "type": "Bar/Club", "tags": ["Intimate", "Social"], "status": "Open"},
        {"name": "Mami's", "type": "Bar/Club", "tags": ["New", "Neighborhood", "Social"], "status": "Open"},
        {"name": "Neil Conversion (NC)", "type": "Bar/Club", "tags": ["Dance", "Circuit Events"], "status": "Active"},
        {"name": "Taboo", "type": "Bar/Club", "tags": ["Iconic", "Dance", "Pop"], "status": "Open"}
    ],
    "restaurants": [
        {"name": "PS. Café (Paragon)", "type": "Restaurant (Gay-Popular Iconic)"},
        {"name": "Smol Cafe & Salad Bar", "type": "Cafe (LGBTQ-Supportive / Healthy)"},
        {"name": "Monk's Brew Club", "type": "Cafe (Inclusive / Trivia Nights)"},
        {"name": "Group Therapy Coffee", "type": "Cafe (Social Hub)"},
        {"name": "Common Man Coffee Roasters", "type": "Cafe (Inclusive / Social)"},
        {"name": "Potato Head Singapore", "type": "Restaurant (Rooftop / Trendy)"},
        {"name": "The Blue Ginger", "type": "Restaurant (Peranakan / Inclusive)"},
        {"name": "Artichoke", "type": "Restaurant (Middle Eastern / Artsy)"},
        {"name": "Wild Honey", "type": "Restaurant (Breakfast / Social)"},
        {"name": "Super Loco", "type": "Restaurant (Mexican / Social)"}
    ],
    "safetyScore": 6,
    "saunas": [
        {"name": "Ten Mens Club", "type": "Sauna", "tags": ["Premier", "Multi-level", "Themed Nights"]},
        {"name": "Keybox Sauna", "type": "Sauna", "tags": ["Modern", "Social", "Central"]},
        {"name": "One Seven", "type": "Sauna", "tags": ["Gym-focused", "Social"]}
    ],
    "stores": [
        {"name": "Heckin' Unicorn", "type": "Local Queer Lifestyle Brand"},
        {"name": "Prout Shop", "type": "Online Pride Merchandise"},
        {"name": "U4Ria", "type": "Adult / Underwear / Toys"},
        {"name": "BooksActually", "type": "Independent Bookstore (Inclusive)"},
        {"name": "Mandarin Gallery", "type": "High-end Shopping Hub"}
    ],
    "tours": [
        {"name": "LGBTQ History Walking Tour", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Moderate"},
        {"name": "Singapore Inclusivity Journey", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Budget"},
        {"name": "Street Food & Hawker Center Walk", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Gardens by the Bay Experience", "activityLevel": "Low", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Singapore River Cruise (Sunset)", "activityLevel": "Low", "estimatedTime": "1 Hour", "pricingGuide": "Budget"},
        {"name": "Chinatown Heritage & Food Tour", "activityLevel": "High", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Sentosa Island Adventure", "activityLevel": "High", "estimatedTime": "6 Hours", "pricingGuide": "Luxury"},
        {"name": "Peranakan Culture & Tile Making", "activityLevel": "Low", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Marina Bay Sands Skypark Visit", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Moderate"},
        {"name": "Night Safari Tram & Walk", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Luxury"},
        {"name": "Little India Spices & Sights Tour", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Battlebox WWII Underground Tour", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Moderate"},
        {"name": "Universal Studios VIP Experience", "activityLevel": "High", "estimatedTime": "8 Hours", "pricingGuide": "Luxury"},
        {"name": "National Museum: Journey of Time", "activityLevel": "Low", "estimatedTime": "2.5 Hours", "pricingGuide": "Budget"},
        {"name": "Pulau Ubin Nature Bike Tour", "activityLevel": "High", "estimatedTime": "5 Hours", "pricingGuide": "Moderate"}
    ]
}

with open('/home/user/PrideTravelScoutAPP/destinations.json', 'r') as f:
    file_lines = f.readlines()

print(f"Original: {len(file_lines)} lines")

updates = []
for city_key, city_data in [('rome', rome_data), ('singapore', singapore_data)]:
    start, end = find_toplevel_city_range(file_lines, city_key)
    if start is not None:
        print(f"{city_key}: lines {start+1}-{end+1} ({end-start+1} lines)")
        updates.append((start, end, city_key, city_data))
    else:
        print(f"WARNING: {city_key} not found!")

updates.sort(key=lambda x: x[0], reverse=True)

for start, end, city_key, city_data in updates:
    new_lines = build_toplevel_city_lines(city_key, city_data)
    orig_last = file_lines[end].rstrip('\n')
    has_comma = orig_last.rstrip().endswith(',')
    formatted = [l + '\n' for l in new_lines]
    if has_comma:
        formatted[-1] = formatted[-1].rstrip('\n') + ',\n'
    file_lines[start:end+1] = formatted
    print(f"Replaced {city_key}: {end-start+1} -> {len(formatted)} lines")

print(f"New total: {len(file_lines)} lines")

try:
    json.loads(''.join(file_lines))
    print("JSON validation: PASSED")
except json.JSONDecodeError as e:
    print(f"JSON validation: FAILED - {e}")

with open('/home/user/PrideTravelScoutAPP/destinations.json', 'w') as f:
    f.writelines(file_lines)

print("Done.")
