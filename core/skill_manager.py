# core/skill_manager.py

SKILLS = {

    "programming": {
        "name": "برنامه نویسی",
        "children": [
            "python",
            "html",
            "css",
            "database",
            "android"
        ]
    },

    "business": {
        "name": "کسب و کار",
        "children": [
            "management",
            "marketing",
            "accounting",
            "sales"
        ]
    },

    "construction": {
        "name": "ساختمان",
        "children": [
            "architecture",
            "structure",
            "electrical",
            "mechanical"
        ]
    },

    "medicine": {
        "name": "پزشکی",
        "children": [
            "anatomy",
            "disease",
            "drug"
        ]
    }

}


def get_skill(skill):

    return SKILLS.get(skill)


def has_skill(skill):

    return skill in SKILLS


def list_skills():

    return list(SKILLS.keys())
