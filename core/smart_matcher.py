import re


STOP_WORDS = [
    "یک",
    "برای",
    "از",
    "به",
    "را",
    "رو",
    "میخوام",
    "می خواهم",
    "بده",
    "بدی",
    "کن",
    "کنه",
    "بساز",
    "ساخت"
]


def normalize(text):

    text = text.lower().strip()

    replacements = {
        "یه": "یک",
        "میخوام": "",
        "می خواهم": "",
        "رو": "",
    }


    for old, new in replacements.items():
        text = text.replace(old, new)


    words = text.split()


    words = [
        w for w in words
        if w not in STOP_WORDS
    ]


    return words



def similarity(text1, text2):

    a = set(normalize(text1))
    b = set(normalize(text2))


    if not a or not b:
        return 0


    common = a.intersection(b)


    return len(common) / min(len(a), len(b))



def find_similar(question, memories, threshold=0.5):

    results = []


    for item in memories:

        score = similarity(
            question,
            item["question"]
        )


        if score >= threshold:

            results.append(
                {
                    "item": item,
                    "similarity": score
                }
            )


    results.sort(
        key=lambda x: (
            x["similarity"],
            x["item"].get("score", 0)
        ),
        reverse=True
    )


    if results:

        print("[SMART MATCH] سوال مشابه پیدا شد")
        print("Similarity:", results[0]["similarity"])

        return results[0]["item"]


    return None
