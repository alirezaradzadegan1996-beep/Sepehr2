NAME = "Capability"
VERSION = "1.0"
DESCRIPTION = "معرفی قابلیت‌ها و مهارت‌های سپهر"



def can_handle(text):

    words = [
        "چه کارهایی بلدی",
        "چه قابلیت هایی داری",
        "چه قابلیت‌هایی داری",
        "قابلیت هات",
        "قابلیت‌ها",
        "توانایی هات",
        "توانایی‌ها",
        "چه بلدی",
        "کمک می‌کنی"
    ]


    for word in words:

        if word in text:
            return True


    return False



def run(text):

    # جلوگیری از circular import
    from core.skill_registry import get_skills
    from core.skill_info import list_skills


    skills = get_skills()

    infos = list_skills(skills)


    result = [
        "من این قابلیت‌ها را دارم:"
    ]


    for skill in infos:

        result.append(
            f"- {skill['name']}: {skill['description']}"
        )


    return "\n".join(result)
