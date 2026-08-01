class ActionChain:


    def __init__(self):

        self.actions = []


    def add(self, action):

        self.actions.append(action)


    def run(self, context):

        results = []

        for action in self.actions:

            result = action.execute(context)

            results.append({
                "action": action.name,
                "result": result
            })


        return results
