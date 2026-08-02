

class BusinessFactory:

    def create(self,idea):
        return {
            "business":idea,
            "strategy":"generated",
            "status":"BUSINESS_FACTORY_ACTIVE"
        }


business_factory=BusinessFactory()

