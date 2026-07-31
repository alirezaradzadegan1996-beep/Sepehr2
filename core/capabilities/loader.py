import os
import importlib

from core.capabilities import registry


CAPABILITY_PATH = "core.capabilities"


def discover():

    loaded = []


    path = "core/capabilities"


    for file in os.listdir(path):

        if (
            file.endswith(".py")
            and not file.endswith(".backup.py")
            and file not in [
                "__init__.py",
                "loader.py"
            ]
        ):

            name = file[:-3]


            try:

                module = importlib.import_module(
                    f"{CAPABILITY_PATH}.{name}"
                )


                if hasattr(module,"capability"):

                    obj = module.capability


                    registry.register(
                        obj.name,
                        obj
                    )


                    loaded.append(
                        obj.name
                    )


            except Exception as e:

                print(
                    "[Capability Error]",
                    name,
                    e
                )


    return loaded
