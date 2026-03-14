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

manuel_antonio_data = {
    "baseFare": [400, 900],
    "hotels": [
        {"name": "Hotel Villa Roca", "type": "Mid-Priced", "tags": ["LGBTQ Owned & Operated", "Men-Only"]},
        {"name": "Oasis Diverse Adult Retreat", "type": "Mid-Priced", "tags": ["LGBTQ Owned & Operated", "Clothing Optional"]},
        {"name": "Tico Tico Villas", "type": "Moderate", "tags": ["LGBTQ Owned & Operated", "Adults Only"]},
        {"name": "Shana by the Beach", "type": "Luxury", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "Gaia Hotel & Reserve", "type": "Luxury", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "Hotel Makanda by the Sea", "type": "Luxury", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "The Falls Resort", "type": "Mid-Priced", "tags": ["IGLTA Member", "LGBTQ Friendly"]},
        {"name": "Issimo Suites Boutique Hotel", "type": "Luxury", "tags": ["LGBTQ Friendly", "Adults Only"]},
        {"name": "Coyaba Tropical", "type": "Moderate", "tags": ["LGBTQ Owned & Operated"]},
        {"name": "Tabulia Tree Hotel and Villas", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Arenas Del Mar Resort", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel Mono Azul", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Villas Jacquelina", "type": "Budget", "tags": ["LGBTQ Friendly"]},
        {"name": "La Foresta Nature Resort", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Tulemar Resort", "type": "Luxury", "tags": ["LGBTQ Friendly"]}
    ],
    "iata": "XQP",
    "image": "&#127464;&#127479;",
    "lgbtqDistrict": "Manuel Antonio Village",
    "lgbtqSafety": "Costa Rica: Very Safe. Manuel Antonio is one of Latin America's most LGBTQ+-welcoming destinations.",
    "monthlyWeather": {
        "0": {"high": "88°F", "low": "72°F", "summary": "Hot and dry; peak travel season.", "gear": "Linen shirts, shorts, sunglasses."},
        "1": {"high": "89°F", "low": "72°F", "summary": "Dry and sunny; clear skies.", "gear": "Breathable fabrics, sunscreen."},
        "2": {"high": "90°F", "low": "73°F", "summary": "Hottest month; intense tropical sun.", "gear": "Light cotton, hat, UV protection."},
        "3": {"high": "89°F", "low": "74°F", "summary": "Warm with occasional light showers.", "gear": "Hydration gear, light tanks."},
        "4": {"high": "87°F", "low": "75°F", "summary": "Transition to wet season; humid.", "gear": "Portable fan, light raincoat."},
        "5": {"high": "86°F", "low": "74°F", "summary": "Lush and green; afternoon rain likely.", "gear": "Umbrella, waterproof bag."},
        "6": {"high": "85°F", "low": "74°F", "summary": "Warm with regular tropical showers.", "gear": "Quick-dry clothes, sandals."},
        "7": {"high": "85°F", "low": "74°F", "summary": "Tropical climate; heavy afternoon rain.", "gear": "Rain poncho, light layers."},
        "8": {"high": "84°F", "low": "73°F", "summary": "Wet season peak; verdant rainforest.", "gear": "Sturdy umbrella, waterproof shoes."},
        "9": {"high": "84°F", "low": "73°F", "summary": "Rain decreases; high humidity.", "gear": "Moisture-wicking gear."},
        "10": {"high": "85°F", "low": "72°F", "summary": "Transition to dry; pleasant evenings.", "gear": "Light sweater for AC, jeans."},
        "11": {"high": "87°F", "low": "72°F", "summary": "Dry season returns; festive vibe.", "gear": "Summer attire, light layers."}
    },
    "name": "Manuel Antonio, Costa Rica",
    "nightlife": [
        {"name": "Mogambo Bar", "type": "Bar/Club", "tags": ["Iconic", "Social", "Happy Hour"], "status": "Open"},
        {"name": "Drunken Monkey Bar", "type": "Bar/Club", "tags": ["Dance", "Pop", "High Energy"], "status": "Open"},
        {"name": "Latino Lounge (Upstairs Bar)", "type": "Bar/Club", "tags": ["Local", "Social", "Queer-Operated"], "status": "Open"},
        {"name": "Liquid Nightclub", "type": "Bar/Club", "tags": ["Dance", "Electronic", "Late Night"], "status": "Open"},
        {"name": "Sunday Sunset Session", "type": "Bar/Club", "tags": ["Pool Party", "Social", "Weekly"], "status": "Active"},
        {"name": "Pride on the Beach", "type": "Bar/Club", "tags": ["Event Series", "Seasonal"], "status": "Active"}
    ],
    "restaurants": [
        {"name": "Latino Lounge", "type": "Restaurant (Gay-Owned / Latin)"},
        {"name": "El Patio de Café Milagro", "type": "Cafe / Restaurant (Inclusive Hub)"},
        {"name": "Emilio's Cafe", "type": "Cafe / Bakery (Views / Social)"},
        {"name": "Falafel Bar", "type": "Restaurant (Middle Eastern / Social)"},
        {"name": "Soda Sánchez", "type": "Restaurant (Traditional / Inclusive)"},
        {"name": "Agua Azul", "type": "Restaurant (Seafood / Social)"},
        {"name": "Ronny's Place", "type": "Restaurant (Sunset Views / Social)"},
        {"name": "Marlin Restaurant", "type": "Restaurant (Beachfront / Inclusive)"}
    ],
    "safetyScore": 8,
    "saunas": [
        {"name": "Playita Club", "type": "Sauna", "tags": ["Men-only", "Pool", "Cruising"]},
        {"name": "Oasis Diverse Retreat Spa", "type": "Sauna", "tags": ["Wellness", "Clothing Optional"]}
    ],
    "stores": [
        {"name": "Quepos Farmers Market", "type": "Store (Artisanal / Social Hub)"},
        {"name": "Boutique Gaia", "type": "Store (High-end Gifts / Fashion)"},
        {"name": "Regalos Nosara", "type": "Store (Local Crafts / Gifts)"},
        {"name": "Tulemar Store", "type": "Store (Boutique Fashion)"}
    ],
    "tours": [
        {"name": "Gay-Only Catamaran Cruise", "activityLevel": "Low", "estimatedTime": "4 Hours", "pricingGuide": "Luxury"},
        {"name": "Gay-Only Waterfall Adventure", "activityLevel": "Moderate", "estimatedTime": "5 Hours", "pricingGuide": "Moderate"},
        {"name": "National Park Guided Walk", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Budget"},
        {"name": "Damane Mangrove Kayaking", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Quepos Sunset Sailing & Snorkel", "activityLevel": "Low", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Rainmaker Conservation Hike", "activityLevel": "High", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Chocolate & Coffee Farm Tour", "activityLevel": "Low", "estimatedTime": "2.5 Hours", "pricingGuide": "Moderate"},
        {"name": "ATV Jungle Adventure", "activityLevel": "High", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Parasailing Over the Bay", "activityLevel": "Low", "estimatedTime": "1 Hour", "pricingGuide": "Luxury"},
        {"name": "Night Jungle Walking Tour", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Kids Saving the Rainforest Visit", "activityLevel": "Low", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Jaco Adventure Day Trip", "activityLevel": "High", "estimatedTime": "8 Hours", "pricingGuide": "Luxury"},
        {"name": "Scuba Diving Caño Island", "activityLevel": "High", "estimatedTime": "10 Hours", "pricingGuide": "Luxury"},
        {"name": "Santa Juana Rural Mountain Tour", "activityLevel": "Moderate", "estimatedTime": "6 Hours", "pricingGuide": "Luxury"},
        {"name": "Surfing Lessons Espadilla", "activityLevel": "High", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Ocean Kayak & Snorkeling", "activityLevel": "High", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Manuel Antonio Horseback Riding", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"}
    ]
}

medellin_data = {
    "baseFare": [400, 900],
    "hotels": [
        {"name": "Marquee Medellin", "type": "Luxury", "tags": ["LGBTQ Friendly", "IGLTA Member"]},
        {"name": "The Charlee Hotel", "type": "Luxury", "tags": ["LGBTQ Friendly", "Iconic Hub"]},
        {"name": "Click Clack Hotel Medellín", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "Design-led"]},
        {"name": "Poblado Guest House", "type": "Moderate", "tags": ["LGBTQ Owned & Operated"]},
        {"name": "23 Hotel Medellin", "type": "Luxury", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "Celestino Boutique Hotel", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "IGLTA Member"]},
        {"name": "York Luxury Suites", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel Park 10", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Medellín Vibes", "type": "Budget", "tags": ["LGBTQ Friendly", "Social"]},
        {"name": "The Art Hotel", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Diez Hotel Categoria Colombia", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Selina Poblado Medellin", "type": "Budget", "tags": ["LGBTQ Friendly", "Social Hub"]},
        {"name": "Hotel Dann Carlton Medellín", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Movich Hotel Las Lomas", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Novotel Medellín El Tesoro", "type": "Moderate", "tags": ["LGBTQ Friendly"]}
    ],
    "iata": "MDE",
    "image": "&#127464;&#127476;",
    "lgbtqDistrict": "El Poblado / Parque Lleras",
    "lgbtqSafety": "Colombia: Generally safe in tourist areas. El Poblado is the hub for nightlife and LGBTQ+ spaces.",
    "monthlyWeather": {
        "0": {"high": "82°F", "low": "63°F", "summary": "Warm, breezy, and mostly sunny.", "gear": "Light sweaters for night, jeans."},
        "1": {"high": "82°F", "low": "63°F", "summary": "\"City of Eternal Spring\" feel; pleasant.", "gear": "T-shirts, light layers."},
        "2": {"high": "81°F", "low": "64°F", "summary": "Sunny mornings; occasional afternoon rain.", "gear": "Sunglasses, light rain shell."},
        "3": {"high": "80°F", "low": "64°F", "summary": "Humid; frequent tropical showers.", "gear": "Umbrella, moisture-wicking gear."},
        "4": {"high": "79°F", "low": "64°F", "summary": "Wettest month; overcast and verdant.", "gear": "Rain poncho, waterproof shoes."},
        "5": {"high": "80°F", "low": "64°F", "summary": "Rainy and lush; cooling evening winds.", "gear": "Waterproof bag, light fleece."},
        "6": {"high": "82°F", "low": "63°F", "summary": "Drier \"summer\"; clear blue skies.", "gear": "Summer attire, sun hat."},
        "7": {"high": "83°F", "low": "63°F", "summary": "Warmest daytime highs; breezy.", "gear": "Linen shirts, sunglasses."},
        "8": {"high": "82°F", "low": "63°F", "summary": "Mild and pleasant; flower festival time.", "gear": "T-shirts, light evening jacket."},
        "9": {"high": "80°F", "low": "63°F", "summary": "Variable rain; warm afternoons.", "gear": "Versatile layers, portable umbrella."},
        "10": {"high": "79°F", "low": "63°F", "summary": "Wet transition; cloudy and damp.", "gear": "Rain jacket, comfortable sneakers."},
        "11": {"high": "80°F", "low": "63°F", "summary": "Drier air returns; festive atmosphere.", "gear": "Summer attire, light layers."}
    },
    "name": "Medellin, Colombia",
    "nightlife": [
        {"name": "Industry Club", "type": "Bar/Club", "tags": ["Iconic", "Dance", "Circuit"], "status": "Open"},
        {"name": "Oráculo", "type": "Bar/Club", "tags": ["High Energy", "Drag", "Pop"], "status": "Open"},
        {"name": "Bar Chiquita", "type": "Bar/Club", "tags": ["Kitsch", "Cocktails", "Pop"], "status": "Open"},
        {"name": "Querida", "type": "Bar/Club", "tags": ["Drag", "Social", "Neighborhood"], "status": "Open"},
        {"name": "Donde Aquiles", "type": "Bar/Club", "tags": ["Local", "Social", "Traditional"], "status": "Open"},
        {"name": "Zero Bar", "type": "Bar/Club", "tags": ["Cocktails", "Pre-party", "Social"], "status": "Open"},
        {"name": "La Cantina de Javi", "type": "Bar/Club", "tags": ["Karaoke", "Social", "Local"], "status": "Open"},
        {"name": "Sweet Night", "type": "Bar/Club", "tags": ["Strip Show", "Men-only", "Social"], "status": "Open"},
        {"name": "Punto Zero", "type": "Bar/Club", "tags": ["Dance", "Pop", "Youth"], "status": "Open"}
    ],
    "restaurants": [
        {"name": "Bar Chiquita", "type": "Restobar (Kitsch / Social)"},
        {"name": "Carmen", "type": "Restaurant (Contemporary Colombian)"},
        {"name": "Oci.Mde", "type": "Restaurant (Modern Fusion)"},
        {"name": "Hija Mía Coffee Roasters", "type": "Cafe (Inclusive Hub)"},
        {"name": "Pergamino Coffee", "type": "Cafe (Social Hub / Local Coffee)"},
        {"name": "Alambique", "type": "Restaurant (Artsy / Rooftop)"},
        {"name": "Mondongos", "type": "Restaurant (Traditional / Social)"},
        {"name": "Crepes & Waffles", "type": "Restaurant (Inclusive / Women-led)"},
        {"name": "Azul Selva", "type": "Cafe (Brunch / Healthy)"},
        {"name": "Velvet", "type": "Cafe / Bakery"}
    ],
    "safetyScore": 7,
    "saunas": [
        {"name": "Sauna Acuario", "type": "Sauna", "tags": ["Pool", "Steam", "Cruising"]},
        {"name": "Sauna Vitraus", "type": "Sauna", "tags": ["Modern", "Gym", "Massage"]},
        {"name": "Sauna Neptuno", "type": "Sauna", "tags": ["Local", "Mature", "Social"]},
        {"name": "Sauna Odin", "type": "Sauna", "tags": ["Private Rooms", "Cruising"]}
    ],
    "stores": [
        {"name": "Via Primavera Boutiques", "type": "Fashion / Local Designers"},
        {"name": "El Tesoro Shopping Park", "type": "High-end / Inclusive Retail"},
        {"name": "Makeno", "type": "Store (Concept Store / Fashion)"},
        {"name": "Underwear Shop Medellin", "type": "Store (Apparel / Underwear)"},
        {"name": "TRUE", "type": "Store (Streetwear / LGBTQ-popular)"}
    ],
    "tours": [
        {"name": "Medellín Queer History & Comuna 13", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "LGBTQ Nightlife Safari (Poblado)", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Gay-Friendly Coffee Farm Experience", "activityLevel": "Moderate", "estimatedTime": "6 Hours", "pricingGuide": "Luxury"},
        {"name": "Comuna 13 Graffiti Tour", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Guatapé & El Peñol Day Trip", "activityLevel": "High", "estimatedTime": "10 Hours", "pricingGuide": "Moderate"},
        {"name": "Pablo Escobar History: Fact vs Fiction", "activityLevel": "Low", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Real City Free Walking Tour", "activityLevel": "Moderate", "estimatedTime": "3.5 Hours", "pricingGuide": "Budget"},
        {"name": "Salsa Lesson in Laureles", "activityLevel": "High", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Metrocable & Arví Park Discovery", "activityLevel": "Moderate", "estimatedTime": "5 Hours", "pricingGuide": "Budget"},
        {"name": "Exotic Fruit Market Tour", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Private Helicopter City Flyover", "activityLevel": "Low", "estimatedTime": "20 Minutes", "pricingGuide": "Luxury"},
        {"name": "Botanical Garden & Orquideorama Walk", "activityLevel": "Low", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Paragliding Over the Valley", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Museum of Antioquia Guided Tour", "activityLevel": "Low", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Silleteros Flower Farm (Santa Elena)", "activityLevel": "Moderate", "estimatedTime": "5 Hours", "pricingGuide": "Moderate"},
        {"name": "Antioquian Gastronomy Journey", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Barefoot Park & Interactive Museum", "activityLevel": "Low", "estimatedTime": "3 Hours", "pricingGuide": "Budget"}
    ]
}

with open('/home/user/PrideTravelScoutAPP/destinations.json', 'r') as f:
    file_lines = f.readlines()

print(f"Original: {len(file_lines)} lines")

updates = []
for city_key, city_data in [('manuel antonio', manuel_antonio_data), ('medellin', medellin_data)]:
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
