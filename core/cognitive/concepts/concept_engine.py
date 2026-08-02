import re


class ConceptEngine:

    def clean_concept(self, text):

        text = text.strip()

        text = re.sub(
            r"[؟?!.,،؛:]+",
            "",
            text
        )

        text = re.sub(
            r"(تفاوت|فرق|چیست|چیه|رو بگو|را بگو|رو توصیف کن|را توصیف کن)",
            "",
            text
        )

        return text.strip()


    def extract(self, text):

        result = {
            "concepts": [],
            "count": 0
        }

        separators = [
            " با ",
            " و ",
            " نسبت به ",
            " در مقابل "
        ]

        parts = None

        for sep in separators:
            if sep in text:
                parts = text.split(sep)
                break

        if parts:

            for item in parts:

                clean = self.clean_concept(item)

                if clean:
                    result["concepts"].append({
                        "name": clean,
                        "properties": []
                    })


        result["count"] = len(result["concepts"])

        return result


concept_engine = ConceptEngine()
