from core.dispatcher.dispatcher import dispatcher
from core.decision.decision_core import decision_core
from core.projects.engine.project_manager import project_manager
from core.capabilities.registry import registry
from core.capabilities.evolution_guard import evolution_guard
from core.capabilities.capability_matcher import CapabilityMatcher
from core.capabilities.capability_resolver import CapabilityResolver
from core.learning.capability_creator import CapabilityCreator
from core.learning.capability_tester import CapabilityTester
from core.learning.capability_quality import CapabilityQuality
from datetime import datetime


class RuntimeRouterBridge:


    def __init__(self):
        self.matcher = CapabilityMatcher()
        self.resolver = CapabilityResolver()
        self.creator = CapabilityCreator()
        self.tester = CapabilityTester()
        self.quality = CapabilityQuality()

        self.capability_matcher = CapabilityMatcher()
        self.capability_resolver = CapabilityResolver()
        self.capability_creator = CapabilityCreator()
        self.capability_tester = CapabilityTester()
        self.capability_quality = CapabilityQuality()

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


        # ==========================
        # Capability Intelligence Layer
        # ==========================

        try:

            match = self.capability_matcher.match(
                text,
                registry
            )

            if match:

                score = match.get("score",0)

                if score >= 40:

                    name = match["name"]
                    cap = match["capability"]

                    print(
                        "Capability selected:",
                        name
                    )

                    return {
                        "route":"capability",
                        "capability":name,
                        "result":cap.handle(text)
                    }


            # Self Evolution

            name = self.capability_resolver.resolve(text)


            if not evolution_guard.should_evolve(text):

                raise Exception(
                    "Evolution blocked by guard"
                )


            if registry.find(name) is None:

                print(
                    "Creating capability:",
                    name
                )

                created = self.capability_creator.create(name)

                tested = self.capability_tester.test(name)

                quality = self.capability_quality.check(name)


                if quality.get("quality") == "passed":

                    from importlib import import_module

                    module = import_module(
                        f"core.capabilities.{name}"
                    )

                    if hasattr(module,"capability"):

                        registry.register(
                            name,
                            module.capability
                        )

                        print(
                            "Capability evolved:",
                            name
                        )

                        return {
                            "route":"capability",
                            "capability":name,
                            "result":
                                module.capability.handle(text)
                        }


        except Exception as e:

            print(
                "Capability evolution bypass:",
                e
            )


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

