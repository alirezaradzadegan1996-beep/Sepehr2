
from core.capabilities.base.capability import Capability


class AccountingAiCapability(Capability):

    name = "accounting_ai"

    purpose = "accounting management capability"

    keywords = [
        "حسابداری",
        "مالی",
        "فاکتور",
        "دخل",
        "خرج",
        "گزارش مالی",
        "حساب",
        "پرداخت",
        "تراکنش",
        "income",
        "finance"
    ]


    def can_handle(self,text):

        return "accounting_ai" in text



    def handle(self,text):

        return {
            "capability":"accounting_ai",
            "status":"active",
            "version":self.version
        }



capability = AccountingAiCapability()
