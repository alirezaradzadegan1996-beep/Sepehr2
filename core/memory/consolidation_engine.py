import json
import os
from collections import defaultdict
from datetime import datetime


EXPERIENCE_FILE = "data/experiences.json"
KNOWLEDGE_FILE = "data/consolidated_memory.json"


class ConsolidationEngine:

    def __init__(self):
        self.knowledge = {}
        self.load()


    def load(self):

        if os.path.exists(KNOWLEDGE_FILE):

            with open(
                KNOWLEDGE_FILE,
                encoding="utf-8"
            ) as f:

                self.knowledge = json.load(f)

        else:
            self.knowledge = {}



    def save(self):

        with open(
            KNOWLEDGE_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.knowledge,
                f,
                ensure_ascii=False,
                indent=2
            )



    def consolidate(self):

        if not os.path.exists(EXPERIENCE_FILE):

            return {
                "status":"no_experience"
            }


        try:
            from core.memory.memory_quality_filter import (
                memory_quality_filter
            )

            filtered = memory_quality_filter.filter()

            experiences = filtered.get(
                "experiences",
                []
            )

            print(
                "Memory Quality Filter:",
                {
                    "total": filtered.get("total"),
                    "valid": filtered.get("valid"),
                    "ignored": filtered.get("ignored")
                }
            )

        except Exception as e:

            print(
                "Quality Filter bypass:",
                e
            )

            with open(
                EXPERIENCE_FILE,
                encoding="utf-8"
            ) as f:

                experiences = json.load(f)



        groups = defaultdict(list)


        for item in experiences:

            skill = item.get(
                "skill",
                "unknown"
            )

            groups[skill].append(item)



        result = {}


        for skill, items in groups.items():

            success = 0
            failed = 0
            goals = []


            for item in items:

                if item.get("result") == "success":
                    success += 1

                else:
                    failed += 1


                if item.get("goal"):
                    goals.append(
                        item["goal"]
                    )



            total = success + failed


            confidence = 0

            if total:
                confidence = round(
                    success / total,
                    2
                )


            result[skill] = {

                "capability": skill,

                "experience_count": total,

                "success": success,

                "failed": failed,

                "confidence": confidence,

                "patterns": goals,

                "learned_rule":
                    f"Use {skill} for similar tasks",

                "updated":
                    str(datetime.now())

            }


        self.knowledge = result

        self.save()


        return {
            "status":"consolidated",
            "capabilities":len(result),
            "knowledge":result
        }



consolidation_engine = ConsolidationEngine()
