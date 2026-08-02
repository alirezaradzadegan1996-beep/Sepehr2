class ConceptExpansion:

    def expand(self, concept):

        concept = concept.strip()

        rules = {

            "تلویزیون": {
                "category": "وسیله الکترونیکی",
                "properties": [
                    "نمایش تصویر",
                    "پخش صدا",
                    "مصرف برق",
                    "دریافت اطلاعات"
                ]
            },

            "قابلمه": {
                "category": "ابزار آشپزی",
                "properties": [
                    "ظرف پخت غذا",
                    "تحمل حرارت",
                    "جنس فلزی یا سرامیکی",
                    "استفاده در آشپزی"
                ]
            },

            "مسواک": {
                "category": "وسیله بهداشت شخصی",
                "properties": [
                    "پاکسازی دندان",
                    "دسته و برس",
                    "استفاده روزانه"
                ]
            },

            "شامپو": {
                "category": "محصول بهداشتی",
                "properties": [
                    "شستشوی مو",
                    "مایع شوینده",
                    "استفاده روی پوست و مو"
                ]
            }

        }

        if concept in rules:
            return rules[concept]

        return {
            "category": "مفهوم ناشناخته",
            "properties": [
                "دارای کاربرد مشخص",
                "دارای ویژگی‌های قابل بررسی",
                "قابل مقایسه با مفاهیم دیگر"
            ]
        }


concept_expansion = ConceptExpansion()
