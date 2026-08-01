from core.capabilities.loader import discover
from core.learning.priority_engine import learning_priority
from core.brain.self_map import self_map


class CompletionEngine:


    def complete(self, skill):


        # فعال سازی قابلیت جدید
        loaded = discover()


        # ثبت در مدل خود
        try:

            self_map.add(
                skill
            )

        except Exception:

            pass



        # بروزرسانی صف یادگیری

        for item in learning_priority.queue:

            if item.get("skill") == skill:

                item["status"] = "completed"



        learning_priority.save()


        return {

            "skill": skill,

            "status":"completed",

            "loaded":loaded

        }



completion_engine = CompletionEngine()
