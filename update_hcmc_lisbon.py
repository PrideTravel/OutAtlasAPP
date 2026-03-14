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

hcmc_data = {
    "baseFare": [800, 2600],
    "hotels": [
        {"name": "Rex Hotel Saigon", "type": "Luxury", "tags": ["World Rainbow Hotels Member"]},
        {"name": "The Reverie Saigon", "type": "Luxury", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "Park Hyatt Saigon", "type": "Luxury", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "Caravelle Saigon Hotel", "type": "Luxury", "tags": ["LGBTQ Friendly", "Heritage"]},
        {"name": "Hotel Nikko Saigon", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Grand Hotel Saigon", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "La Siesta Premium Saigon", "type": "Luxury", "tags": ["LGBTQIA-Welcoming"]},
        {"name": "Orchids Saigon Hotel", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Silverland Ben Thanh Hotel", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Beautiful Saigon Boutique Hotel", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Holiday Inn & Suites Saigon Airport", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Language Exchange Hotel 3", "type": "Budget", "tags": ["LGBTQIA-Welcoming"]},
        {"name": "Saigon Authentic Hostel", "type": "Budget", "tags": ["LGBTQIA-Welcoming"]},
        {"name": "Prei Nokor Hostel", "type": "Budget", "tags": ["LGBTQ Friendly"]},
        {"name": "Victory Airport Hotel", "type": "Budget", "tags": ["LGBTQIA-Welcoming"]}
    ],
    "iata": "SGN",
    "image": "🇻🇳",
    "lgbtqDistrict": "District 1",
    "lgbtqSafety": "Vietnam: Safe. Rapidly growing scene. Public displays of affection are generally discreet.",
    "monthlyWeather": {
        "0": {"high": "90°F", "low": "72°F", "summary": "Hot and dry; peak travel season.", "gear": "Linen shirts, shorts, sunglasses."},
        "1": {"high": "92°F", "low": "73°F", "summary": "Dry and sunny; clear skies.", "gear": "Breathable fabrics, sunscreen."},
        "2": {"high": "94°F", "low": "76°F", "summary": "Very hot; low humidity.", "gear": "Light cotton, hat, UV protection."},
        "3": {"high": "95°F", "low": "79°F", "summary": "Hottest month; oppressive heat.", "gear": "Hydration gear, light tanks."},
        "4": {"high": "94°F", "low": "78°F", "summary": "Transition to rain; high humidity.", "gear": "Portable fan, light raincoat."},
        "5": {"high": "92°F", "low": "77°F", "summary": "Rainy season begins; tropical storms.", "gear": "Umbrella, waterproof bag."},
        "6": {"high": "91°F", "low": "76°F", "summary": "Humid with frequent rain showers.", "gear": "Quick-dry clothes, sandals."},
        "7": {"high": "91°F", "low": "76°F", "summary": "Warm and wet; overcast days.", "gear": "Rain poncho, light layers."},
        "8": {"high": "90°F", "low": "76°F", "summary": "Wet season peak; heavy rain.", "gear": "Sturdy umbrella, waterproof shoes."},
        "9": {"high": "90°F", "low": "75°F", "summary": "Rain decreases; high humidity.", "gear": "Moisture-wicking gear."},
        "10": {"high": "90°F", "low": "74°F", "summary": "Drier air returns; pleasant evenings.", "gear": "Light sweater for AC, jeans."},
        "11": {"high": "89°F", "low": "72°F", "summary": "Warm and clear; holiday atmosphere.", "gear": "Summer attire, light layers."}
    },
    "name": "Ho Chi Minh City, Vietnam",
    "nightlife": [
        {"name": "Frolic Bar", "type": "Bar/Club", "tags": ["Drag Shows", "Dance", "Neon"], "status": "Open"},
        {"name": "ChinChin Bar", "type": "Bar/Club", "tags": ["Social", "Cocktails", "Trendy"], "status": "Open"},
        {"name": "Thi Bar", "type": "Bar/Club", "tags": ["Live Music", "Mixed Crowd"], "status": "Open"},
        {"name": "Republic Lounge", "type": "Bar/Club", "tags": ["Drag Shows", "Younger Crowd"], "status": "Open"},
        {"name": "Le PUB", "type": "Bar/Club", "tags": ["Relaxed", "Karaoke", "Local"], "status": "Open"},
        {"name": "Poc Poc Beer Garden", "type": "Bar/Club", "tags": ["Outdoor", "Social", "High Energy"], "status": "Open"},
        {"name": "Full Disclosure", "type": "Bar/Club", "tags": ["Drag Extravaganza"], "status": "Open"},
        {"name": "GenderFunk", "type": "Bar/Club", "tags": ["Creative Queer Parties"], "status": "Open"}
    ],
    "restaurants": [
        {"name": "Bánh Mì Huynh Hoa", "type": "Sandwich Shop (Lesbian-Owned)"},
        {"name": "Pride Cafe", "type": "Cafe (Queer-Owned / Social Hub)"},
        {"name": "Ak", "type": "Cafe (Queer-Owned / Artsy)"},
        {"name": "The Refinery", "type": "Restaurant (French Bistro)"},
        {"name": "Bếp Mẹ Ỉn", "type": "Restaurant (Traditional Vietnamese)"},
        {"name": "Filthy Vegan", "type": "Restaurant (Plant-based)"},
        {"name": "The Old Compass Cafe", "type": "Cafe / Wine Bar"},
        {"name": "Café Marcel", "type": "Cafe (French-Vietnamese Fusion)"}
    ],
    "safetyScore": 7,
    "saunas": [
        {"name": "GUU Spa", "type": "Sauna", "tags": ["BDSM Maze", "Dark Room", "Sauna"]},
        {"name": "Galaxy Sauna", "type": "Sauna", "tags": ["Local", "Relaxed", "Clean"]},
        {"name": "3Some Spa", "type": "Sauna", "tags": ["Luxury Steam", "VIP Rooms"]},
        {"name": "The Sun Spa", "type": "Sauna", "tags": ["Men's Massage", "24 Hours"]},
        {"name": "Rainbow Spa", "type": "Sauna", "tags": ["Professional Massage"]}
    ],
    "stores": [
        {"name": "Mekong Quilts", "type": "Social Enterprise / Local Crafts"},
        {"name": "Ginkgo T-Shirts", "type": "Boutique (Inclusive / Sustainable)"},
        {"name": "L'Usine", "type": "Concept Store (Fashion / Gifts)"},
        {"name": "Amai", "type": "Boutique (Ceramics / Design)"},
        {"name": "Sadéc District", "type": "Store (Home Decor / Local Art)"}
    ],
    "tours": [
        {"name": "LGBT-Led Street Food Tour", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Discover Saigon with Pride (Private)", "activityLevel": "Low", "estimatedTime": "5 Hours", "pricingGuide": "Moderate"},
        {"name": "Saigon Motorbike Night Adventure", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Cu Chi Tunnels Exploration", "activityLevel": "Moderate", "estimatedTime": "6 Hours", "pricingGuide": "Moderate"},
        {"name": "Mekong Delta Day Trip", "activityLevel": "Moderate", "estimatedTime": "9 Hours", "pricingGuide": "Moderate"},
        {"name": "Saigon Opera House Performance", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Moderate"},
        {"name": "Vespa Sightseeing Tour", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Luxury"},
        {"name": "Bean-to-Bar Chocolate Workshop", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Moderate"},
        {"name": "Independence Palace History Walk", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Saigon River Sunset Cruise", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Moderate"},
        {"name": "War Remnants Museum Guided Tour", "activityLevel": "Low", "estimatedTime": "2.5 Hours", "pricingGuide": "Budget"},
        {"name": "Bitexco Financial Tower View", "activityLevel": "Low", "estimatedTime": "1 Hour", "pricingGuide": "Budget"},
        {"name": "Ben Thanh Market Shopping Tour", "activityLevel": "High", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Cholon Chinatown Cultural Walk", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Saigon US Army Jeep History Tour", "activityLevel": "Low", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Egg Coffee Making Class", "activityLevel": "Low", "estimatedTime": "1 Hour", "pricingGuide": "Budget"},
        {"name": "Vietnamese Cooking & Market Tour", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"}
    ]
}

lisbon_data = {
    "baseFare": [600, 1200],
    "hotels": [
        {"name": "The Late Birds Lisbon", "type": "Mid-Priced", "tags": ["LGBTQ Owned & Operated", "Men-Only"]},
        {"name": "Bairro Alto Hotel", "type": "Luxury", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "Corinthia Lisbon", "type": "Luxury", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "Pestana Palace Lisboa", "type": "Luxury", "tags": ["World Rainbow Hotels", "LGBTQ Friendly"]},
        {"name": "Hotel Anjo Azul", "type": "Moderate", "tags": ["LGBTQ Owned", "Bairro Alto"]},
        {"name": "1908 Lisboa Hotel", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "Altis Avenida Hotel", "type": "Luxury", "tags": ["LGBTQ Friendly", "IGLTA Member"]},
        {"name": "H10 Duque de Loulé", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel do Chiado", "type": "Luxury", "tags": ["LGBTQ Friendly", "Views"]},
        {"name": "Browns Central Hotel", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "Memmo Príncipe Real", "type": "Luxury", "tags": ["LGBTQ Friendly", "IGLTA Member"]},
        {"name": "Selina Secret Garden Lisbon", "type": "Budget", "tags": ["LGBTQ Friendly", "Social Hub"]},
        {"name": "My Story Hotel Tejo", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel Heritage Avenida Liberdade", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Lookout Lisbon! Hostel", "type": "Budget", "tags": ["LGBTQ Friendly", "Social"]}
    ],
    "iata": "LIS",
    "image": "&#127477;&#127481;",
    "lgbtqDistrict": "Bairro Alto / Príncipe Real",
    "lgbtqSafety": "Portugal: Very Safe. Lisbon has one of Europe's most welcoming LGBTQ+ scenes.",
    "monthlyWeather": {
        "0": {"high": "59°F", "low": "47°F", "summary": "Mild but rainy; clear sunny spells.", "gear": "Light jacket, umbrella, sneakers."},
        "1": {"high": "61°F", "low": "48°F", "summary": "Pleasant and bright; crisp mornings.", "gear": "Sweaters, light scarf, jeans."},
        "2": {"high": "65°F", "low": "51°F", "summary": "Spring air; blooming parks.", "gear": "T-shirts, light jacket, sunglasses."},
        "3": {"high": "68°F", "low": "53°F", "summary": "Sunny and warm; ideal for sightseeing.", "gear": "Cotton shirts, comfortable walking shoes."},
        "4": {"high": "72°F", "low": "56°F", "summary": "Warm summer start; very clear skies.", "gear": "Linen clothes, sunscreen, sun hat."},
        "5": {"high": "77°F", "low": "60°F", "summary": "Hot and dry; peak beach season.", "gear": "Swimwear, light tanks, shades."},
        "6": {"high": "82°F", "low": "63°F", "summary": "Peak summer heat; intense Atlantic sun.", "gear": "Light fabrics, stay hydrated."},
        "7": {"high": "83°F", "low": "64°F", "summary": "Sizzling; warm nights for outdoor dining.", "gear": "Shorts, sandals, UV protection."},
        "8": {"high": "79°F", "low": "61°F", "summary": "Cooling slightly; breezy autumn air.", "gear": "Light layers, jeans for evening."},
        "9": {"high": "72°F", "low": "57°F", "summary": "Mild and crisp; beautiful foliage.", "gear": "Sweaters, trench coat, scarf."},
        "10": {"high": "64°F", "low": "53°F", "summary": "Chilly transition; rainy days return.", "gear": "Waterproof boots, warm hat."},
        "11": {"high": "60°F", "low": "49°F", "summary": "Cool and damp; festive winter lights.", "gear": "Winter coat, thermal socks."}
    },
    "name": "Lisbon, Portugal",
    "nightlife": [
        {"name": "Finalmente Club", "type": "Bar/Club", "tags": ["Iconic", "Drag", "Dance"], "status": "Open"},
        {"name": "Trumps", "type": "Bar/Club", "tags": ["Iconic", "Dance", "Pop"], "status": "Open"},
        {"name": "Construction", "type": "Bar/Club", "tags": ["Bears", "Masculine", "Dance"], "status": "Open"},
        {"name": "Friends Bairro Alto", "type": "Bar/Club", "tags": ["Cocktails", "Social", "Pop"], "status": "Open"},
        {"name": "TR3S Lisboa", "type": "Bar/Club", "tags": ["Bears", "Social", "Terrace"], "status": "Open"},
        {"name": "Shelter Bar", "type": "Bar/Club", "tags": ["Bears", "Cruise-friendly", "Social"], "status": "Open"},
        {"name": "SideBar", "type": "Bar/Club", "tags": ["Cocktails", "Chic", "Social"], "status": "Open"},
        {"name": "Posh Club Lisbon", "type": "Bar/Club", "tags": ["Dance", "High Energy", "International"], "status": "Open"},
        {"name": "Bar 106", "type": "Bar/Club", "tags": ["Cruising", "Men-only", "Social"], "status": "Open"},
        {"name": "Cru Clube", "type": "Bar/Club", "tags": ["Fetish", "Cruise", "Men-only"], "status": "Open"},
        {"name": "Woof X", "type": "Bar/Club", "tags": ["Leather", "Fetish", "Men-only"], "status": "Open"},
        {"name": "Trombeta Bath", "type": "Bar/Club", "tags": ["Social", "Pre-club", "Mixed"], "status": "Open"},
        {"name": "Maria Caxuxa", "type": "Bar/Club", "tags": ["Social", "Artsy", "Cocktails"], "status": "Open"}
    ],
    "restaurants": [
        {"name": "The Late Birds Lounge", "type": "Restaurant (Social / Brunch)"},
        {"name": "A Cevicheria", "type": "Restaurant (Seafood / Trendy)"},
        {"name": "Príncipe do Calhariz", "type": "Restaurant (Traditional / Social)"},
        {"name": "Tapisco", "type": "Restaurant (Tapas / Social)"},
        {"name": "Copenhagen Coffee Lab", "type": "Cafe (Specialty Coffee)"},
        {"name": "Tartine", "type": "Bakery / Cafe"},
        {"name": "Lost In", "type": "Restaurant (Fusion / Terrace)"},
        {"name": "Fábrica Coffee Roasters", "type": "Cafe (Artisanal Coffee)"},
        {"name": "Manteigaria", "type": "Bakery (Pastel de Nata)"},
        {"name": "Time Out Market (Lisboa)", "type": "Food Court (Diverse / Social)"}
    ],
    "safetyScore": 9,
    "saunas": [
        {"name": "Trombeta Bath", "type": "Sauna", "tags": ["Modern", "Central", "Steam"]},
        {"name": "Sauna Olaias", "type": "Sauna", "tags": ["Large", "Pool", "Cinema"]},
        {"name": "Sauna Thermas do Loreto", "type": "Sauna", "tags": ["Historic", "Mature", "Local"]},
        {"name": "The Late Birds Sauna", "type": "Sauna", "tags": ["Private", "Hotel Guests Only"]}
    ],
    "stores": [
        {"name": "Mister B Lisbon", "type": "Store (Fetish / Apparel)"},
        {"name": "Up Your Alley", "type": "Store (Leather / Gear)"},
        {"name": "Embaixada", "type": "Store (Concept Mall / Boutique)"},
        {"name": "Ler Devagar", "type": "Store (Bookstore / Artsy)"},
        {"name": "A Vida Portuguesa", "type": "Store (Gifts / Traditional)"},
        {"name": "A Ginjinha", "type": "Store (Traditional Liquor)"}
    ],
    "tours": [
        {"name": "Lisbon Queer History Walk", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Moderate"},
        {"name": "Lisbon Pride & Heritage Walking Tour", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Private LGBTQ Nightlife & Bar Crawl", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Sintra & Cascais Full-Day Trip", "activityLevel": "Moderate", "estimatedTime": "8 Hours", "pricingGuide": "Luxury"},
        {"name": "Belém Tower & Monastery Heritage", "activityLevel": "Low", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Alfama Fado & Tapas Night Walk", "activityLevel": "Moderate", "estimatedTime": "3.5 Hours", "pricingGuide": "Moderate"},
        {"name": "Tagus River Sunset Sailing Cruise", "activityLevel": "Low", "estimatedTime": "2 Hours", "pricingGuide": "Moderate"},
        {"name": "Lisbon Seven Hills Electric Bike", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Arrábida Kayak & Snorkel Adventure", "activityLevel": "High", "estimatedTime": "6 Hours", "pricingGuide": "Luxury"},
        {"name": "Lisbon Street Food Experience", "activityLevel": "Moderate", "estimatedTime": "3.5 Hours", "pricingGuide": "Budget"},
        {"name": "Tile Painting Workshop (Azulejo)", "activityLevel": "Low", "estimatedTime": "2 Hours", "pricingGuide": "Moderate"},
        {"name": "Fátima & Óbidos Private Tour", "activityLevel": "Low", "estimatedTime": "8 Hours", "pricingGuide": "Luxury"},
        {"name": "Lisbon Tram 28 Historic Ride", "activityLevel": "Low", "estimatedTime": "1 Hour", "pricingGuide": "Budget"},
        {"name": "Évora Roman Temple & Bone Chapel", "activityLevel": "Moderate", "estimatedTime": "9 Hours", "pricingGuide": "Luxury"},
        {"name": "Lisbon Street Art & Mural Walk", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Algarve Coastal Day Trip (Private)", "activityLevel": "Moderate", "estimatedTime": "12 Hours", "pricingGuide": "Luxury"},
        {"name": "Portuguese Cooking Class (Pastel)", "activityLevel": "Low", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"}
    ]
}

with open('/home/user/PrideTravelScoutAPP/destinations.json', 'r') as f:
    file_lines = f.readlines()

print(f"Original: {len(file_lines)} lines")

updates = []
for city_key, city_data in [('ho chi minh city', hcmc_data), ('lisbon', lisbon_data)]:
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
