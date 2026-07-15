import re


def parse_decision(text):

    problem = ""
    decision = ""
    result = ""


    # استخراج مشکل

    problem_patterns = [
        r"مشکل از (.*?)( بود| شد|,|،)",
        r"مشکل (.*?)( بود| شد|,|،)"
    ]


    for pattern in problem_patterns:

        match = re.search(
            pattern,
            text
        )

        if match:

            problem = match.group(1).strip()
            break



    # استخراج تصمیم

    decision_patterns = [
        r"تصمیم گرفتم (.*?)( و| که| شد|$)",
        r"انجام دادم (.*?)( و| که| شد|$)",
        r"راه حل (.*?)( بود| شد|$)"
    ]


    for pattern in decision_patterns:

        match = re.search(
            pattern,
            text
        )

        if match:

            decision = match.group(1).strip()
            break



    # استخراج نتیجه

    result_patterns = [
        r"(بعد|و بعد|نتیجه) (.*)"
    ]


    for pattern in result_patterns:

        match = re.search(
            pattern,
            text
        )

        if match:

            result = match.group(2).strip()
            break



    if not problem and not decision:

        return None


    return {
        "problem": problem,
        "decision": decision,
        "result": result
    }
