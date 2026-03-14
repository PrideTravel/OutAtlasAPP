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

melbourne_data = {
    "baseFare": [900, 1800],
    "hotels": [
        {"name": "Adelphi Hotel", "type": "Luxury", "tags": ["World Rainbow Hotels", "LGBTQ Friendly"]},
        {"name": "169 Drummond St", "type": "Moderate", "tags": ["LGBTQ Owned & Operated", "B&B"]},
        {"name": "The Prince Hotel", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "Iconic Hub"]},
        {"name": "Crown Towers Melbourne", "type": "Luxury", "tags": ["LGBTQ Friendly", "5-Star"]},
        {"name": "W Melbourne", "type": "Luxury", "tags": ["LGBTQ Friendly", "High Design"]},
        {"name": "The Olsen Melbourne - Art Series", "type": "Luxury", "tags": ["LGBTQ Friendly", "IGLTA Member"]},
        {"name": "Roamer St Kilda", "type": "Budget", "tags": ["LGBTQ Friendly", "Social Hub"]},
        {"name": "Lylo Melbourne", "type": "Budget", "tags": ["LGBTQ Friendly", "Boutique Hostel"]},
        {"name": "The Cullen Melbourne - Art Series", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "QT Melbourne", "type": "Luxury", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "Ovolo South Yarra", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "Retro-Chic"]},
        {"name": "The Langham Melbourne", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "InterContinental Melbourne The Rialto", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Mantra on the Park", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Quest St Kilda Bayside", "type": "Moderate", "tags": ["LGBTQ Friendly"]}
    ],
    "iata": "MEL",
    "image": "&#127462;&#127482;",
    "lgbtqDistrict": "St Kilda / Fitzroy",
    "lgbtqSafety": "Australia: Very Safe. Melbourne has one of the most vibrant and established LGBTQ+ scenes in the Southern Hemisphere.",
    "monthlyWeather": {
        "0": {"high": "81°F", "low": "61°F", "summary": "Warm to hot; sudden heatwaves likely.", "gear": "T-shirts, shorts, sunglasses, sunscreen."},
        "1": {"high": "81°F", "low": "61°F", "summary": "Peak summer heat; dry and sunny.", "gear": "Linen fabrics, UV protection, hat."},
        "2": {"high": "75°F", "low": "57°F", "summary": "Pleasant and mild; transition to autumn.", "gear": "Light layers, jeans for evening."},
        "3": {"high": "68°F", "low": "52°F", "summary": "Crisp air; beautiful autumn foliage.", "gear": "Light jacket, long-sleeve shirts."},
        "4": {"high": "62°F", "low": "49°F", "summary": "Chilly mornings; frequent light drizzle.", "gear": "Cardigan, raincoat, sneakers."},
        "5": {"high": "57°F", "low": "45°F", "summary": "Coldest and most humid month.", "gear": "Heavy coat, thermal layers, scarf."},
        "6": {"high": "56°F", "low": "43°F", "summary": "Chilly with biting southern winds.", "gear": "Windproof jacket, warm boots."},
        "7": {"high": "59°F", "low": "45°F", "summary": "Chilly but clearer skies begin.", "gear": "Rain shell, layered sweaters."},
        "8": {"high": "63°F", "low": "48°F", "summary": "Mild transition; highly variable weather.", "gear": "Umbrella, windbreaker, layered tops."},
        "9": {"high": "67°F", "low": "51°F", "summary": "Wettest month; unpredictable showers.", "gear": "Waterproof jacket, comfortable boots."},
        "10": {"high": "72°F", "low": "55°F", "summary": "Warm spring days; ideal for walking.", "gear": "T-shirts, light evening layer."},
        "11": {"high": "77°F", "low": "59°F", "summary": "Summer heat returns; breezy evenings.", "gear": "Summer attire, light evening jacket."}
    },
    "name": "Melbourne, Australia",
    "nightlife": [
        {"name": "The Laird", "type": "Bar/Club", "tags": ["Bear", "Leather", "Men-only", "Pub"], "status": "Open"},
        {"name": "Poof Doof", "type": "Bar/Club", "tags": ["Dance", "Pop", "High Energy", "Iconic"], "status": "Open"},
        {"name": "The Peel Hotel", "type": "Bar/Club", "tags": ["Iconic", "Dance", "Late Night"], "status": "Open"},
        {"name": "Sircuit", "type": "Bar/Club", "tags": ["Drag", "Dance", "Mixed Crowd"], "status": "Open"},
        {"name": "Pride of our Footscray", "type": "Bar/Club", "tags": ["Community Bar", "Theatre", "Drag"], "status": "Open"},
        {"name": "The Glasshouse Hotel", "type": "Bar/Club", "tags": ["Cabaret", "Drag", "Social"], "status": "Open"},
        {"name": "UBQ", "type": "Bar/Club", "tags": ["Alternative", "Queer", "Performance"], "status": "Open"},
        {"name": "Yah Yah's", "type": "Bar/Club", "tags": ["Live Music", "Alternative", "Queer-friendly"], "status": "Open"},
        {"name": "Libation", "type": "Bar/Club", "tags": ["Cocktails", "Social", "Neighborhood"], "status": "Open"},
        {"name": "Njoy", "type": "Bar/Club", "tags": ["Lounge", "Social", "CBD"], "status": "Open"},
        {"name": "Sundaylicious", "type": "Bar/Club", "tags": ["Pop-up Party", "High Energy", "Dance"], "status": "Active"},
        {"name": "Pinkalicious", "type": "Bar/Club", "tags": ["Monthly", "Lesbian-centric", "Dance"], "status": "Active"},
        {"name": "T-Bird Club", "type": "Bar/Club", "tags": ["Trans-inclusive", "Alternative", "Dance"], "status": "Open"}
    ],
    "restaurants": [
        {"name": "Chin Chin", "type": "Restaurant (Asian Fusion / Iconic)"},
        {"name": "Follow the Leader Cafe", "type": "Cafe (Gay-popular / Brunch)"},
        {"name": "St Edmonds Cafe", "type": "Cafe (Artsy / Social Hub)"},
        {"name": "Amici On Chapel", "type": "Cafe (Social / Sweets)"},
        {"name": "Bomb Cafe Abbotsford", "type": "Cafe (Social / Casual)"},
        {"name": "Flower Drum", "type": "Restaurant (Fine Dining / Cantonese)"},
        {"name": "Don Don", "type": "Restaurant (Quick Service / Japanese)"},
        {"name": "Victorian Pride Centre Cafe", "type": "Cafe (Community Hub)"}
    ],
    "safetyScore": 9,
    "saunas": [
        {"name": "Wet on Wellington", "type": "Sauna", "tags": ["Largest", "Pool", "Steam", "Cruising"]},
        {"name": "Spartacus Lounge", "type": "Sauna", "tags": ["CBD", "Modern", "Cinema", "Cruising"]},
        {"name": "Bay City Sauna", "type": "Sauna", "tags": ["Traditional", "Mature", "Local"]},
        {"name": "Ram Lounge @ Club X", "type": "Sauna", "tags": ["CBD", "Arcade", "Cruising"]}
    ],
    "stores": [
        {"name": "Hares & Hyenas", "type": "LGBTQ+ Bookstore & Performance Space"},
        {"name": "Eagle Leather", "type": "Store (Fetish / Leather / Gear)"},
        {"name": "Blender Studios", "type": "Store (Art / Independent Crafts)"},
        {"name": "The Bookshop Darlinghurst (Online)", "type": "Store (Books / Inclusive Culture)"},
        {"name": "Minotaur", "type": "Store (Pop Culture / Inclusive)"}
    ],
    "tours": [
        {"name": "Melbourne Queer Heritage Walk", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Budget"},
        {"name": "Street Art Tour with Local Artist", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Great Ocean Road & 12 Apostles Day Trip", "activityLevel": "Moderate", "estimatedTime": "12 Hours", "pricingGuide": "Moderate"},
        {"name": "Phillip Island Penguin Parade Tour", "activityLevel": "Low", "estimatedTime": "8 Hours", "pricingGuide": "Moderate"},
        {"name": "Spirit of Melbourne Dinner Cruise", "activityLevel": "Low", "estimatedTime": "3 Hours", "pricingGuide": "Luxury"},
        {"name": "Yarra Valley Wine & Cider Tasting", "activityLevel": "Low", "estimatedTime": "8 Hours", "pricingGuide": "Luxury"},
        {"name": "Melbourne Coffee Culture Walk", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Melbourne Lanes & Arcades Walk", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Puffing Billy Steam Train Experience", "activityLevel": "Low", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Old Melbourne Gaol Ghost Tour", "activityLevel": "Moderate", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"},
        {"name": "Mornington Peninsula Hot Springs", "activityLevel": "Low", "estimatedTime": "9 Hours", "pricingGuide": "Luxury"},
        {"name": "Healesville Sanctuary Wildlife Tour", "activityLevel": "Moderate", "estimatedTime": "7 Hours", "pricingGuide": "Moderate"},
        {"name": "Melbourne Skydeck Edge Experience", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"},
        {"name": "Queen Victoria Market Foodie Tour", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Ballarat & Sovereign Hill Gold Rush", "activityLevel": "Moderate", "estimatedTime": "9 Hours", "pricingGuide": "Moderate"}
    ]
}

montevideo_data = {
    "baseFare": [600, 1200],
    "hotels": [
        {"name": "Hyatt Centric Montevideo", "type": "Luxury", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "Soro Montevideo, Curio Collection", "type": "Mid-Priced", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "Sofitel Montevideo Casino Carrasco", "type": "Luxury", "tags": ["LGBTQ Friendly", "World Rainbow"]},
        {"name": "Aloft Montevideo Hotel", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "IGLTA Member"]},
        {"name": "After Hotel Montevideo", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel Costanero MGallery", "type": "Luxury", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "Alma Histórica Boutique Hotel", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "Don Boutique Hotel", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "NH Columbia", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Radisson Montevideo Victoria Plaza", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Dazzler by Wyndham Montevideo", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Hilton Garden Inn Montevideo", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Cala di Volpe Boutique Hotel", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Splendido Hotel", "type": "Budget", "tags": ["LGBTQ Friendly", "Historic"]},
        {"name": "Circus Hostel & Hotel", "type": "Budget", "tags": ["LGBTQ Friendly", "Social Hub"]}
    ],
    "iata": "MVD",
    "image": "&#127482;&#127486;",
    "lgbtqDistrict": "Ciudad Vieja / Barrio Sur",
    "lgbtqSafety": "Uruguay: Very Safe. One of Latin America's most LGBTQ+-progressive countries with same-sex marriage since 2013.",
    "monthlyWeather": {
        "0": {"high": "83°F", "low": "64°F", "summary": "Warm summer; breezy Atlantic air.", "gear": "T-shirts, shorts, light evening layer."},
        "1": {"high": "82°F", "low": "64°F", "summary": "Humid but sunny; peak beach season.", "gear": "Swimwear, sunscreen, sunglasses."},
        "2": {"high": "78°F", "low": "61°F", "summary": "Pleasant autumn transition; dry.", "gear": "Light layers, jeans for evening."},
        "3": {"high": "71°F", "low": "55°F", "summary": "Crisp air; beautiful fall foliage.", "gear": "Light jacket, long-sleeve shirts."},
        "4": {"high": "64°F", "low": "49°F", "summary": "Chilly mornings; frequent light rain.", "gear": "Cardigan, raincoat, sneakers."},
        "5": {"high": "59°F", "low": "45°F", "summary": "Coldest month; damp sea winds.", "gear": "Heavy coat, scarves, waterproof boots."},
        "6": {"high": "58°F", "low": "45°F", "summary": "Chilly and overcast; short days.", "gear": "Wool sweaters, winter jacket."},
        "7": {"high": "61°F", "low": "46°F", "summary": "Cool transition; breezy spring air.", "gear": "Rain shell, warm layers."},
        "8": {"high": "65°F", "low": "49°F", "summary": "Bright spring; variable weather.", "gear": "Windbreaker, layered tops, umbrella."},
        "9": {"high": "71°F", "low": "54°F", "summary": "Sunny days; ideal for sightseeing.", "gear": "Light sweater, sunglasses."},
        "10": {"high": "76°F", "low": "58°F", "summary": "Warm spring; blooming parks.", "gear": "T-shirts, light evening jacket."},
        "11": {"high": "81°F", "low": "62°F", "summary": "Summer returns; long sunny evenings.", "gear": "Summer attire, light layers."}
    },
    "name": "Montevideo, Uruguay",
    "nightlife": [
        {"name": "Chains Pub", "type": "Bar/Club", "tags": ["Iconic", "Social", "Pop"], "status": "Open"},
        {"name": "Il Tempo", "type": "Bar/Club", "tags": ["Dance", "Drag", "Show", "High Energy"], "status": "Open"},
        {"name": "Small Club", "type": "Bar/Club", "tags": ["Alternative", "Electronic", "Queer"], "status": "Open"},
        {"name": "Tiziano", "type": "Bar/Club", "tags": ["Social", "Cocktails", "Local"], "status": "Open"},
        {"name": "Cain Club", "type": "Bar/Club", "tags": ["Dance", "Pop", "Youthful"], "status": "Open"},
        {"name": "Bar Lola", "type": "Bar/Club", "tags": ["Alternative", "Artsy", "Mixed"], "status": "Open"},
        {"name": "La Cretina", "type": "Bar/Club", "tags": ["Artsy", "Social", "Patio"], "status": "Open"}
    ],
    "restaurants": [
        {"name": "Es Mercat", "type": "Restaurant (Seafood / Social)"},
        {"name": "Jacinto", "type": "Restaurant (Bakery / Bistro)"},
        {"name": "Estrecho", "type": "Restaurant (French-Uruguayan / Social)"},
        {"name": "Sin Pretensiones", "type": "Cafe / Restaurant (Traditional)"},
        {"name": "Democracia Cafetería", "type": "Cafe (Social Hub / Inclusive)"},
        {"name": "Escaramuza", "type": "Cafe / Bookstore (Artsy Hub)"},
        {"name": "Primuseum", "type": "Restaurant (Tango / Dinner Show)"},
        {"name": "Mercado del Puerto", "type": "Food Court (Steakhouse Hub)"},
        {"name": "La Farmacia", "type": "Cafe (Historic / Social)"},
        {"name": "Candy Bar", "type": "Cafe / Bistro (Neighborhood)"}
    ],
    "safetyScore": 8,
    "saunas": [
        {"name": "Sauna Horus", "type": "Sauna", "tags": ["Modern", "Steam", "Cruising"]},
        {"name": "Sauna Zeus", "type": "Sauna", "tags": ["Traditional", "Mature", "Local"]}
    ],
    "stores": [
        {"name": "Escaramuza Libros", "type": "Bookstore (Inclusive Culture)"},
        {"name": "Puro Verso", "type": "Bookstore (Historic / Art)"},
        {"name": "Mercado de los Artesanos", "type": "Store (Artisanal / Local)"},
        {"name": "Sinergia Design", "type": "Store (Concept Store / Boutique)"},
        {"name": "Tristán Narvaja Market", "type": "Store (Antiques / Sunday Hub)"}
    ],
    "tours": [
        {"name": "Montevideo Queer History Walk", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Budget"},
        {"name": "Uruguayan Wine & Tannat Experience", "activityLevel": "Low", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Ciudad Vieja Architecture & History", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Colonia del Sacramento Day Trip", "activityLevel": "Moderate", "estimatedTime": "10 Hours", "pricingGuide": "Luxury"},
        {"name": "Punta del Este Full-Day Tour", "activityLevel": "Low", "estimatedTime": "9 Hours", "pricingGuide": "Luxury"},
        {"name": "Montevideo Rambla Sunset Bike Tour", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Carnaval Museum & Drums Experience", "activityLevel": "Low", "estimatedTime": "2.5 Hours", "pricingGuide": "Budget"},
        {"name": "Tristán Narvaja Sunday Market Walk", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Mercado del Puerto Gastronomy Tour", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Candombe Drumming Workshop", "activityLevel": "High", "estimatedTime": "1.5 Hours", "pricingGuide": "Moderate"},
        {"name": "Legislative Palace Heritage Tour", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"},
        {"name": "Private Photography Tour Montevideo", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Olive Oil & Rural Farm Visit", "activityLevel": "Low", "estimatedTime": "5 Hours", "pricingGuide": "Moderate"},
        {"name": "Soccer History: Centenario Stadium", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Parque Rodó Arts & Lake Walk", "activityLevel": "Low", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "LGBTQ+ Nightlife Bar Crawl", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Maté Tea Culture Experience", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"}
    ]
}

with open('/home/user/PrideTravelScoutAPP/destinations.json', 'r') as f:
    file_lines = f.readlines()

print(f"Original: {len(file_lines)} lines")

updates = []
for city_key, city_data in [('melbourne', melbourne_data), ('montevideo', montevideo_data)]:
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
