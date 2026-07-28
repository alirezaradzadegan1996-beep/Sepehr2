from core.actions.action import Action


def analyze(context):

    return {
        "step": "analyze",
        "task": context
    }


def reason(context):

    return {
        "step": "reason",
        "decision": "project architecture selected"
    }


def plan(context):

    return {
        "step": "plan",
        "steps": [
            "create structure",
            "write code",
            "test"
        ]
    }


def generate(context):

    return {
        "step": "generate",
        "status": "code generation ready"
    }


def create_project_chain(manager):

    chain = manager.create("project_build")


    chain.add(
        Action("analyze", analyze)
    )

    chain.add(
        Action("reason", reason)
    )

    chain.add(
        Action("plan", plan)
    )

    chain.add(
        Action("generate", generate)
    )


    return chain
