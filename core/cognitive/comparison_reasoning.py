import re


class ComparisonReasoning:

    def detect(self, text):

        patterns = [
            "تفاوت",
            "فرق",
            "مقایسه",
            "چه فرقی",
            "فرقش"
        ]

        return any(p in text for p in patterns)


    def extract_objects(self, text):

        separators = [
            " با ",
            " و ",
            " نسبت به "
        ]

        for sep in separators:
            if sep in text:
                parts = text.split(sep)

                if len(parts) >= 2:
                    a = parts[0]
                    b = parts[1]

                    a = a.replace("تفاوت", "")
                    a = a.replace("فرق", "")
                    a = a.replace("چیه", "")
                    a = a.strip()

                    b = b.replace("چیه", "")
                    b = b.replace("چیست", "")
                    b = b.strip()

                    return a, b

        return None, None


    def analyze(self, text):

        a,b = self.extract_objects(text)

        if not a or not b:
            return None


        result = f"""
تحلیل مقایسه‌ای سپهر:

موضوع اول: {a}
موضوع دوم: {b}

1- کاربرد:
{a} و {b} هدف و کاربرد متفاوتی دارند.

2- ساختار:
{a} و {b} از نظر ساختار و اجزا متفاوت هستند.

3- نحوه استفاده:
هرکدام در شرایط خاص خود مزیت دارند.

4- محدودیت:
هرکدام نقاط ضعف مخصوص خود را دارند.

نتیجه:
انتخاب بین {a} و {b} به نیاز و شرایط استفاده بستگی دارد.
"""

        return {
            "type":"comparison",
            "object_a":a,
            "object_b":b,
            "answer":result.strip()
        }


comparison_reasoning = ComparisonReasoning()
