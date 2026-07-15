import os
import importlib


def load_skills():

    skills = []

    folder = "core.skills"


    path = folder.replace(".", "/")


    for file in os.listdir(path):

        if not file.endswith("_skill.py"):
            continue


        name = file.replace(".py", "")


        if name.startswith("__"):
            continue


        module = importlib.import_module(
            f"{folder}.{name}"
        )


        if hasattr(module, "can_handle") and hasattr(module, "run"):

            skills.append(module)


    return skills
