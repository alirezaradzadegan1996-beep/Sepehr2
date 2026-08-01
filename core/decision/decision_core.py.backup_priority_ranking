from core.brain.improved_decision import improved_decision


class DecisionCore:

    def decide(self, text, memory_context=None):

        t = text.lower()


        # =====================================
        # EXISTING CAPABILITY PRIORITY
        # =====================================

        try:

            # =====================================
            # CONSOLIDATED MEMORY GUIDED PRIORITY
            # =====================================

            try:
                import json
                import os

                knowledge_file = "data/consolidated_memory.json"

                if os.path.exists(knowledge_file):

                    with open(
                        knowledge_file,
                        encoding="utf-8"
                    ) as f:

                        consolidated = json.load(f)


                    for cap_name, info in consolidated.items():

                          rule = info.get(
                              "learned_rule",
                              ""
                          ).lower()

                          patterns = info.get(
                              "patterns",
                              []
                          )

                          matched_pattern = any(
                              str(p).lower() in t
                              for p in patterns
                          )

                          if (
                              cap_name.lower()
                              in t
                              or matched_pattern
                              or (
                                  rule
                                  and any(
                                      word in t
                                      for word in rule.split()
                                  )
                              )
                          ):

                            if info.get("confidence",0) >= 0.8:

                                return {
                                    "route":"capability",
                                    "decision":"consolidated_memory_capability",
                                    "capability":cap_name,
                                    "confidence":info.get("confidence")
                                }


            except Exception:
                pass



            # =====================================
            # MEMORY GUIDED CAPABILITY PRIORITY
            # =====================================

            if memory_context:

                boost = memory_context.get(
                    "memory_boost",
                    {}
                )

                recommended = boost.get(
                    "recommended_capability"
                )

                confidence = boost.get(
                    "confidence",
                    0
                )

                if (
                    recommended
                    and confidence >= 0.6
                ):

                    return {
                        "route":"capability",
                        "decision":"memory_guided_capability",
                        "capability":recommended,
                        "memory_boost":boost
                    }


            from core.capabilities.registry import registry

            existing = registry.route(text)

            if existing:

                memory_boost = None

                try:

                    if memory_context:

                        memory_boost = (
                            memory_context.get(
                                "memory_boost"
                            )
                        )

                        if memory_boost is None:

                            memory_boost = {
                                "used": False,
                                "experience_count": 0
                            }


                except Exception:
                    pass

                return {
                    "route":"capability",
                    "decision":"use_existing_capability",
                    "capability":existing,
                    "memory_boost":memory_boost
                }

        except Exception:
            pass



        # CAPABILITY EVOLUTION PRIORITY

        if any(x in t for x in [
            "قابلیت",
            "توانایی جدید",
            "مهارت جدید",
            "قابلیت جدید",
            "توانایی بساز",
            "قابلیت اضافه"
        ]):

            return {
                "route":"capability_evolution",
                "decision":"create_capability"
            }


        if any(x in t for x in [
            "بساز","اپ","برنامه","پروژه"
        ]):
            return {
                "route":"project_builder",
                "decision":"build_project"
            }

        if any(x in t for x in [
            "یاد","ذخیره","حفظ"
        ]):
            return {
                "route":"memory",
                "decision":"store_information"
            }

        if any(x in t for x in [
            "هوا","اخبار","قیمت","امروز","فردا"
        ]):
            return {
                "route":"external_learning",
                "decision":"research"
            }

        if any(x in t for x in [
            "رژیم","غذا","بیماری","دارو","آشپزی"
        ]):
            return {
                "route":"knowledge",
                "decision":"knowledge_answer"
            }

        experience = improved_decision.decide("conversation")

        return {
            "route":"conversation",
            "decision":"chat",
            "experience":experience
        }


decision_core = DecisionCore()


if __name__ == "__main__":

    print(decision_core.decide("سلام"))

    print(decision_core.decide("برام یک اپ ماشین حساب بساز"))

    print(decision_core.decide("فردا هوا چطوره"))

    print(decision_core.decide("رژیم غذایی بده"))
