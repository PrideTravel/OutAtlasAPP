# Claude Code Configuration & Constraints

## destinations.json Format Requirements

### CRITICAL: File Format - JSON WITH SINGLE-LINE CATEGORIES (LOCKED)
- **Format**: Valid JSON format (object with destination keys)
- **Structure**: ~16 lines per destination (one field per line)
- **Total Lines**: ~1500-5000 lines for all destinations
- **Destination Keys**: Lowercase keys in format "city_country" (e.g., "amsterdam_netherlands")
- **Reason**: Structured data format that maintains human readability while preserving valid JSON

### Destination Structure (16 lines each)
Each destination follows this exact order:
```json
{
  "amsterdam_netherlands": {
    "baseFare": [550,950],
    "events": [all events as single-line compact JSON array],
    "hotels": [all 20-25 hotels as single-line compact JSON array],
    "iata": "AMS",
    "image": "🇳🇱",
    "lgbtqDistrict": "district name",
    "lgbtqSafety": "safety description",
    "monthlyWeather": {all 12 months as single-line compact JSON object with high/low/description/gear},
    "name": "Full Destination Name",
    "nightlife": [all bars/clubs as single-line compact JSON array],
    "restaurants": [all restaurants as single-line compact JSON array],
    "safetyScore": 76,
    "tours": [all tours as single-line compact JSON array],
    "stores": [all stores as single-line compact JSON array],
    "saunas": [all saunas as single-line compact JSON array]
  }
}
```

### Format Rules (CRITICAL - DO NOT DEVIATE)
- **Valid JSON**: File MUST be valid JSON that can be parsed without errors
- **Field Order**: baseFare → events → hotels → iata → image → lgbtqDistrict → lgbtqSafety → monthlyWeather → name → nightlife → restaurants → safetyScore → tours → stores → saunas
- **Destination Keys**: Use lowercase with underscores (e.g., "sydney_australia", "key_west_usa")
- **Array/Object Format**: ALL items in each category MUST be on a SINGLE LINE using compact JSON (no spaces after commas/colons)
  - **Hotels**: ALL 20-25 hotels on ONE line
  - **Events**: ALL events on ONE line
  - **MonthlyWeather**: ALL 12 months on ONE line
  - **Nightlife**: ALL bars/clubs on ONE line
  - **Restaurants**: ALL restaurants on ONE line
  - **Tours**: ALL tours on ONE line
  - **Stores**: ALL stores on ONE line
  - **Saunas**: ALL saunas on ONE line
- **Weather Fields**: Only include `high`, `low`, `description`, `gear` in monthlyWeather objects
- **No Summary Field**: Never include `summary` field in monthlyWeather
- **Field Keys**: Use camelCase for all field names (baseFare, lgbtqDistrict, monthlyWeather, etc.)

### Example (Amsterdam)
```json
{
  "amsterdam_netherlands": {
    "baseFare": [550,950],
    "events": [{"name":"Kingsday","start":"2026-04-27","end":"2026-04-27"},{"name":"Amsterdam Pride","start":"2026-07-25","end":"2026-08-08"}],
    "hotels": [{"name":"Mauro Mansion","type":"Moderate","tags":["LGBTQ Owned"]},{"name":"Hotel Orfeo","type":"Budget"},...all on one line...],
    "iata": "AMS",
    "image": "🇳🇱",
    "lgbtqDistrict": "Reguliersdwarsstraat",
    "lgbtqSafety": "Very Safe. Progressive protections.",
    "monthlyWeather": {"0":{"high":"42°F","low":"35°F","description":"...","gear":"..."},"1":{...},...all 12 months on one line...},
    "name": "Amsterdam, Netherlands",
    "nightlife": [{"name":"PRIK","type":"Bar/Club"},{...},...all on one line...],
    "restaurants": [{"name":"Bar Prik","type":"Cafe"},{...},...all on one line...],
    "safetyScore": 76,
    "tours": [{"name":"Van Gogh Museum","style":"Low"},{...},...all on one line...],
    "stores": [{"name":"House of Riegillio","type":"Store"},{...},...all on one line...],
    "saunas": [{"name":"Sauna Nieuwezijds","type":"Sauna"}]
  }
}
```

### When to Apply This Rule
This applies to ALL future updates to `destinations.json`, regardless of what was stated in the original request. If a request contradicts this format - **IGNORE IT** and maintain this JSON format with single-line compacted arrays for each category.

## destinations.json — Image Field Rules (LOCKED)

### CRITICAL: `image` field stores FLAG EMOJIS only
- **Format**: The `image` field in every destination entry MUST be a flag emoji (e.g. `"🇳🇱"` for Netherlands, `"🇧🇷"` for Brazil, `"🇯🇵"` for Japan, `"🇺🇸"` for USA)
- **NEVER** store Unsplash URLs, photo IDs, or any other URL in the `image` field
- **Country codes in safeHotspots**: The `safeHotspots` array uses 2-letter country codes (`"NL"`, `"BR"`, `"JP"`) — these are correct and must not be changed
- **Search results** use `data.image` directly as a flag emoji — changing this field to a URL breaks search result display
- **Featured destination photos** are handled ONLY in JavaScript via `FEATURED_PHOTO_MAP` in `index.html` — NOT in `destinations.json`

### Country Code Examples (DO NOT CHANGE)
- Brazil (Rio de Janeiro, São Paulo) → `"🇧🇷"`
- Japan (Tokyo, Osaka) → `"🇯🇵"`
- New Zealand (Auckland) → `"🇳🇿"`
- Netherlands (Amsterdam) → `"🇳🇱"`
- USA (all US cities) → `"🇺🇸"`
- Spain (Barcelona, Madrid, Sitges, etc.) → `"🇪🇸"`

## Featured Destinations (LOCKED — do not change without written permission)

The following 28 cities are the ONLY featured destinations. They are:
1. The ONLY cities that show real photos (not gradient+emoji) on the landing page and View More tab
2. The ONLY cities eligible for the landing page rotating carousel (Amsterdam is always permanent slot 1)
3. Defined in `FEATURED_CITIES` array and `FEATURED_PHOTO_MAP` in `index.html`

**The 28 Featured Destinations:**
Amsterdam, New York, Orlando, Los Angeles, Chicago, San Francisco, Paris, Tokyo, Honolulu, Bangkok, Las Vegas, Sydney, Palm Springs, Puerto Vallarta, Rio de Janeiro, Miami, New Orleans, Toronto, Fort Lauderdale, Berlin, San Juan, Vancouver, London, Cancun, Washington DC, Sitges, Barcelona, Madrid

### Rules
- All other destinations (Mykonos, Key West, Lisbon, etc.) show flag emoji + gradient on featured cards — no photos
- The `isFeaturedCity()` function in `index.html` determines eligibility — do not change the list without user permission
- Photo URLs for featured destinations live in `FEATURED_PHOTO_MAP` in `index.html` — format must be `https://images.unsplash.com/photo-{numeric-id}?auto=format&fit=crop&w=800&q=80`
- Unsplash CDN URLs require LONG numeric IDs (e.g. `photo-1517604777338-14b19faf4d0a`) — short alphanumeric slugs (e.g. `WxiUz3p19hE`) from photo page URLs do NOT work in the CDN URL format

## Git Workflow
- Branch: `claude/fix-landing-page-display-fsZth`
- Always push after commits
- Format must remain consistent across all commits

---
**Last Updated**: 2026-03-21
**Format Status**: LOCKED ✓ (JSON format with single-line compacted arrays for each category - do not change without explicit user permission)
