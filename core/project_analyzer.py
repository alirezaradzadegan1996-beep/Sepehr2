class ProjectAnalyzer:


    def analyze(self, goal):

        result = {
            "type": "unknown",
            "features": [],
            "files": []
        }


        text = goal.lower()


        # Calculator
        if (
            "ماشین حساب" in text
            or "calculator" in text
            or "جمع" in text
            or "تفریق" in text
            or "ضرب" in text
            or "تقسیم" in text
        ):

            result["type"] = "calculator"

            result["features"] = [
                "جمع",
                "تفریق",
                "ضرب",
                "تقسیم"
            ]

            result["files"] = [
                "main.py",
                "calculator.py",
                "test.py"
            ]


        # Temperature Converter
        elif (
            "دما" in text
            or "حرارت" in text
            or "سانتیگراد" in text
            or "فارنهایت" in text
            or "کلوین" in text
            or "تبدیل دما" in text
        ):

            result["type"] = "temperature_converter"

            result["features"] = [
                "تبدیل سانتیگراد به فارنهایت",
                "تبدیل فارنهایت به سانتیگراد",
                "تبدیل کلوین"
            ]

            result["files"] = [
                "main.py",
                "converter.py",
                "test.py"
            ]


        # Weather
        elif (
            "هوا" in text
            or "آب و هوا" in text
        ):

            result["type"] = "weather"

            result["features"] = [
                "دریافت وضعیت هوا",
                "نمایش دما",
                "نمایش شهر"
            ]

            result["files"] = [
                "main.py",
                "weather.py",
                "config.py"
            ]


        # Robot
        elif "ربات" in text:

            result["type"] = "robot"

            result["features"] = [
                "کنترل موتور",
                "سنسورها",
                "منطق تصمیم"
            ]

            result["files"] = [
                "main.py",
                "motor.py",
                "sensor.py"
            ]


        else:

            result["type"] = "general_app"

            result["features"] = [
                "ساختار پایه برنامه"
            ]

            result["files"] = [
                "main.py"
            ]


        return result
