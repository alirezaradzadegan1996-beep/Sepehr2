
from core.dispatcher.dispatcher import dispatcher


def connect_routes():

    try:
        from core.services.memory_service import memory_service
        dispatcher.register("memory", memory_service)
    except Exception as e:
        print("memory:",e)


    try:
        from core.projects.engine.project_manager import project_manager
        dispatcher.register("build", project_manager)
    except Exception as e:
        print("build:",e)


    try:
        from core.decision.decision_core import decision_core
        dispatcher.register("decision", decision_core)
    except Exception as e:
        print("decision:",e)


    try:
        from core.agents.project_agent import project_agent
        dispatcher.register("agent", project_agent)
    except Exception as e:
        print("agent:",e)




    try:
        from core.agents.project_agent import project_agent
        dispatcher.register("agent", project_agent)
    except Exception as e:
        print("agent:",e)


    try:
        from core.decision.decision_core import decision_core
        dispatcher.register("decision", decision_core)
    except Exception as e:
        print("decision:",e)


    try:
        from core.world.modules.context_builder import ContextBuilder
        dispatcher.register("world", ContextBuilder())
    except Exception as e:
        print("world:",e)

    print("✅ Runtime Routes Extended")


connect_routes()
