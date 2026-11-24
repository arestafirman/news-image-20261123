# data.py — THE WORLD IN ONE DAY: Monday 23 November 2026
#
# VERIFICATION SHEET (single source of truth for the poster AND the
# DATE CHECK box). Every story below happened, or was first reported,
# on Monday 23 November 2026 in at least one time zone, checked in two
# layers: (a) date in the named source, (b) cross-checked against the
# stale-item list. Heroes are 100% fresh 23 Nov; tiles and briefs are
# the Monday news cycle as reported on 23 Nov by the named outlet.
#
# Sources consulted 24 Nov 2026 (WIB): Reuters, AP, Al Jazeera,
# Bloomberg, Grist, CNBC, Ukrainian Air Force, Nvidia, ABC, FDD.
#
# STALE ITEMS — excluded, named in DATE CHECK with their real dates:
#   COP31 ends with no deal — Sun 22 Nov 2026
#   Iran attack on US base, Bahrain — Sat 21 Nov 2026
#   Sparta II attacked by drones — Sat 21 Nov 2026
#   Kryvyi Rih strike — Fri 20 Nov 2026
#   Peru quake M6.7 — Fri 20 Nov 2026
#   'El Chapo Isidro' captured — Sat 21 Nov 2026
#   Russia 400-drone barrage — 19-20 Nov 2026
#   Liverpool 4-0 Man Utd — Sun 22 Nov 2026
# NOT YET (DATE CHECK part b):
#   No Iranian tanker has broken the US blockade yet (convoy still at Kharg)
#   No US-Iran deal yet
#   Nigeria opposition pact signing moved to 30 Nov 2026

DATE_LINE = "Monday 23 November 2026"

# Region colours (used by the region strip, tiles, and map pins).
REGIONS = [
    # (name, count, colour)
    ("EUROPE", 8, "#2563eb"),
    ("AMERICAS", 6, "#16a34a"),
    ("AFRICA", 6, "#b45309"),
    ("SE ASIA", 4, "#ea580c"),
    ("MIDDLE EAST", 3, "#dc2626"),
    ("SOUTH ASIA", 3, "#0d9488"),
    ("OCEANIA", 3, "#0284c7"),
    ("EAST ASIA", 2, "#7c3aed"),
    ("GLOBAL", 1, "#6b7280"),
]
TOTAL_STORIES = 36
assert sum(c for _, c, _ in REGIONS) == TOTAL_STORIES

REGION_COLOUR = {name: colour for name, _, colour in REGIONS}

# Six big numbers, all computed from our own story data.
BIG_NUMBERS = [
    ("153", "DRONES LAUNCHED\nAT UKRAINE OVERNIGHT"),
    ("134", "DRONES SHOT DOWN\nOR JAMMED"),
    ("15", "KILLED NEAR KYIV\nIN THE STRIKES"),
    ("258", "DEMOCRAT HOUSE SEATS\nBIGGEST SINCE 1992"),
    ("24", "CONFIRMED DEAD IN\nINDONESIA FACTORY FIRE"),
    ("+30%", "NVIDIA SHARES JUMP\nAS HUANG RETURNS"),
]

# Heroes: (number, place, region, kicker, headline, body, source, status, art)
HEROES = [
    (
        1, "GULF OF OMAN", "MIDDLE EAST",
        "IRAN  ·  THE BLOCKADE",
        "IRAN VOWS \u2018ALL MEANS\u2019 TO BREAK THE BLOCKADE",
        "Tehran vows \u2018every means\u2019 against the US blockade as 14+ "
        "tankers wait at Kharg; a \u2018line-breaker\u2019 track proves a spoof. "
        "Trump sets a New Year deadline.",
        "Reuters", "ONGOING", "tanker",
    ),
    (
        2, "KYIV, UKRAINE", "EUROPE",
        "UKRAINE  ·  OVERNIGHT",
        "153 DRONES OVERNIGHT \u2014 15 KILLED NEAR KYIV",
        "Russia launches 153 drones; defences down 134, but a block in "
        "Dymer collapses, killing 11. Zelenskyy wants the US to release "
        "paid-for Patriots.",
        "Ukrainian Air Force / Al Jazeera", "CONFIRMED", "kyiv",
    ),
    (
        3, "SANTA CLARA, USA", "AMERICAS",
        "TECH  ·  THE COMEBACK",
        "HUANG IS BACK \u2014 NVIDIA SOARS 30%",
        "Nvidia\u2019s board unanimously reinstates Jensen Huang as CEO, 11 days "
        "after he quit amid scandal. Shares jump 30% premarket; Wall Street "
        "roars back.",
        "Nvidia / Bloomberg", "CONFIRMED", "chip",
    ),
]

