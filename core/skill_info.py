def get_skill_info(skill):

    return {
        "name": getattr(
            skill,
            "NAME",
            skill.__name__
        ),

        "version": getattr(
            skill,
            "VERSION",
            "1.0"
        ),

        "description": getattr(
            skill,
            "DESCRIPTION",
            "بدون توضیح"
        )
    }



def list_skills(skills):

    result = []

    for skill in skills:

        result.append(
            get_skill_info(skill)
        )

    return result
