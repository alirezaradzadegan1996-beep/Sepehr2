from datetime import datetime


class EnvironmentBootstrap:


    def __init__(self):

        self.modules = []



    def activate(self):

        modules = [

            "world_model",

            "situation_understanding",

            "context_builder",

            "environment_memory"

        ]


        for m in modules:

            self.modules.append(
                {
                    "module":m,
                    "status":"active",
                    "time":str(datetime.now())
                }
            )


        return {

            "status":"environment_understanding_complete",

            "completed":self.modules

        }



environment_bootstrap = EnvironmentBootstrap()
