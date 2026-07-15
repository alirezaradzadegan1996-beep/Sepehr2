def calculate_rank(score, confidence):

    if confidence is None:
        confidence = 1


    # امتیاز نهایی
    rank = score + (confidence * 0.5)


    return rank



def confidence_level(confidence):

    if confidence <= 2:

        return "ضعیف"


    elif confidence <= 7:

        return "قابل اعتماد"


    else:

        return "تثبیت شده"
