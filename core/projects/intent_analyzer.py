import re


class ProjectIntentAnalyzer:


    def analyze(self, request):

        text = request.lower()


        project_type = "general"

        features = [
            "basic_structure"
        ]


        ecommerce_words = [
            "فروشگاه",
            "لوازم",
            "محصول",
            "خرید",
            "فروش",
            "کالا",
            "بازار",
            "مارکت",
            "قطعه",
            "خودرو",
            "خانگی"
        ]


        if any(word in text for word in ecommerce_words):

            project_type = "ecommerce"

            features = [
                "products",
                "users",
                "cart",
                "database",
                "inventory"
            ]


        elif "ماشین حساب" in text:

            project_type = "calculator"

            features = [
                "operations",
                "interface",
                "testing"
            ]


        elif "تعمیر" in text:

            project_type = "service"

            features = [
                "customers",
                "orders",
                "database"
            ]


        return {

            "request": request,

            "project_type": project_type,

            "features": features,

            "status": "understood"

        }



intent_analyzer = ProjectIntentAnalyzer()
