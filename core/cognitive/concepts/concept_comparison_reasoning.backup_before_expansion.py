from core.cognitive.concepts.concept_engine import concept_engine
from core.cognitive.concepts.concept_knowledge import concept_knowledge


class ConceptComparisonReasoning:


    def analyze(self, text):

        concepts = concept_engine.extract(text)


        if concepts["count"] != 2:
            return None


        first = concepts["concepts"][0]["name"]
        second = concepts["concepts"][1]["name"]


        first_info = concept_knowledge.get(first)
        second_info = concept_knowledge.get(second)


        if not first_info or not second_info:
            return None


        answer = (
            "تحلیل مقایسه‌ای سپهر:\n\n"
            f"موضوع اول: {first}\n"
            f"نوع: {first_info['category']}\n"
            f"ویژگی‌ها: {', '.join(first_info['properties'])}\n\n"
            f"موضوع دوم: {second}\n"
            f"نوع: {second_info['category']}\n"
            f"ویژگی‌ها: {', '.join(second_info['properties'])}\n\n"
            "تفاوت اصلی:\n"
            f"{first} و {second} از نظر کاربرد و ساختار متفاوت هستند.\n"
            "یکی بر اساس ویژگی‌های خودش برای یک هدف استفاده می‌شود و دیگری برای هدف متفاوت."
        )


        return {
            "answer": answer,
            "concepts": concepts,
            "knowledge_used": True
        }


concept_comparison_reasoning = ConceptComparisonReasoning()
