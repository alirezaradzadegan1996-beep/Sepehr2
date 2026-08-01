import json
import os


EXPERIENCE_FILE = "data/experiences.json"


class MemoryQualityFilter:

    def __init__(self):
        pass


    def load(self):

        if not os.path.exists(EXPERIENCE_FILE):
            return []

        with open(
            EXPERIENCE_FILE,
            encoding="utf-8"
        ) as f:

            return json.load(f)



    def is_valid(self, item):

        skill = item.get("skill")
        result = item.get("result")

        # بدون قابلیت واقعی
        if not skill:
            return False


        # تجربه های conversation قدیمی
        if skill in [
            "unknown",
            None,
            ""
        ]:
            return False


        # فقط نتیجه‌های مشخص
        if result not in [
            "success",
            "failed"
        ]:
            return False


        return True



    def filter(self, data=None):

        if data is None:
            data = self.load()


        valid = []
        ignored = []


        for item in data:

            if self.is_valid(item):

                valid.append(item)

            else:

                ignored.append(item)



        return {

            "status":"filtered",

            "total":
                len(data),

            "valid":
                len(valid),

            "ignored":
                len(ignored),

            "experiences":
                valid

        }



memory_quality_filter = MemoryQualityFilter()
