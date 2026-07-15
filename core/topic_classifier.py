TOPICS = {

    "رباتیک": [
        "ربات",
        "رباتیک",
        "دستگاه",
        "ماشین هوشمند",
        "بازو"
    ],


    "پهپاد و پرواز": [
        "پهپاد",
        "پرنده",
        "پرواز",
        "درون",
        "کوادکوپتر"
    ],


    "هوش مصنوعی": [
        "هوش مصنوعی",
        "ai",
        "یادگیری ماشین",
        "شبکه عصبی"
    ],


    "نجوم": [
        "فضا",
        "سیاره",
        "مریخ",
        "ماه",
        "ستاره",
        "کهکشان"
    ],


    "برنامه نویسی": [
        "کد",
        "برنامه",
        "پایتون",
        "نرم افزار"
    ]

}



def detect_topic(text):

    text = text.lower()


    scores = {}


    for topic, words in TOPICS.items():

        score = 0


        for word in words:

            if word in text:
                score += 1


        scores[topic] = score



    best_topic = max(
        scores,
        key=scores.get
    )


    if scores[best_topic] == 0:

        return "عمومی"



    return best_topic
