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


        # =====================================
        # CAPABILITY FIRST ROUTING
        # =====================================

        try:

            cap_name = self.capability_resolver.resolve(text)

            if cap_name:

                cap = registry.find(cap_name)

                if cap:

                    print("Resolver Capability:", cap_name)

                    return {
                        "route":"capability",
                        "capability":cap_name,
                        "result":cap.handle(text)
                    }


        except Exception as e:
            print("Capability resolver bypass:", e)



        # =====================================
        # NORMAL ROUTING
        # =====================================

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

    def status(self):

        return {
            "routes": self.routes,
            "status": "runtime_router_active"
        }

