FIELD_MAP = {
    "اسم من": "name",
    "ماشین من": "car",
    "شغل من": "job",
    "شهر من": "city",
    "رنگ مورد علاقه من": "favorite_color",
    "سن من": "age"
}


def extract_learning(text):

    text = text.strip()

    for phrase, field in FIELD_MAP.items():

        if text.startswith(phrase) and text.endswith("است"):

            value = text[len(phrase):-len("است")].strip()

            if value:
                return {
                    "field": field,
                    "value": value
                }

    return None
