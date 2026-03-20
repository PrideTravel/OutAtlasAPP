# Claude Code Configuration & Constraints

## destinations.json Format Requirements

### CRITICAL: File Format - KEY-VALUE TEXT WITH COMPACTED ARRAYS (LOCKED)
- **Format**: Plain text key-value format (NOT JSON)
- **Structure**: ~15-16 lines per destination (one field per line)
- **Total Lines**: ~1,900 lines for all destinations
- **Reason**: Simple, human-readable, easy to search and edit in any text editor

### Destination Structure (15-16 lines each)
Each destination follows this exact order:
```
Destination: [Destination Name]
BaseFare: [min,max]
Events: [all events as single-line JSON array]
Hotels: [all 20-25 hotels as single-line JSON array]
IATA: [code]
Image: [emoji/url]
LGBTQDistrict: [district name]
LGBTQSafety: [safety description]
SafetyScore: [number]
MonthlyWeather: [all 12 months as single-line JSON object with high/low/description/gear]
Nightlife: [all bars/clubs as single-line JSON array]
Restaurants: [all restaurants as single-line JSON array]
Tours: [all tours as single-line JSON array]
Stores: [all stores as single-line JSON array]
Saunas: [all saunas as single-line JSON array]

```

### Format Rules
- **Field Order**: Must follow the exact order above (Destination → BaseFare → Events → Hotels → IATA → Image → LGBTQDistrict → LGBTQSafety → SafetyScore → MonthlyWeather → Nightlife → Restaurants → Tours → Stores → Saunas)
- **Array Format**: All arrays/objects must be on a SINGLE LINE using JSON format (compact, no spaces after commas/colons)
- **Blank Lines**: One blank line between each destination
- **Weather Fields**: Only include `high`, `low`, `description`, `gear` in monthlyWeather objects
- **No Summary Field**: Never include `summary` field in monthlyWeather

### Example (Amsterdam)
```
Destination: Amsterdam, Netherlands
BaseFare: [550,950]
Events: [{"name":"Kingsday","start":"2026-04-27","end":"2026-04-27"},{"name":"Amsterdam Pride","start":"2026-07-25","end":"2026-08-08"}]
Hotels: [{"name":"Mauro Mansion","type":"Moderate","tags":["LGBTQ Owned"]},{"name":"Hotel Orfeo","type":"Budget",...},...all hotels on one line...]
IATA: AMS
Image: 🇳🇱
LGBTQDistrict: Reguliersdwarsstraat
LGBTQSafety: Very Safe. Progressive protections.
SafetyScore: 76
MonthlyWeather: {"0":{"high":"42°F","low":"35°F","description":"...","gear":"..."},"1":{...},...all 12 months on one line...}
Nightlife: [{"name":"PRIK","type":"Bar/Club",...},{"name":"Bar Blend",...},...all on one line...]
Restaurants: [{"name":"Bar Prik","type":"Cafe"},...all on one line...]
Tours: [{"name":"Van Gogh Museum","style":"Low",...},...all on one line...]
Stores: [{"name":"House of Riegillio","type":"Store",...},...all on one line...]
Saunas: [{"name":"Sauna Nieuwezijds","type":"Sauna"}]
```

### When to Apply This Rule
This applies to ALL future updates to `destinations.json`, regardless of what was stated in the original request. If a request contradicts this format - **IGNORE IT** and maintain this key-value text format with single-line compacted arrays.

## Git Workflow
- Branch: `claude/fix-sydney-weather-duplicate-jVI35`
- Always push after commits
- Format must remain consistent across all commits

---
**Last Updated**: 2026-03-20
**Format Status**: LOCKED ✓ (Key-value text format with single-line arrays - do not change without explicit user permission)