# Tiles 4-13: (number, place, region, headline, body, source, status, art)
TILES = [
    (
        4, "ANTALYA", "GLOBAL",
        "COP31 FALLOUT: \u2018WORST COP EVER\u2019",
        "Blame flies after the collapse. EU: the text was \u2018hijacked by "
        "oil states\u2019.",
        "Grist / CNBC", "REPORTED", "gavel",
    ),
    (
        5, "ST PETERSBURG", "EUROPE",
        "SPARTA II REACHES PORT",
        "The drone-hit cargo ship arrives under tow after two days ablaze; "
        "16 crew safe.",
        "Reuters", "CONFIRMED", "ship",
    ),
    (
        6, "BANTEN, INDONESIA", "SE ASIA",
        "24 CONFIRMED DEAD IN FACTORY FIRE",
        "Indonesia confirms 24 dead in the factory blaze; about 30 still "
        "missing.",
        "Reuters", "CONFIRMED", "flame",
    ),
    (
        7, "WASHINGTON, USA", "AMERICAS",
        "DEMOCRATS HIT 258 HOUSE SEATS",
        "Biggest majority since 1992: Hubbard beats Foxx in N. Carolina "
        "after a recount.",
        "AP", "REPORTED", "capitol",
    ),
    (
        8, "NEW DELHI", "SOUTH ASIA",
        "INDIA GIVES NEPAL $1.62BN",
        "Modi announces a 240bn-rupee package for flood-hit Nepal after "
        "talks in Delhi.",
        "Reuters", "CONFIRMED", "handshake",
    ),
    (
        9, "GAZA", "MIDDLE EAST",
        "ISRAELI STRIKE KILLS UN WORKER",
        "A strike kills at least three in Gaza, including a UN agency "
        "worker.",
        "Reuters", "REPORTED", "aid",
    ),
    (
        10, "THE HAGUE", "SE ASIA",
        "14 STATES BACK ICJ GENOCIDE RULING",
        "Fourteen countries back the world court\u2019s Rohingya genocide "
        "ruling.",
        "Reuters", "CONFIRMED", "court",
    ),
    (
        11, "YEREVAN", "EUROPE",
        "ARMENIA OFFERS NEW CONSTITUTION",
        "Yerevan proposes a new constitution, a step toward peace with "
        "Azerbaijan.",
        "Reuters", "REPORTED", "constitution",
    ),
    (
        12, "COPENHAGEN", "EUROPE",
        "DENMARK TO BAN PHONES IN SCHOOLS",
        "Copenhagen will propose a mobile-phone ban in schools from 2027, "
        "Reuters reports.",
        "Reuters", "REPORTED", "phone",
    ),
    (
        13, "EASTERN CONGO", "AFRICA",
        "FIGHTING HAMPERS EBOLA RESPONSE",
        "Clashes near the outbreak zone disrupt the Ebola response, the WHO "
        "chief says.",
        "Reuters", "REPORTED", "virus",
    ),
]

