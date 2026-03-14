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

taipei_data = {
    "baseFare": [700, 1400],
    "hotels": [
        {"name": "W Taipei", "type": "Luxury", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "Kimpton Da An Hotel", "type": "Luxury", "tags": ["IGLTA Member", "LGBTQ Friendly"]},
        {"name": "Hotel PaPa Whale", "type": "Moderate", "tags": ["LGBTQ Friendly", "Ximending Hub"]},
        {"name": "CitizenM Taipei North Gate", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "The Red Corner", "type": "Budget", "tags": ["LGBTQ Owned", "Men-Only"]},
        {"name": "Green World Hotel Zhonghua", "type": "Moderate", "tags": ["LGBTQ Friendly", "Near Red House"]},
        {"name": "Just Sleep Ximending", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Amba Taipei Ximending", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Humble House Taipei", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Play Design Hotel", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "Meander Taipei Hostel", "type": "Budget", "tags": ["LGBTQ Friendly"]},
        {"name": "Star Hostel Taipei Main Station", "type": "Budget", "tags": ["LGBTQ Friendly"]},
        {"name": "Eslite Hotel", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Home Hotel Da-An", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Swiio Hotel Daan", "type": "Moderate", "tags": ["LGBTQ Friendly"]}
    ],
    "iata": "TPE",
    "image": "&#127481;&#127484;",
    "lgbtqDistrict": "Ximending / Red House",
    "lgbtqSafety": "Taiwan: Very Safe. One of Asia's most LGBTQ+-friendly destinations; same-sex marriage legal since 2019.",
    "monthlyWeather": {
        "0": {"high": "66°F", "low": "57°F", "summary": "Mild and overcast; high humidity.", "gear": "Light jacket, scarf, umbrella."},
        "1": {"high": "68°F", "low": "58°F", "summary": "Pleasant and cool; occasional drizzle.", "gear": "Layered sweaters, light rain shell."},
        "2": {"high": "72°F", "low": "61°F", "summary": "Spring blossoms; breezy and bright.", "gear": "T-shirts, light cardigan, sneakers."},
        "3": {"high": "77°F", "low": "65°F", "summary": "Warm and sunny; peak comfort.", "gear": "Cotton shirts, sunglasses, hat."},
        "4": {"high": "83°F", "low": "70°F", "summary": "Hot and humid; rainy season begins.", "gear": "Breathable fabrics, rain poncho."},
        "5": {"high": "88°F", "low": "74°F", "summary": "Tropical heat; frequent heavy showers.", "gear": "Waterproof bag, quick-dry clothes."},
        "6": {"high": "92°F", "low": "77°F", "summary": "Peak summer heat; intense humidity.", "gear": "Linen, sandals, UV protection."},
        "7": {"high": "93°F", "low": "78°F", "summary": "Sizzling; warm tropical nights.", "gear": "Light tanks, shorts, stay hydrated."},
        "8": {"high": "89°F", "low": "76°F", "summary": "Rainy and windy; typhoon season risk.", "gear": "Sturdy umbrella, waterproof shoes."},
        "9": {"high": "82°F", "low": "72°F", "summary": "Pleasant transition; clear blue skies.", "gear": "Light sweater, sunglasses."},
        "10": {"high": "75°F", "low": "66°F", "summary": "Mild and crisp; beautiful dry days.", "gear": "Jeans, light jacket, layered tops."},
        "11": {"high": "70°F", "low": "60°F", "summary": "Cool and damp; festive winter lights.", "gear": "Winter coat (light), thermal socks."}
    },
    "name": "Taipei, Taiwan",
    "nightlife": [
        {"name": "The Red House Complex", "type": "Bar/Club", "tags": ["Multiple Bars", "Outdoor", "Iconic"], "status": "Open"},
        {"name": "Cafe Dalida", "type": "Bar/Club", "tags": ["Drag", "Cocktails", "Outdoor"], "status": "Open"},
        {"name": "The Secret Garden", "type": "Bar/Club", "tags": ["Social", "Pop", "Ximending"], "status": "Open"},
        {"name": "Locker Room", "type": "Bar/Club", "tags": ["Dance", "Shower Shows", "Drag"], "status": "Open"},
        {"name": "Commander D", "type": "Bar/Club", "tags": ["BDSM", "Fetish", "Shows"], "status": "Open"},
        {"name": "G-Star", "type": "Bar/Club", "tags": ["Dance", "Electronic", "Youth"], "status": "Open"},
        {"name": "Abrazo", "type": "Bar/Club", "tags": ["Upscale", "Cocktails", "Social"], "status": "Open"},
        {"name": "Goldfish", "type": "Bar/Club", "tags": ["Social", "Local", "Friendly"], "status": "Open"},
        {"name": "Hunt Taipei", "type": "Bar/Club", "tags": ["Bear-friendly", "Cruise", "Social"], "status": "Open"},
        {"name": "Taboo", "type": "Bar/Club", "tags": ["Lesbian-centric", "Dance"], "status": "Open"},
        {"name": "Fairy Taipei", "type": "Bar/Club", "tags": ["Artsy", "Cocktails", "Social"], "status": "Open"},
        {"name": "B.E.D. Taipei", "type": "Bar/Club", "tags": ["Dance", "Pop", "Social"], "status": "Open"},
        {"name": "Wonderland", "type": "Bar/Club", "tags": ["Themed", "Performance", "Fun"], "status": "Open"}
    ],
    "restaurants": [
        {"name": "Cafe Dalida", "type": "Cafe (Iconic / Social)"},
        {"name": "Abrazo", "type": "Restaurant (Fusion / Posh Lounge)"},
        {"name": "The Tavernist", "type": "Restaurant (Modern British / Inclusive)"},
        {"name": "Fairy Taipei", "type": "Cafe (Bistro / Artsy)"},
        {"name": "Jin Jin Cafe", "type": "Cafe (Traditional / Social)"},
        {"name": "Yong He Soy Milk King", "type": "Restaurant (Breakfast / Local Hub)"},
        {"name": "Mui Mui", "type": "Restaurant (Thai / Trendy)"},
        {"name": "Woolloomooloo", "type": "Cafe (Australian / Inclusive)"},
        {"name": "Fujin Tree 353 Cafe", "type": "Cafe (Design-led / Social)"},
        {"name": "Din Tai Fung (Xinyi)", "type": "Restaurant (Dumplings / Inclusive)"}
    ],
    "safetyScore": 9,
    "saunas": [
        {"name": "Aniki Luxury Sauna", "type": "Sauna", "tags": ["High-end", "Pool", "Gym", "Cruising"]},
        {"name": "Hao-Man Sauna", "type": "Sauna", "tags": ["Local", "Mature", "Social"]},
        {"name": "Soi 13 Sauna", "type": "Sauna", "tags": ["Modern", "Young Crowd"]},
        {"name": "I-Sauna", "type": "Sauna", "tags": ["Traditional", "Central"]}
    ],
    "stores": [
        {"name": "GinGin Books", "type": "LGBTQ+ Bookstore"},
        {"name": "Commander D Store", "type": "Store (Fetish / Apparel / Toys)"},
        {"name": "Red House Boutique Shops", "type": "Store (Local Crafts / Gifts)"},
        {"name": "Eslite Spectrum", "type": "Store (Independent Designer Hub)"},
        {"name": "GX3 Taipei", "type": "Store (Underwear / Apparel)"}
    ],
    "tours": [
        {"name": "Taipei Queer Culture Walk", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Red House Nightlife Discovery", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "LGBTQ Heritage & Temple Tour", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Taipei 101 Observatory Access", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"},
        {"name": "Yangmingshan National Park Hike", "activityLevel": "High", "estimatedTime": "6 Hours", "pricingGuide": "Moderate"},
        {"name": "Jiufen Old Street & Shifen Day Trip", "activityLevel": "Moderate", "estimatedTime": "8 Hours", "pricingGuide": "Moderate"},
        {"name": "Beitou Hot Springs & Museum", "activityLevel": "Low", "estimatedTime": "4 Hours", "pricingGuide": "Budget"},
        {"name": "Longshan Temple Night Market Walk", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Private Tea Tasting in Maokong", "activityLevel": "Low", "estimatedTime": "3 Hours", "pricingGuide": "Luxury"},
        {"name": "Taipei Street Art & Mural Walk", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "National Palace Museum Highlights", "activityLevel": "Low", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Taipei E-Bike Discovery Tour", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "Taroko Gorge Private Day Trip", "activityLevel": "Moderate", "estimatedTime": "12 Hours", "pricingGuide": "Luxury"},
        {"name": "Night Food Tour: Shilin Market", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Taipei Cooking Class & Market", "activityLevel": "Low", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Yehliu Geopark & North Coast", "activityLevel": "Moderate", "estimatedTime": "7 Hours", "pricingGuide": "Moderate"},
        {"name": "Sun Moon Lake Private Day Trip", "activityLevel": "Low", "estimatedTime": "10 Hours", "pricingGuide": "Luxury"}
    ]
}

torremolinos_data = {
    "baseFare": [500, 1000],
    "hotels": [
        {"name": "Hotel Ritual Torremolinos", "type": "Mid-Priced", "tags": ["LGBTQ Owned & Operated", "IGLTA"]},
        {"name": "Namaste Elite", "type": "Moderate", "tags": ["LGBTQ Owned", "Men-Only"]},
        {"name": "Fenix Torremolinos", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "Adults Only"]},
        {"name": "Meliá Costa del Sol", "type": "Luxury", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "Hotel El Gato", "type": "Moderate", "tags": ["LGBTQ Owned", "Beachfront"]},
        {"name": "Gran Cervantes by Blue Sea", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Sol Torremolinos - Don Pablo", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel Tent Torremolinos", "type": "Budget", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel Isabel", "type": "Mid-Priced", "tags": ["LGBTQ Friendly"]},
        {"name": "MS Amaragua", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Bajondillo Beach Cozy In", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel Princesa Solar", "type": "Moderate", "tags": ["LGBTQ Friendly", "Adults Only"]},
        {"name": "Hotel Natali", "type": "Budget", "tags": ["LGBTQ Friendly"]},
        {"name": "AluaSun Costa Park", "type": "Budget", "tags": ["LGBTQ Friendly"]},
        {"name": "Hotel Griego", "type": "Budget", "tags": ["LGBTQ Friendly"]}
    ],
    "iata": "AGP",
    "image": "&#127466;&#127480;",
    "lgbtqDistrict": "La Nogalera",
    "lgbtqSafety": "Spain: Very Safe. Torremolinos is one of Europe's oldest gay resorts with a large, welcoming LGBTQ+ scene.",
    "monthlyWeather": {
        "0": {"high": "62°F", "low": "47°F", "summary": "Cool, windy, and partly cloudy.", "gear": "Light jacket, jeans, sneakers."},
        "1": {"high": "63°F", "low": "48°F", "summary": "Crisp air; variable winter sun.", "gear": "Sweaters, light scarf, layers."},
        "2": {"high": "66°F", "low": "50°F", "summary": "Pleasant spring start; breezy.", "gear": "T-shirts, light cardigan."},
        "3": {"high": "69°F", "low": "53°F", "summary": "Sunny and bright; ideal for walking.", "gear": "Cotton shirts, sunglasses, hat."},
        "4": {"high": "74°F", "low": "58°F", "summary": "Warm spring; beach season begins.", "gear": "Swimwear, light tanks, shades."},
        "5": {"high": "80°F", "low": "65°F", "summary": "Hot and sunny; peak Pride weather.", "gear": "Linen clothes, sunscreen, sandals."},
        "6": {"high": "84°F", "low": "69°F", "summary": "Sizzling summer; clear blue skies.", "gear": "Light fabrics, UV protection."},
        "7": {"high": "85°F", "low": "70°F", "summary": "Hottest month; warm tropical nights.", "gear": "Shorts, flip-flops, stay hydrated."},
        "8": {"high": "81°F", "low": "66°F", "summary": "Warm transition; lower humidity.", "gear": "T-shirts, light evening sweater."},
        "9": {"high": "74°F", "low": "60°F", "summary": "Mild and crisp; beautiful foliage.", "gear": "Sweaters, trench coat, scarf."},
        "10": {"high": "67°F", "low": "53°F", "summary": "Chilly transition; rainy days return.", "gear": "Waterproof boots, warm hat."},
        "11": {"high": "63°F", "low": "49°F", "summary": "Coldest and wettest; winter lights.", "gear": "Winter coat, thermal socks."}
    },
    "name": "Torremolinos, Spain",
    "nightlife": [
        {"name": "Centuryon", "type": "Bar/Club", "tags": ["Large Club", "Circuit", "Dance"], "status": "Open"},
        {"name": "Aqua Terraza", "type": "Bar/Club", "tags": ["Iconic", "Dance", "Social"], "status": "Open"},
        {"name": "Bears Bar", "type": "Bar/Club", "tags": ["Bear", "Social", "Men-only"], "status": "Open"},
        {"name": "Eagle Bar", "type": "Bar/Club", "tags": ["Fetish", "Leather", "Cruising"], "status": "Open"},
        {"name": "Marta, Cariño!", "type": "Bar/Club", "tags": ["Drag", "Young Crowd", "Dance"], "status": "Open"},
        {"name": "Eden Copas", "type": "Bar/Club", "tags": ["Drag", "Stylish", "Pop"], "status": "Open"},
        {"name": "3 Monkeys", "type": "Bar/Club", "tags": ["Social", "Cocktails", "Happy Hour"], "status": "Open"},
        {"name": "Alcatraz Men's Club", "type": "Bar/Club", "tags": ["Leather", "Fetish", "Cruise"], "status": "Open"},
        {"name": "Mariquita Copas", "type": "Bar/Club", "tags": ["Drag", "Cocktails", "Social"], "status": "Open"},
        {"name": "Baloo Bar Lounge", "type": "Bar/Club", "tags": ["Bear", "Social", "Coffee"], "status": "Open"},
        {"name": "Exxxtreme Cruising Club", "type": "Bar/Club", "tags": ["Fetish", "Cruise", "Men-only"], "status": "Open"},
        {"name": "El 12 Bar", "type": "Bar/Club", "tags": ["Cocktails", "Social", "Terrace"], "status": "Open"},
        {"name": "Pourquoi Pas", "type": "Bar/Club", "tags": ["Historic", "Performance", "Social"], "status": "Open"},
        {"name": "Arcos Gin & Music Bar", "type": "Bar/Club", "tags": ["Gin", "Music", "Terrace"], "status": "Open"},
        {"name": "Vida Bar", "type": "Bar/Club", "tags": ["Social", "Terrace", "Mixed"], "status": "Open"},
        {"name": "Wow", "type": "Bar/Club", "tags": ["Cafe", "Social", "Neighborhood"], "status": "Open"},
        {"name": "Eden Beach Club", "type": "Bar/Club", "tags": ["Beach", "Social", "Restaurant"], "status": "Open"}
    ],
    "restaurants": [
        {"name": "Casero La Comida", "type": "Restaurant (Gay-Owned / Mediterranean)"},
        {"name": "Eden Beach Club", "type": "Restaurant (Beachfront / Social)"},
        {"name": "3 Monkeys", "type": "Restaurant (Pub Food / Social)"},
        {"name": "El Gato Lounge", "type": "Restaurant (Beachfront / Tapas)"},
        {"name": "Vanilla Café", "type": "Cafe (Breakfast / Social Hub)"},
        {"name": "Baloó Bar", "type": "Cafe (Bears / Social)"},
        {"name": "La Biznaga", "type": "Cafe (Local / Social)"},
        {"name": "La Crema", "type": "Restaurant (Spanish / International)"},
        {"name": "Poseidon", "type": "Restaurant (Gay Beach / Seafood)"},
        {"name": "Boca Loca", "type": "Restaurant (Social / Local)"}
    ],
    "safetyScore": 9,
    "saunas": [
        {"name": "Apolo Sauna Cabaret", "type": "Sauna", "tags": ["Large", "Drag Shows", "Pool"]}
    ],
    "stores": [
        {"name": "ES Collection Store", "type": "Store (Apparel / Swimwear)"},
        {"name": "BOXER Torremolinos", "type": "Store (Fetish / Apparel / Toys)"},
        {"name": "Addicted", "type": "Store (Underwear / Beachwear)"},
        {"name": "Club Couture", "type": "Store (Concept Store / Fashion)"},
        {"name": "La Nogalera Shops", "type": "Store (Boutique Hub)"}
    ],
    "tours": [
        {"name": "Torremolinos Pride Heritage Walk", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Moderate"},
        {"name": "Costa del Sol Gay Beach Hop", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Private LGBTQ Nightlife Crawl", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Caminito del Rey Guided Hike", "activityLevel": "High", "estimatedTime": "6 Hours", "pricingGuide": "Moderate"},
        {"name": "Dolphin Watching Boat Tour", "activityLevel": "Low", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Ronda & Setenil Day Trip", "activityLevel": "Moderate", "estimatedTime": "10 Hours", "pricingGuide": "Moderate"},
        {"name": "Gibraltar Tax-Free & Rock Tour", "activityLevel": "Moderate", "estimatedTime": "8 Hours", "pricingGuide": "Moderate"},
        {"name": "Flamenco Show at Pepe Lopez", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"},
        {"name": "Nerja Caves & Frigiliana Trip", "activityLevel": "Moderate", "estimatedTime": "7.5 Hours", "pricingGuide": "Moderate"},
        {"name": "Malaga Wine & Vineyard Tour", "activityLevel": "Low", "estimatedTime": "5 Hours", "pricingGuide": "Luxury"},
        {"name": "Mijas Pueblo White Village Tour", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Budget"},
        {"name": "Marbella & Puerto Banus VIP", "activityLevel": "Low", "estimatedTime": "6 Hours", "pricingGuide": "Luxury"},
        {"name": "Cordoba Mosque-Cathedral Trip", "activityLevel": "Moderate", "estimatedTime": "10 Hours", "pricingGuide": "Luxury"},
        {"name": "Crocodile Park Entry & Tour", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Private Boat Rental (Benalmadena)", "activityLevel": "Low", "estimatedTime": "3.5 Hours", "pricingGuide": "Luxury"},
        {"name": "Alhambra Granada Full-Day", "activityLevel": "Moderate", "estimatedTime": "11 Hours", "pricingGuide": "Luxury"},
        {"name": "Costa del Sol Sunset Sailing", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Moderate"}
    ]
}

vienna_data = {
    "baseFare": [500, 1000],
    "hotels": [
        {"name": "Hotel Sans Souci Wien", "type": "Luxury", "tags": ["World Rainbow Hotels", "LGBTQ Friendly"]},
        {"name": "The Guesthouse Vienna", "type": "Luxury", "tags": ["World Rainbow Hotels", "LGBTQ Friendly"]},
        {"name": "Hotel Das Tyrol", "type": "Mid-Priced", "tags": ["LGBTQ Owned & Operated", "Boutique"]},
        {"name": "Hotel Altstadt Vienna", "type": "Luxury", "tags": ["LGBTQ Friendly", "IGLTA Member"]},
        {"name": "Steigenberger Hotel Herrenhof", "type": "Luxury", "tags": ["IGLTA Accredited", "LGBTQ Friendly"]},
        {"name": "Hotel Motto", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "Design-led"]},
        {"name": "25hours Hotel at MuseumsQuartier", "type": "Mid-Priced", "tags": ["LGBTQ Friendly", "Social Hub"]},
        {"name": "Hotel Beethoven Wien", "type": "Moderate", "tags": ["LGBTQ Friendly", "Boutique"]},
        {"name": "The Harmonie Vienna", "type": "Moderate", "tags": ["LGBTQ Friendly", "Sustainable"]},
        {"name": "W Vienna", "type": "Luxury", "tags": ["IGLTA Member", "LGBTQ Friendly"]},
        {"name": "Hotel Indigo Vienna – Naschmarkt", "type": "Moderate", "tags": ["LGBTQ Friendly"]},
        {"name": "The Leo Grand", "type": "Luxury", "tags": ["LGBTQ Friendly"]},
        {"name": "Ruby Marie Hotel & Bar", "type": "Moderate", "tags": ["LGBTQ Friendly", "Modern"]},
        {"name": "Wombat's City Hostel Vienna", "type": "Budget", "tags": ["LGBTQ Friendly", "Youth Hub"]},
        {"name": "Superbude Wien Prater", "type": "Budget", "tags": ["LGBTQ Friendly", "Creative"]}
    ],
    "iata": "VIE",
    "image": "&#127462;&#127481;",
    "lgbtqDistrict": "Naschmarkt / Mariahilfer Straße",
    "lgbtqSafety": "Austria: Very Safe. Vienna has a thriving LGBTQ+ scene centered around Naschmarkt and the 6th district.",
    "monthlyWeather": {
        "0": {"high": "38°F", "low": "28°F", "summary": "Cold, damp, and often grey.", "gear": "Heavy coat, thermal layers, boots."},
        "1": {"high": "43°F", "low": "31°F", "summary": "Chilly with frequent winter rain.", "gear": "Wool coat, windproof umbrella."},
        "2": {"high": "52°F", "low": "37°F", "summary": "Variable spring air; breezy and bright.", "gear": "Trench coat, layered sweaters."},
        "3": {"high": "61°F", "low": "45°F", "summary": "Mild and bright; parks begin to bloom.", "gear": "Light jacket, scarf, jeans."},
        "4": {"high": "69°F", "low": "52°F", "summary": "Pleasant spring; peak outdoor comfort.", "gear": "T-shirts, light cardigan."},
        "5": {"high": "76°F", "low": "58°F", "summary": "Warm summer start; clear sunny days.", "gear": "Cotton shirts, sunglasses."},
        "6": {"high": "80°F", "low": "62°F", "summary": "Mild summer; light rain showers possible.", "gear": "Summer attire, light rain shell."},
        "7": {"high": "81°F", "low": "62°F", "summary": "Warm and humid; peak travel season.", "gear": "Linen, sandals, sun hat."},
        "8": {"high": "72°F", "low": "54°F", "summary": "Cooling down; crisp autumn mornings.", "gear": "Light jacket, layered tops."},
        "9": {"high": "60°F", "low": "47°F", "summary": "Cool and breezy; beautiful foliage.", "gear": "Sweaters, trench coat, scarf."},
        "10": {"high": "48°F", "low": "38°F", "summary": "Rainy and windy transition to winter.", "gear": "Waterproof boots, warm hat."},
        "11": {"high": "40°F", "low": "31°F", "summary": "Cold and damp; Christmas markets open.", "gear": "Winter gear, thermal socks."}
    },
    "name": "Vienna, Austria",
    "nightlife": [
        {"name": "Village Bar", "type": "Bar/Club", "tags": ["Iconic", "Social", "Pop"], "status": "Open"},
        {"name": "The Eagle Vienna", "type": "Bar/Club", "tags": ["Leather", "Fetish", "Men-only"], "status": "Open"},
        {"name": "Mango Bar", "type": "Bar/Club", "tags": ["Social", "Pop", "Mixed Ages"], "status": "Open"},
        {"name": "City Bar", "type": "Bar/Club", "tags": ["Traditional", "Local", "Social"], "status": "Open"},
        {"name": "Why Not", "type": "Bar/Club", "tags": ["Iconic Club", "Dance", "Pop"], "status": "Open"},
        {"name": "Ken Club", "type": "Bar/Club", "tags": ["Electronic", "Youth", "Performance"], "status": "Open"},
        {"name": "Hard On", "type": "Bar/Club", "tags": ["Fetish", "Cruise", "Men-only"], "status": "Open"},
        {"name": "Gugg", "type": "Bar/Club", "tags": ["Community Bar", "Relaxed", "Social"], "status": "Open"},
        {"name": "Felixx", "type": "Bar/Club", "tags": ["Stylish", "Cocktails", "Social"], "status": "Open"},
        {"name": "Türkis Rosa Lila Villa", "type": "Bar/Club", "tags": ["Community Hub", "Cafe", "Radical"], "status": "Open"},
        {"name": "Kisss Bar Vienna", "type": "Bar/Club", "tags": ["Social", "Karaoke", "Fun"], "status": "Open"},
        {"name": "Viennese Guy", "type": "Bar/Club", "tags": ["Small", "Intimate", "Social"], "status": "Open"}
    ],
    "restaurants": [
        {"name": "Café Savoy", "type": "Cafe (Iconic / Historic LGBTQ Hub)"},
        {"name": "Türkis Rosa Lila Villa", "type": "Cafe (Social Hub / Community)"},
        {"name": "Motto", "type": "Restaurant (Fine Dining / Social)"},
        {"name": "The Guesthouse Brasserie", "type": "Restaurant (Modern / Social)"},
        {"name": "Naschmarkt Deli", "type": "Cafe (Social / International)"},
        {"name": "Café Sacher", "type": "Cafe (Historic / Sacher Torte)"},
        {"name": "Skopik & Lohn", "type": "Restaurant (Artsy / Bistro)"},
        {"name": "Café Drechsler", "type": "Cafe (Historic / Reopened)"},
        {"name": "Palmenhaus", "type": "Cafe / Restaurant (Botanical / Social)"},
        {"name": "Glacis Beisl", "type": "Restaurant (Traditional / Modern)"}
    ],
    "safetyScore": 9,
    "saunas": [
        {"name": "Kaiserbründl", "type": "Sauna", "tags": ["Historic", "Luxury", "Iconic"]},
        {"name": "Sportsauna", "type": "Sauna", "tags": ["Modern", "Gym-vibe", "Young"]},
        {"name": "Apollo Sauna", "type": "Sauna", "tags": ["Traditional", "Mature", "Local"]}
    ],
    "stores": [
        {"name": "Löwenherz", "type": "LGBTQ+ Bookstore"},
        {"name": "Gay-T-Shop", "type": "Store (Fashion / Apparel / Gifts)"},
        {"name": "Fetter", "type": "Store (Fetish / Leather / Gear)"},
        {"name": "Eslite Spectrum", "type": "Store (Independent Designer Hub)"},
        {"name": "Naschmarkt Antiques", "type": "Store (Flea Market / Social)"}
    ],
    "tours": [
        {"name": "Vienna Queer History Walk", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Budget"},
        {"name": "The Imperial Gay History Tour", "activityLevel": "Moderate", "estimatedTime": "3 Hours", "pricingGuide": "Moderate"},
        {"name": "LGBTQ Nightlife & Naschmarkt Crawl", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Schönbrunn Palace State Rooms", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Moderate"},
        {"name": "Hofburg Imperial Treasury Tour", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"},
        {"name": "Belvedere Palace & Klimt Viewing", "activityLevel": "Low", "estimatedTime": "2 Hours", "pricingGuide": "Budget"},
        {"name": "Spanish Riding School Training", "activityLevel": "Low", "estimatedTime": "1 Hour", "pricingGuide": "Budget"},
        {"name": "Danube River Sightseeing Cruise", "activityLevel": "Low", "estimatedTime": "1.5 Hours", "pricingGuide": "Budget"},
        {"name": "Viennese Coffee House Culture Walk", "activityLevel": "Moderate", "estimatedTime": "2.5 Hours", "pricingGuide": "Moderate"},
        {"name": "Central Cemetery Art & Music Walk", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Wachau Valley Wine & Melk Abbey", "activityLevel": "Moderate", "estimatedTime": "9 Hours", "pricingGuide": "Luxury"},
        {"name": "Salzburg Full-Day Private Trip", "activityLevel": "Moderate", "estimatedTime": "12 Hours", "pricingGuide": "Luxury"},
        {"name": "Vienna Street Art & Urban Walk", "activityLevel": "High", "estimatedTime": "3 Hours", "pricingGuide": "Budget"},
        {"name": "Prater Giant Ferris Wheel Ride", "activityLevel": "Low", "estimatedTime": "0.5 Hours", "pricingGuide": "Budget"},
        {"name": "Viennese Cooking Class (Schnitzel)", "activityLevel": "Low", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"},
        {"name": "Underground Vienna: Roman Ruins", "activityLevel": "Moderate", "estimatedTime": "2 Hours", "pricingGuide": "Moderate"},
        {"name": "Vienna Woods & Mayerling History", "activityLevel": "Moderate", "estimatedTime": "4 Hours", "pricingGuide": "Moderate"}
    ]
}

with open('/home/user/PrideTravelScoutAPP/destinations.json', 'r') as f:
    file_lines = f.readlines()

print(f"Original: {len(file_lines)} lines")

updates = []
for city_key, city_data in [('taipei', taipei_data), ('torremolinos', torremolinos_data), ('vienna', vienna_data)]:
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
