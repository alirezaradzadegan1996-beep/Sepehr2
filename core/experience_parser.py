def parse_experience(text):

    problem = text
    solution = text


    # جدا کردن مشکل

    if "مشکل از" in text:

        parts = text.split(
            "مشکل از",
            1
        )

        if len(parts) > 1:

            problem = parts[1]


            for separator in [
                "بود",
                "است",
                ",",
                "،"
            ]:

                if separator in problem:

                    problem = problem.split(
                        separator,
                        1
                    )[0]

                    break



    # جدا کردن راه حل

    solution_markers = [
        "دفعه بعد",
        "بهتره",
        "باید",
        "لازمه",
        "یاد گرفتم"
    ]


    for marker in solution_markers:

        if marker in text:

            solution = text.split(
                marker,
                1
            )[1]

            break



    return {
        "problem": problem.strip(),
        "solution": solution.strip()
    }
