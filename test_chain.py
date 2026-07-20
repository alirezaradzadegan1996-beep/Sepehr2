from core.action_chain_builder import ActionChainBuilder


class Decision:
    intent = "create_project"


builder = ActionChainBuilder()

chain = builder.build(Decision())

for action in chain:
    print(action)
