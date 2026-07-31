class ContextBuilder:

    def build(self, world, situation):

        return {
            "status":"built",
            "world":world,
            "situation":situation
        }


context_builder = ContextBuilder()
