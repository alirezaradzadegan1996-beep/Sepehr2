def brain(text):

    text = text.lower()

    if "وای فای" in text:
        return "wifi"

    if "بلوتوث" in text:
        return "bluetooth"

    if "دوربین" in text:
        return "camera"

    if "پیام" in text:
        return "sms"

    if "تماس" in text:
        return "call"

    if "سلام" in text:
        return "سلام 👋 من سپهر هستم"

    return "unknown"
