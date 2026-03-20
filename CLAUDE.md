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

## Git Workflow
- Branch: `claude/fix-sydney-weather-duplicate-jVI35`
- Always push after commits
- Format must remain consistent across all commits

---
**Last Updated**: 2026-03-20
**Format Status**: LOCKED ✓ (JSON format with single-line compacted arrays for each category - do not change without explicit user permission)
