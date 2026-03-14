#!/usr/bin/env python3
import json, re

def build_city_lines(city_key, city_data):
    lines = []
    lines.append(f'    "{city_key}": {{')
    keys = list(city_data.keys())
    for i, k in enumerate(keys):
        v = city_data[k]
        comma = ',' if i < len(keys) - 1 else ''
        lines.append(f'      "{k}": {json.dumps(v, separators=(", ", ": "))}{comma}')
    lines.append('    }')
    return lines

def find_city_range(lines, city_key):
    start = None
    for i, line in enumerate(lines):
        if re.match(rf'\s+"{re.escape(city_key)}"\s*:\s*\{{', line):
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

# Frankfurt data
frankfurt_data = {
    "baseFare": [500, 1000],
    "iata": "FRA",
    "image": "frankfurt.jpg",
    "lgbtqDistrict": "Sachsenhausen / Berger Straße",
    "lgbtqSafety": "Generally safe; LGBTQ+ scene concentrated in Sachsenhausen and around Berger Straße.",
    "name": "Frankfurt, Germany",
    "safetyScore": 8,
    "gaycities": "https://frankfurt.gaycities.com/",
    "hotels": [
        {"name": "Steigenberger Frankfurter Hof", "type": "Luxury", "tags": ["World Rainbow Hotels", "IGLTA Member"]},
        {"name": "Hotel Rocco Forte Villa Kennedy", "type": "Luxury", "tags": ["World Rainbow Hotels", "LGBTQ Friendly"]},
        {"name": "Roomers, Frankfurt", "type": "Luxury", "tags": ["LGBTQ Friendly", "Design Focus"]},
        {"name": "The Westin Grand Frankfurt", "type": "Luxury", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "Hilton Frankfurt City Centre", "type": "Luxury", "tags": ["IGLTA Member", "LGBTQ Friendly"]},
        {"name": "Jumeirah Frankfurt", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Adina Apartment Hotel Frankfurt", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Innside by Meliá Frankfurt Ostend", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "25hours Hotel The Goldman", "type": "Moderate", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "Hotel Cult Frankfurt City", "type": "Moderate", "tags": ["LGBTQ Friendly", "Sachsenhausen"]},
        {"name": "Motel One Frankfurt-Römer", "type": "Budget", "tags": ["LGBTQ Friendly"]},
        {"name": "Fleming's Selection Hotel City", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Scandic Frankfurt Museumsufer", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel Libertine Lindenberg", "type": "Moderate", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "MEININGER Hotel Frankfurt/Main", "type": "Budget", "tags": ["LGBTQ Friendly"]}
    ],
    "nightlife": [
        {"name": "Lucky's", "type": "Bar/Club", "tags": ["Social", "Cocktails", "Pop"], "status": "Open"},
        {"name": "Central", "type": "Bar/Club", "tags": ["Iconic", "Social", "Terrace"], "status": "Open"},
        {"name": "Comeback", "type": "Bar/Club", "tags": ["Drag", "Social", "Neighborhood"], "status": "Open"},
        {"name": "La Gata", "type": "Bar/Club", "tags": ["Lesbian-centric", "Alternative"], "status": "Open"},
        {"name": "Switchboard", "type": "Bar/Club", "tags": ["Community Hub", "Social", "Mixed"], "status": "Open"},
        {"name": "Kumpel", "type": "Bar/Club", "tags": ["Traditional", "Bears", "Social"], "status": "Open"},
        {"name": "Orange Bar", "type": "Bar/Club", "tags": ["Stylish", "Cocktails", "Music"], "status": "Open"},
        {"name": "Metropol Bar", "type": "Bar/Club", "tags": ["Leather-friendly", "Neighborhood"], "status": "Open"},
        {"name": "Pik Dame", "type": "Bar/Club", "tags": ["Performance", "Alternative", "Kitsch"], "status": "Open"},
        {"name": "Blue Angel", "type": "Bar/Club", "tags": ["Drag", "Pop", "Social"], "status": "Open"},
        {"name": "Velvet Club", "type": "Bar/Club", "tags": ["Dance", "Electronic", "Mixed"], "status": "Open"},
        {"name": "Gibson Club (The Choice Party)", "type": "Bar/Club", "tags": ["High Energy", "Pop", "Monthly"], "status": "Open"},
        {"name": "Sauna am Verna Park", "type": "Sauna", "tags": ["Modern", "Large", "Steam"], "status": "Open"},
        {"name": "Sauna Mainhattan", "type": "Sauna", "tags": ["Iconic", "Cinema", "Cruising"], "status": "Open"},
        {"name": "Römer-Sauna", "type": "Sauna", "tags": ["Traditional", "Mature", "Local"], "status": "Open"}
    ],
    "restaurants": [
        {"name": "Metropol am Dom", "category": "Restaurant (Fine Dining / Social)"},
        {"name": "IIMORI Patisserie", "category": "Bakery / Cafe (Inclusive)"},
        {"name": "Bitter & Zart", "category": "Sweet Shop / Cafe"},
        {"name": "Ginkgo", "category": "Restaurant (Fusion / Inclusive)"},
        {"name": "Mainlust", "category": "Restaurant (Traditional / Social)"},
        {"name": "Margarete", "category": "Restaurant (Modern / Artsy)"},
        {"name": "Cafe Laumer", "category": "Cafe / Bakery (Historic)"},
        {"name": "Oatman's", "category": "Cafe (Vegan / Specialty)"},
        {"name": "EatDOORI", "category": "Restaurant (Indian / Inclusive)"},
        {"name": "Antipodean Specialty Coffee", "category": "Cafe (Australian Style)"}
    ],
    "stores": [
        {"name": "Bruno's Frankfurt", "category": "Store (Fashion / Lifestyle / Books)"},
        {"name": "MGW Frankfurt", "category": "Store (Adult / Fetish / Apparel)"},
        {"name": "Eichhorn", "category": "Store (Leather / Gear)"},
        {"name": "Kleinmarkthalle", "category": "Store (Gourmet / Social Hub)"},
        {"name": "Berger Straße Boutiques", "category": "Store (Boutique Hub)"},
        {"name": "Oxfam Shop (Merianplatz)", "category": "Store (Second-hand / Inclusive)"}
    ],
    "tours": [
        {"name": "Frankfurt Queer History Walk", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Moderate"},
        {"name": "Frankfurt Pride Heritage Walk", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Budget"},
        {"name": "LGBTQ Nightlife & Bar Crawl", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Main River Sightseeing Cruise", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"},
        {"name": "Städel Museum Art & History", "activityLevel": "Low", "estimatedTime": "2 Hours", "pricingGuide": "Moderate"},
        {"name": "Frankfurt Old Town Highlights", "activityLevel": "Moderate", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"},
        {"name": "Sachsenhausen Apple Wine Experience", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Frankfurt Skyline Panorama Walk", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Dialog Museum (Blind Experience)", "activityLevel": "Moderate", "estimatedTime": "1.5 Hours", "pricingGuide": "Moderate"},
        {"name": "E-Scooter Riverfront Tour", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"},
        {"name": "Palmengarten Botanical Walk", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Heidelberg Full-Day Private Tour", "activityLevel": "Moderate", "estimatedTime": "8 Hours", "pricingGuide": "Luxury"},
        {"name": "Rhine Valley Wine & Castle Day", "activityLevel": "Moderate", "estimatedTime": "9 Hours", "pricingGuide": "Luxury"},
        {"name": "Frankfurt Street Art & Mural Tour", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Goethe House & Museum Visit", "activityLevel": "Low", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Frankfurt Indoor Market Tasting", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Moderate"},
        {"name": "Zeil Shopping & Terrace Views", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Budget"}
    ],
    "monthlyWeather": {
        "0": {"high": "39°F", "low": "30°F", "summary": "Cold and overcast; occasional light snow.", "gear": "Heavy coat, thermal layers, boots."},
        "1": {"high": "43°F", "low": "31°F", "summary": "Chilly with frequent winter rain.", "gear": "Wool coat, windproof umbrella."},
        "2": {"high": "51°F", "low": "36°F", "summary": "Variable spring air; damp and breezy.", "gear": "Trench coat, layered sweaters."},
        "3": {"high": "59°F", "low": "41°F", "summary": "Mild and bright; parks begin to bloom.", "gear": "Light jacket, scarf, jeans."},
        "4": {"high": "66°F", "low": "47°F", "summary": "Pleasant spring; peak outdoor comfort.", "gear": "T-shirts, light cardigan."},
        "5": {"high": "73°F", "low": "54°F", "summary": "Warm summer start; clear sunny days.", "gear": "Cotton shirts, sunglasses."},
        "6": {"high": "76°F", "low": "58°F", "summary": "Mild summer; light rain showers possible.", "gear": "Summer attire, light rain shell."},
        "7": {"high": "76°F", "low": "57°F", "summary": "Warm and humid; peak travel season.", "gear": "Linen, sandals, sun hat."},
        "8": {"high": "68°F", "low": "51°F", "summary": "Cooling down; crisp autumn mornings.", "gear": "Light jacket, layered tops."},
        "9": {"high": "57°F", "low": "44°F", "summary": "Cool and breezy; beautiful foliage.", "gear": "Sweaters, trench coat, scarf."},
        "10": {"high": "47°F", "low": "37°F", "summary": "Rainy and windy transition to winter.", "gear": "Waterproof boots, warm hat."},
        "11": {"high": "41°F", "low": "32°F", "summary": "Cold and damp; Christmas markets open.", "gear": "Winter gear, thermal socks."}
    }
}

# Hamburg data
hamburg_data = {
    "baseFare": [650, 1150],
    "iata": "HAM",
    "image": "hamburg.jpg",
    "lgbtqDistrict": "St. Georg",
    "lgbtqSafety": "Very welcoming; St. Georg is Hamburg's established LGBTQ+ neighborhood with visible queer culture.",
    "name": "Hamburg, Germany",
    "safetyScore": 8,
    "gaycities": "https://hamburg.gaycities.com/",
    "hotels": [
        {"name": "TORTUE HAMBURG", "type": "Luxury", "tags": ["World Rainbow Hotels", "LGBTQ Friendly"]},
        {"name": "Le Méridien Hamburg", "type": "Luxury", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "The George Hamburg", "type": "Mid-Priced", "tags": ["World Rainbow Hotels", "LGBTQ Friendly"]},
        {"name": "Hotel Hanseatin", "type": "Moderate", "tags": ["LGBTQ Owned", "Women-Only"]},
        {"name": "ARCOTEL Onyx Hamburg", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "IGLTA Member"]},
        {"name": "Henri Hotel Hamburg Downtown", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "Wedina Budget", "type": "Budget", "tags": ["LGBTQ Friendly", "Art-focused"]},
        {"name": "Superbude St. Georg", "type": "Budget", "tags": ["LGBTQ Friendly", "Social Hub"]},
        {"name": "NYX Hotel Hamburg", "type": "Moderate", "tags": ["LGBTQ Friendly", "Design-led"]},
        {"name": "Fairmont Hotel Vier Jahreszeiten", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "The Westin Hamburg", "type": "Luxury", "tags": ["LGBTQ Friendly", "Iconic Landmark"]},
        {"name": "25hours Hotel HafenCity", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "Motel One Hamburg Alster", "type": "Budget", "tags": ["LGBTQ Friendly"]},
        {"name": "Reichshof Hotel Hamburg", "type": "Moderate", "tags": ["LGBTQ Friendly", "Historic"]},
        {"name": "ARCOTEL Rubin Hamburg", "type": "Moderate", "tags": ["LGBTQ Friendly"]}
    ],
    "nightlife": [
        {"name": "Bellini Bar", "type": "Bar/Club", "tags": ["Cocktails", "Italian Flair", "Social"], "status": "Open"},
        {"name": "Extratour", "type": "Bar/Club", "tags": ["Basement Bar", "Mixed Crowd", "Social"], "status": "Open"},
        {"name": "M&V Bar", "type": "Bar/Club", "tags": ["Iconic", "Social", "Mixed Ages"], "status": "Open"},
        {"name": "WunderBar", "type": "Bar/Club", "tags": ["Dance", "Pop", "High-Energy"], "status": "Open"},
        {"name": "Olivia Jones Bar", "type": "Bar/Club", "tags": ["Drag Show", "Cabaret", "Comedy"], "status": "Open"},
        {"name": "Pick Up Bar", "type": "Bar/Club", "tags": ["Legendary", "Drag", "Neighborhood"], "status": "Open"},
        {"name": "Toom Peerstall", "type": "Bar/Club", "tags": ["Historic", "Since 1919", "Social"], "status": "Open"},
        {"name": "PINK INC.", "type": "Bar/Club", "tags": ["Large Queer Party", "Dance"], "status": "Open"},
        {"name": "136 Grad", "type": "Bar/Club", "tags": ["Electronic", "Clubbing", "Youth"], "status": "Open"},
        {"name": "Thomaskeller", "type": "Bar/Club", "tags": ["Basement Bar", "Social", "Local"], "status": "Open"},
        {"name": "MINUS Bar", "type": "Bar/Club", "tags": ["Cocktails", "Ice Cream", "House Music"], "status": "Open"},
        {"name": "Bar Kunterbunt", "type": "Bar/Club", "tags": ["Karaoke", "Social", "Fun"], "status": "Open"},
        {"name": "Piccadilly Bar", "type": "Bar/Club", "tags": ["St. Pauli Classic", "Social"], "status": "Open"},
        {"name": "S.L.U.T. Club", "type": "Bar/Club", "tags": ["Men-only", "Fetish", "Cruising"], "status": "Open"},
        {"name": "TOM'S Saloon", "type": "Bar/Club", "tags": ["Iconic", "Cruise Club", "Leather"], "status": "Open"},
        {"name": "Dragon Sauna", "type": "Sauna", "tags": ["Largest in Hamburg", "Finnish", "Bar"], "status": "Open"},
        {"name": "Apollo Sauna", "type": "Sauna", "tags": ["Intimate", "Old-School", "Mature"], "status": "Open"},
        {"name": "Men's Heaven Sauna", "type": "Sauna", "tags": ["4 Levels", "Cruising", "Massage"], "status": "Open"},
        {"name": "New Man", "type": "Sauna", "tags": ["Intimate", "Younger Crowd"], "status": "Open"}
    ],
    "restaurants": [
        {"name": "Café Gnosa", "category": "Cafe / Bakery (LGBTQ Landmark)"},
        {"name": "Café Uhrlaub", "category": "Cafe / Restaurant (Historic Hub)"},
        {"name": "Das Dorf", "category": "Restaurant (Traditional German/Austrian)"},
        {"name": "Cox", "category": "Restaurant (Fine Dining / Social)"},
        {"name": "Kyti Voo", "category": "Cafe (Craft Beer / Terrace)"},
        {"name": "Cafe Leonar", "category": "Cafe (Jewish Bistro / Artsy)"},
        {"name": "Backbord", "category": "Restaurant (Schnitzel / Inclusive)"},
        {"name": "La Luna", "category": "Restaurant (Mediterranean / Social)"},
        {"name": "Cafe Paris", "category": "Cafe / Restaurant (Historic / Social)"},
        {"name": "Bistro St. Georg", "category": "Restaurant (French / Local Favorite)"}
    ],
    "stores": [
        {"name": "Bruno's Hamburg", "category": "Store (Fashion / Lifestyle / Books)"},
        {"name": "Clemens", "category": "Store (Fetish / Leather / Gear)"},
        {"name": "Mr. Chaps", "category": "Store (Fetish / Apparel)"},
        {"name": "Dolly Buster by Seventh Heaven", "category": "Store (Adult / Accessories)"},
        {"name": "Mystery Hall", "category": "Store (Adult / Media)"},
        {"name": "Homo-Kino-Hamburg", "category": "Store (Cinema / Adult Retail)"}
    ],
    "tours": [
        {"name": "Gay Hamburg History Walk", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Budget"},
        {"name": "Reeperbahn Nightlife & Drag Tour", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "St. Pauli Queer Heritage Tour", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Elbphilharmonie & HafenCity Tour", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"},
        {"name": "Speicherstadt Coffee & History", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Moderate"},
        {"name": "Harbour Boat Cruise (Evening)", "activityLevel": "Low", "estimatedTime": "1 Hour", "pricingGuide": "Budget"},
        {"name": "Craft Beer & Alster Walk", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Hamburg E-Bike City Discovery", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Private Icons & Hidden Gems Tour", "activityLevel": "Low", "estimatedTime": "4 Hours", "pricingGuide": "Luxury"},
        {"name": "UNESCO Warehouse District Walk", "activityLevel": "Moderate", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"},
        {"name": "St. Michael's Church Tower Climb", "activityLevel": "High", "estimatedTime": "1 Hour", "pricingGuide": "Budget"},
        {"name": "Alster Lake Sailing Experience", "activityLevel": "Low", "estimatedTime": "2 Hours", "pricingGuide": "Moderate"},
        {"name": "Beatles' Hamburg Musical Walk", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Miniatur Wunderland Behind Scenes", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Moderate"},
        {"name": "VIP City Drive (Personalized)", "activityLevel": "Low", "estimatedTime": "3 Hours", "pricingGuide": "Luxury"},
        {"name": "Hamburg Crime & Sinner Tour", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Chocolate Museum Interactive Tour", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"}
    ],
    "monthlyWeather": {
        "0": {"high": "37°F", "low": "28°F", "summary": "Grey, windy, and frequent rain/snow.", "gear": "Puffer coat, waterproof boots, umbrella."},
        "1": {"high": "40°F", "low": "29°F", "summary": "Damp and chilly; biting sea winds.", "gear": "Scarf, gloves, windproof rain jacket."},
        "2": {"high": "48°F", "low": "33°F", "summary": "Early spring drizzle; unpredictable.", "gear": "Trench coat, layered sweaters, umbrella."},
        "3": {"high": "56°F", "low": "39°F", "summary": "Bright but cool; wind remains constant.", "gear": "Light layers, scarf, sturdy sneakers."},
        "4": {"high": "64°F", "low": "45°F", "summary": "Pleasant spring air; occasional showers.", "gear": "T-shirts, light cardigan, rain shell."},
        "5": {"high": "71°F", "low": "52°F", "summary": "Warm summer start; very comfortable.", "gear": "Cotton shirts, sunglasses, light layer."},
        "6": {"high": "73°F", "low": "55°F", "summary": "Mild summer; frequent light rain.", "gear": "Sunglasses, umbrella, denim jacket."},
        "7": {"high": "73°F", "low": "55°F", "summary": "Best for outdoor dining; breezy.", "gear": "Linen clothes, sunscreen, light sweater."},
        "8": {"high": "66°F", "low": "49°F", "summary": "Crisp autumn transition; colorful.", "gear": "Light jacket, layered tops, boots."},
        "9": {"high": "57°F", "low": "42°F", "summary": "Cool and windy; frequent rain.", "gear": "Wool sweaters, waterproof coat."},
        "10": {"high": "47°F", "low": "36°F", "summary": "Rainy and dark transition to winter.", "gear": "Heavy umbrella, warm hat, boots."},
        "11": {"high": "40°F", "low": "31°F", "summary": "Cold and damp; winter lights appear.", "gear": "Winter coat, thermal socks, scarf."}
    }
}

# Read the file
with open('/home/user/PrideTravelScoutAPP/destinations.json', 'r') as f:
    file_lines = f.readlines()

print(f"Original file: {len(file_lines)} lines")

# Find and replace Frankfurt and Hamburg (in reverse order to preserve line numbers)
updates = []
for city_key, city_data in [('frankfurt', frankfurt_data), ('hamburg', hamburg_data)]:
    start, end = find_city_range(file_lines, city_key)
    if start is not None:
        print(f"{city_key}: lines {start+1}-{end+1}")
        updates.append((start, end, city_key, city_data))
    else:
        print(f"WARNING: {city_key} not found!")

# Sort by start line descending
updates.sort(key=lambda x: x[0], reverse=True)

for start, end, city_key, city_data in updates:
    new_lines = build_city_lines(city_key, city_data)
    # Preserve trailing comma/newline from original
    orig_last = file_lines[end].rstrip('\n')
    has_comma = orig_last.rstrip().endswith(',')

    # Format new lines with newlines
    formatted = [l + '\n' for l in new_lines]
    if has_comma:
        # Add comma to last line
        formatted[-1] = formatted[-1].rstrip('\n') + ',\n'

    file_lines[start:end+1] = formatted
    print(f"Replaced {city_key}: {end-start+1} old lines -> {len(formatted)} new lines")

print(f"New file: {len(file_lines)} lines")

# Validate JSON
try:
    combined = ''.join(file_lines)
    json.loads(combined)
    print("JSON validation: PASSED")
except json.JSONDecodeError as e:
    print(f"JSON validation: FAILED - {e}")

# Write back
with open('/home/user/PrideTravelScoutAPP/destinations.json', 'w') as f:
    f.writelines(file_lines)

print("File written successfully.")
