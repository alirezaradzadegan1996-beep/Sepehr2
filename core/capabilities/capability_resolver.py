import re
from core.capabilities.capability_feedback import CapabilityFeedback


class CapabilityResolver:

    def __init__(self):
        self.feedback = CapabilityFeedback()


    def resolve(self, text):

        text = text.lower()


        rules = {

            "حسابداری": "accounting_ai",
            "حساب": "accounting_ai",

            "مالی": "finance_ai",

            "انبار": "inventory_ai",

            "فروشگاه": "store_manager_ai",
            "فروش": "store_manager_ai",
            "محصول": "store_manager_ai",
            "کالا": "store_manager_ai",
            "مشتری": "store_manager_ai",
            "سبد": "store_manager_ai",

            "ربات فروشگاه": "store_manager_ai"

        }


        for key, name in rules.items():

            if key in text:
                return name


        return None
