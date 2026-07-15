import re


NAME = "Math"
VERSION = "1.0"
DESCRIPTION = "انجام محاسبات ریاضی"



def score(text):

    score = 0

    words = [
        "+",
        "-",
        "*",
        "/",
        "حساب",
        "چقدر میشه"
    ]

    for word in words:

        if word in text:
            score += 20


    return score



def can_handle(text):

    words = [
        "+",
        "-",
        "*",
        "/",
        "حساب",
        "چند میشه",
        "چقدر میشه"
    ]


    for word in words:

        if word in text:
            return True


    return False



def run(text):

    try:

        expression = text


        expression = expression.replace(
            "حساب",
            ""
        )

        expression = expression.replace(
            "چقدر میشه",
            ""
        )

        expression = expression.replace(
            "چند میشه",
            ""
        )

        expression = expression.replace(
            "؟",
            ""
        )

        expression = expression.replace(
            "?",
            ""
        )


        expression = expression.strip()


        # فقط عملیات امن ریاضی
        if not re.match(
            r"^[0-9+\-*/().\s]+$",
            expression
        ):

            return None


        result = eval(
            expression,
            {
                "__builtins__": {}
            }
        )


        return f"نتیجه: {result}"


    except:

        return "نتوانستم محاسبه کنم"
