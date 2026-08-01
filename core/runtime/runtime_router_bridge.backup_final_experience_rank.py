from core.dispatcher.dispatcher import dispatcher
from core.decision.decision_core import decision_core
from core.projects.engine.project_manager import project_manager
from core.capabilities.registry import registry
from core.capabilities.capability_quality_engine import CapabilityQualityEngine
from core.capabilities.capability_experience_selector import CapabilityExperienceSelector
from core.capabilities.capability_memory import CapabilityMemory
from core.capabilities.evolution_guard import evolution_guard
from core.capabilities.capability_matcher import CapabilityMatcher
from core.capabilities.capability_resolver import CapabilityResolver
from core.capabilities.capability_feedback import CapabilityFeedback
from core.memory.experience_memory import ExperienceMemory
from core.memory.memory_intelligence import MemoryIntelligence
from core.learning.capability_creator import CapabilityCreator
from core.learning.capability_tester import CapabilityTester
from core.learning.capability_quality import CapabilityQuality
from datetime import datetime


class RuntimeRouterBridge:


    def __init__(self):
        self.capability_memory = CapabilityMemory()
        self.matcher = CapabilityMatcher()
        self.resolver = CapabilityResolver()
        self.creator = CapabilityCreator()
        self.tester = CapabilityTester()
        self.quality = CapabilityQuality()

        self.capability_matcher = CapabilityMatcher()
        self.capability_resolver = CapabilityResolver()
        self.feedback = CapabilityFeedback()
        self.quality_engine = CapabilityQualityEngine()
        self.experience_selector = CapabilityExperienceSelector()
        self.experience_memory = ExperienceMemory()
        self.memory_intelligence = MemoryIntelligence()
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
            experience_context = self.experience_memory.recall()

            memory_payload = {
                "current_task": text,
                "experiences": experience_context,
                "count": len(experience_context)
            }

            memory_analysis = self.memory_intelligence.analyze(
                memory_payload
            )

            print("Memory Intelligence:", memory_analysis)

            decision = decision_core.decide(text)
            print("Decision:", decision)

        except Exception as e:
            print("Decision bypass:", e)


        # =====================================
        
        # =====================================
        # CAPABILITY PRIORITY FINAL LAYER
        # =====================================

        try:

            blocked_words = [
                "سلام",
                "خوبی",
                "من ",
                "هستم",
                "ماشین حساب",
                "اپ "
            ]

            blocked = any(
                x in text.lower()
                for x in blocked_words
            )

            if not blocked:

                cap_name = self.capability_resolver.resolve(text)

                if cap_name:

                    cap = registry.find(cap_name)

                    if cap:
                        print("Capability selected:", cap_name)

                        result = cap.handle(text)

                        try:
                            self.capability_memory.record(
                                cap_name,
                                success=True
                            )
                            print("Memory recorded:", cap_name)
                        except Exception as e:
                            print("Memory bypass:", e)


                        try:
                            self.feedback.record(
                                cap_name,
                                success=True
                            )

                            print(
                                "Feedback recorded:",
                                cap_name
                            )

                        except Exception as e:
                            print(
                                "Feedback bypass:",
                                e
                            )


                        return {
                            "route":"capability",
                            "capability":cap_name,
                            "result":result
                        }

        except Exception as e:
            print("Capability guard bypass:", e)

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




    def _experience_memory_score(self, capability):

        try:
            experiences = self.experience_memory.recall()

            score = 0

            for exp in experiences:

                skill = exp.get("skill","")

                if skill == capability:

                    result = exp.get("result")

                    if result == "success":
                        score += 0.2

                    elif isinstance(result, dict):
                        if result.get("success"):
                            score += 0.2

            return min(score,1)

        except Exception:
            return 0

    def _select_best_capability(self, candidates):

        try:

            ranked = []

            for c in candidates:

                try:

                    score = (
                        self.experience_selector.score(c) * 0.3
                        +
                        self.quality_engine.score(c) * 0.2
                    )

                    ranked.append({
                        "capability": c,
                        "score": score
                    })

                except:
                    pass


            if ranked:

                ranked.sort(
                    key=lambda x:x["score"],
                    reverse=True
                )

                print("Adaptive ranking:", ranked)

                return ranked[0]["capability"]


        except Exception as e:

            print("Adaptive selector bypass:", e)


        return None



    def _filter_capabilities(self, candidates):

        blocked = [
            "سلام_ai",
            "من_ai",
            "یک_ai"
        ]

        return [
            c for c in candidates
            if c not in blocked
        ]

    def status(self):

        return {
            "routes": self.routes,
            "status": "runtime_router_active"
        }
