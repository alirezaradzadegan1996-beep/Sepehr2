
import re

class CapabilityResolver:

    def resolve(self, text):

        text = text.lower()

        rules = {
            "حسابداری": "accounting_ai",
            "مالی": "finance_ai",
            "انبار": "inventory_ai",
            "فروشگاه": "store_ai",
            "فروش": "sales_ai",
            "کاربر": "user_ai",
            "ربات": "bot_ai"
        }

        for key,name in rules.items():
            if key in text:
                return name

        words = re.findall(r'\w+', text)

        if words:
            return words[0] + "_ai"

        return "general_ai"
