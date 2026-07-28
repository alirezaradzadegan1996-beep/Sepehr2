from core.actions.chain import ActionChain


class ActionManager:


    def __init__(self):

        self.chains = {}


    def create(self, name):

        chain = ActionChain()

        self.chains[name] = chain

        return chain


    def get(self, name):

        return self.chains.get(name)


    def list(self):

        return list(self.chains.keys())


manager = ActionManager()
