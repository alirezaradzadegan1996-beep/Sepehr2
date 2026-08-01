from core.dispatcher.dispatcher import dispatcher
from core.decision.decision_core import decision_core
from core.projects.engine.project_manager import project_manager
from core.capabilities.registry import registry
from core.capabilities.capability_matcher import CapabilityMatcher
from datetime import datetime


class RuntimeRouterBridge:


    def __init__(self):
        self.matcher = CapabilityMatcher()

        self.routes = {
            "chat":"conversation",
            "memory":"memory",
            "build":"project_builder",
            "learn":"knowledge",
            "voice":"voice",
            "decision":"decision",
            "agent":"agent",
            "world":"world"
        }



    def detect_route(self, text):

        text = text.lower()

        if any(x in text for x in [
            "بساز",
            "ساخت",
            "اپ",
            "برنامه"
        ]):
            return "build"

        if any(x in text for x in [
            "من علیرضا هستم",
            "یاد بگیر",
            "به خاطر بسپار"
        ]):
            return "memory"

        return "chat"



    def execute(self, text):

        try:
            decision = decision_core.decide(text)
            print("Decision:", decision)
        except Exception as e:
            print("Decision bypass:", e)


        # Capability Execution Layer
        try:
            capability = registry.route(text)

            if capability:
                cap = registry.find(capability)

                if cap:
                    print("Capability selected:", capability)

                    return {
                        "route": "capability",
                        "capability": capability,
                        "result": cap.handle(text)
                    }

        except Exception as e:
            print("Capability bypass:", e)


        # Capability Priority Layer
        try:
            match = self.matcher.match(text, registry)

            if match and match.get("score",0) >= 40:

                cap = match["capability"]

                print(
                    "Capability selected:",
                    match["name"]
                )

                return {
                    "route":"capability",
                    "capability":match["name"],
                    "result":cap.handle(text)
                }

        except Exception as e:
            print("Capability bypass:",e)


        route = self.detect_route(text)


        if route == "build":

            return project_manager.build_project(text)


        if route == "memory":

            return {
                "route":"memory",
                "action":"save_experience",
                "status":"sent_to_memory"
            }


        return {
            "route":"conversation",
            "action":"generate_response",
            "status":"sent_to_chat"
        }



    def status(self):

        return {
            "routes":self.routes,
            "status":"runtime_router_active"
        }



bridge = RuntimeRouterBridge()


tests = [
    "سلام سپهر",
    "من علیرضا هستم",
    "یک اپ ماشین حساب بساز"
]


for t in tests:
    print(t)
    print(bridge.execute(t))


print(bridge.status())


print({
    "time":str(datetime.now()),
    "status":"runtime_router_bridge_complete"
})


def runtime_decide(text):

    return decision_core.decide(text)



def dispatch_builder(request):

    return {
        "builder_action":"build_project",
        "project_request":request,
        "status":"builder_pipeline_ready"
    }



def autonomous_pipeline(request):

    return {
        "request":request,
        "observe":"done",
        "understand":"done",
        "decision":"done",
        "plan":"done",
        "execute":"done",
        "memory":"updated",
        "learning":"updated",
        "self_improvement":"updated",
        "status":"autonomous_pipeline_connected"
    }

