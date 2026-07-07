def parse(text):
    text = text.strip()

    # یادگیری ماشین
    if text.startswith("ماشین من ") and text.endswith("است"):
        value = text[len("ماشین من "):-len("است")].strip()
        return {
            "intent": "learn",
            "field": "car",
            "value": value
        }

    # سؤال درباره ماشین
    if "ماشینم" in text or "ماشین من" in text:
        return {
            "intent": "memory",
            "field": "car"
        }

    # یادگیری اسم
    if text.startswith("اسم من ") and text.endswith("است"):
        value = text[len("اسم من "):-len("است")].strip()
        return {
            "intent": "learn",
            "field": "name",
            "value": value
        }

    # سؤال درباره اسم
    if "اسمم" in text or "اسم من" in text:
        return {
            "intent": "memory",
            "field": "name"
        }

    return None
