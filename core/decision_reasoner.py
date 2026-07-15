def explain_decision(decision):

    if not decision:

        return "تصمیم قبلی پیدا نشد."


    score = decision.get(
        "score",
        0
    )

    uses = decision.get(
        "uses",
        1
    )

    result = decision.get(
        "result",
        ""
    )

    text = ""


    if score >= 10:

        text += "این تصمیم امتیاز بالایی دارد و نتیجه خوبی ثبت شده. "

    elif score > 0:

        text += "این تصمیم تجربه مثبت دارد. "

    else:

        text += "این تصمیم هنوز نتیجه قابل اعتماد کافی ندارد. "



    if uses > 1:

        text += (
            f"سپهر قبلاً {uses} بار از این تجربه استفاده کرده. "
        )


    if result:

        text += (
            f"نتیجه ثبت‌شده: {result}"
        )


    return text
