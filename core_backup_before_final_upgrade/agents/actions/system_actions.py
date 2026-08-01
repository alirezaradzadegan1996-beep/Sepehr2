from core.actions.action import Action


def analyze(context):

    return {
        "step": "analyze",
        "input": context
    }


def plan(context):

    return {
        "step": "plan",
        "plan": [
            "analyze",
            "execute",
            "finish"
        ]
    }


def create_system_chain(manager):

    chain = manager.create("system_task")

    chain.add(
        Action(
            "analyze",
            analyze
        )
    )

    chain.add(
        Action(
            "plan",
            plan
        )
    )

    return chain