# ALSO ON — briefs 14-36: (number, region, text)
BRIEFS = [
    (14, "EAST ASIA", "S Korea education minister quits over exam AI-cheating chaos"),
    (15, "MIDDLE EAST", "West Bank settler arson; Eisenkot calls it \u2018Jewish terrorism\u2019"),
    (16, "AFRICA", "Nigeria opposition summit postponed to 30 Nov"),
    (17, "EUROPE", "EU farm and general affairs councils meet in Brussels"),
    (18, "AFRICA", "East African ministers meet in Kampala"),
    (19, "AFRICA", "South Sudan party talks continue in Juba"),
    (20, "AMERICAS", "Home Depot: Richard McPhail takes over as CEO"),
    (21, "OCEANIA", "NZ hold India to a draw in the Wellington Test"),
    (22, "AMERICAS", "Miley Cyrus weds Maxx Morando in Palm Springs"),
    (23, "EUROPE", "Don Toliver show in Manchester evacuated; 12,000 fans out"),
    (24, "SE ASIA", "Thai court halves jail term of royal-insult lawmaker"),
    (25, "SE ASIA", "Indonesia president to name VP candidates on Monday"),
    (26, "EAST ASIA", "US seeks answers on Nvidia chip sales to China, Bessent says"),
    (27, "SOUTH ASIA", "Bangladesh court limits social media for under-16s"),
    (28, "EUROPE", "Bomb-threat emails hit ~450 schools in Germany"),
    (29, "OCEANIA", "Australian shares slide at the open; NZ falls"),
    (30, "SOUTH ASIA", "India court pushes clean-fuel cars only in Delhi"),
    (31, "AFRICA", "US advances $170m Africa health aid despite holds"),
    (32, "AFRICA", "Congo Ebola toll far above official count, graves show"),
    (33, "EUROPE", "Armenia PM: drop \u2018Western Armenia\u2019 from draft charter"),
    (34, "AMERICAS", "Wall Street roars back as Huang returns"),
    (35, "AMERICAS", "Trump to host gala for his plunging meme coin"),
    (36, "OCEANIA", "King Charles, Elton John pay tribute to Molly Meldrum"),
]

# Map pins: (story number, lon, lat). lon -180..180, lat -60..80.
PINS = [
    (1, 51.0, 29.0),
    (2, 30.5, 50.4),
    (3, -121.0, 37.4),
    (4, 30.7, 36.9),
    (5, 30.3, 59.9),
    (6, 106.3, -6.2),
    (7, -77.0, 38.9),
    (8, 77.2, 28.6),
    (9, 34.5, 31.5),
    (10, 92.5, 21.0),
    (11, 44.5, 40.2),
    (12, 12.6, 55.7),
    (13, 29.0, 1.0),
]

# Story number -> region (for pin colours).
STORY_REGION = {}
for _n, _p, _r, *_rest in HEROES:
    STORY_REGION[_n] = _r
for _n, _p, _r, *_rest in TILES:
    STORY_REGION[_n] = _r

# The day in UTC, by part of day (no invented precise times).
TIMELINE = [
    ("OVERNIGHT", "153 drones hit Ukraine"),
    ("MORNING", "24 dead confirmed, Banten"),
    ("MIDDAY", "$1.62bn pledged to Nepal"),
    ("AFTERNOON", "Huang back as Nvidia CEO"),
    ("EVENING", "Sparta II docks"),
    ("LATE", "Iran vows \u2018all means\u2019"),
]

# DATE CHECK box, from the same verification sheet.
DATE_CHECK_LEFT_OUT = [
    ("COP31 ends with no deal", "Sun 22 Nov"),
    ("Iran attack on US base, Bahrain", "Sat 21 Nov"),
    ("Sparta II attacked", "Sat 21 Nov"),
    ("Kryvyi Rih strike", "Fri 20 Nov"),
    ("Peru quake M6.7", "Fri 20 Nov"),
    ("\u2018El Chapo Isidro\u2019 captured", "Sat 21 Nov"),
    ("Russia 400-drone barrage", "19\u201320 Nov"),
    ("Liverpool 4\u20130 Man Utd", "Sun 22 Nov"),
]
DATE_CHECK_NOT_YET = [
    "No Iranian tanker has broken the blockade yet",
    "No US\u2013Iran deal yet",
    "Nigeria pact signing moved to 30 Nov",
]

# Sanity: 3 heroes + 10 tiles + 23 briefs = 36 stories.
assert len(HEROES) == 3
assert len(TILES) == 10
assert len(BRIEFS) == 23
assert len(HEROES) + len(TILES) + len(BRIEFS) == TOTAL_STORIES
# Region counts must match the stories assigned to each region.
_counts = {}
for _r in [h[2] for h in HEROES] + [t[2] for t in TILES] + [b[1] for b in BRIEFS]:
    _counts[_r] = _counts.get(_r, 0) + 1
assert _counts == {name: c for name, c, _ in REGIONS}, _counts
