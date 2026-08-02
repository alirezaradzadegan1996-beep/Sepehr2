class ConceptInference:

    def infer(self, concept):

        text = concept.strip()

        result = {
            "name": text,
            "category": "unknown",
            "properties": []
        }

        patterns = {
            "وسیله": [
                "دارای هدف استفاده",
                "دارای اجزا",
                "دارای روش عملکرد"
            ],

            "موجود": [
                "دارای ویژگی",
                "قابل بررسی",
                "دارای کاربرد یا نقش"
            ],

            "شیء": [
                "دارای ساختار",
                "دارای جنس",
                "قابل استفاده در محیط"
            ]
        }


        if any(x in text for x in [
            "ماشین",
            "خودرو",
            "دوچرخه",
            "هواپیما",
            "موتور"
        ]):
            result["category"] = "وسیله"
            result["properties"] = patterns["وسیله"]


        elif any(x in text for x in [
            "تلویزیون",
            "کامپیوتر",
            "موبایل",
            "رایانه"
        ]):
            result["category"] = "وسیله"
            result["properties"] = [
                "پردازش اطلاعات",
                "مصرف انرژی",
                "دارای عملکرد مشخص"
            ]


        else:
            result["category"] = "شیء"
            result["properties"] = patterns["شیء"]


        return result


concept_inference = ConceptInference()
