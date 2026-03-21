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

## Locked App Behavior Rules (NEVER CHANGE without written user permission)

### Rule 1 — Event Search Date Defaults
When a user clicks an event card (quickSearch with start/end dates), the travel date fields MUST be pre-filled as:
- **Departure date** = event start date **minus 1 day**
- **Return date** = event end date **plus 1 day**
- Implementation: `quickSearch(cityName, start, end)` in `index.html` around line 1638
- DO NOT change this date logic under any circumstances

### Rule 2 — Result Card Venue Counts (LOCKED)
Search result cards MUST display exactly:
- **2 Shops/Stores** (from `data.stores` array + any store-type items in `data.nightlife`)
- **2 Saunas** (from `data.saunas` array + any sauna-type items in `data.nightlife`)
- **2 Restaurants** (from `data.restaurants` array)
- **4 Bars & Clubs** (from `data.nightlife` array, excluding stores/saunas/restaurants)
- Implementation: `randomStores`, `randomSaunas`, `randomRestaurants`, `randomNightlife` variables in the search result render block
- DO NOT increase or decrease these counts

### Rule 3 — Tours: Always Show 1 LGBTQ Tour with Rainbow Flag (LOCKED)
- The tours section MUST always show **1 LGBTQ tour first** (when one exists for that destination), followed by up to 4 other tours
- **LGBTQ tour detection**: check tour `tags` array for 'lgbtq'/'gay'/'queer'/'pride' OR check tour `name` for those same keywords
- **Visual indicator**: LGBTQ tours MUST display the 🏳️‍🌈 rainbow flag icon and an 'LGBTQ+' badge on the tour card
- **Card styling**: LGBTQ tour card has a purple-tinted border/background to distinguish it
- If no LGBTQ tour exists for a destination, show up to 4 regular tours (no rainbow flag shown)
- Implementation: `isLgbtqTour()` function, `lgbtqTours.slice(0,1)` in the search result render block

### Rule 4 — Amusement Parks Shown Separately (LOCKED)
- If a destination's data includes an `amusementParks` array with entries, those parks MUST be displayed in their own dedicated "Nearby Theme Parks" section
- This section must be separate from Tours, Nightlife, Restaurants, and Stores
- The section only renders if `data.amusementParks` has at least 1 entry (conditional render)
- Implementation: `randomParks` variable and "Nearby Theme Parks" section around line 2429

### Rule 5 — Landing Page Shows Exactly 3 Featured Hotspot Cards (LOCKED)
- The landing page hotspot carousel (`populateSafeHotspots`) MUST show **exactly 3 destination cards**
- **Amsterdam is always Card 1** (permanent, tied to World Pride 2026)
- **Cards 2 and 3 rotate randomly** — selected only from the 28 featured destinations list
- Cards 2 and 3 must NOT be selected from non-featured destinations
- Implementation: `getRandomSubset(others, 2)` where `others` is filtered by `isFeaturedCity()`

### Rule 6 — View More Tab Event Display Counts (LOCKED)
- **Default "All" view**: Show **15 Pride Events** + **5 Cruises** (never revert to 25 Pride Events)
- **When a specific filter is selected** (non-All, non-Cruise): Show **up to 15** of that filter type first, then a mixed "More LGBTQ Events" pool (up to 15 others), then **5 Cruises** at the bottom
- **Cruise filter selected**: Show up to 25 Cruises
- Implementation: `populateViewMoreEvents()` function — `getRandomSubset(..., 15)` for Pride in `all` branch; `getRandomSubset(..., 15)` for selected type in the `else` branch; `getRandomSubset(..., 5)` for Cruises in all non-Cruise branches
- DO NOT change these counts without explicit user permission

## Git Workflow
- Branch: `claude/fix-landing-page-display-fsZth`
- Always push after commits
- Format must remain consistent across all commits

---
**Last Updated**: 2026-03-21
**Format Status**: LOCKED ✓ (JSON format with single-line compacted arrays for each category - do not change without explicit user permission)
