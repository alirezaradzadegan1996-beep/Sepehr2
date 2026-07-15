def parse_forget_command(text):

    text = text.strip()


    if "فراموش کن" not in text:

        return None


    if "اسم" in text:

        return "name"


    if "شهر" in text:

        return "city"


    if "شغل" in text:

        return "job"


    if "رنگ" in text:

        return "favorite_color"


    return None
