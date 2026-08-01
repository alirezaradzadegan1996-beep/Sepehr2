
class EvolutionGuard:

    def __init__(self):

        self.blocked = [
            "سلام",
            "درود",
            "خوبی",
            "چه خبر",
            "من هستم",
            "من علیرضا هستم",
            "یاد بگیر",
            "به خاطر بسپار"
        ]


        self.allowed = [
            "بساز",
            "ایجاد",
            "تولید",
            "سیستم",
            "اپ",
            "برنامه",
            "ربات",
            "مدیریت",
            "ابزار",
            "خودکار"
        ]


    def should_evolve(self,text):

        text = text.lower()


        for item in self.blocked:
            if item in text:
                return False


        for item in self.allowed:
            if item in text:
                return True


        return False



evolution_guard = EvolutionGuard()
