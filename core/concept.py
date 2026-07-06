# core/concept.py

from core.semantic_map import SEMANTIC_MAP


# ---------- Extract Concepts ----------
def extract_concepts(text):

    concepts = set()

    # 1. direct keyword mapping
    for word, concept in SEMANTIC_MAP.items():
        if word in text:
            concepts.add(concept)

    # 2. entity-based rules (خیلی مهم)
    # کشورها / entity ها

    if "ایران" in text:
        concepts.add("geo_country_iran")

    if "مریخ" in text:
        concepts.add("astro_mars")

    if "خورشید" in text:
        concepts.add("astro_sun")

    # 3. concept strengthening rules
    # جلوگیری از خالی شدن مفهوم

    if "پایتخت" in text:
        concepts.add("geo_capital")

    if "مرکز" in text:
        concepts.add("geo_center")

    if "جمعیت" in text:
        concepts.add("demography_population")

    if "سرعت" in text:
        concepts.add("physics_speed")

    if "نور" in text:
        concepts.add("physics_light")

    # 4. fallback safety (خیلی مهم)
    # اگر هیچ مفهومی نبود، حداقل خالی نده

    if len(concepts) == 0:
        concepts.add("unknown")

    return concepts
