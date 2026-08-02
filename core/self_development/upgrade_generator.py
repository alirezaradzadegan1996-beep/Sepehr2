

class UpgradeGenerator:


    def generate(self, weakness):

        return {

            "upgrade":
                "generated",

            "target":
                weakness,

            "status":
                "UPGRADE_GENERATION_ACTIVE"

        }


upgrade_generator = UpgradeGenerator()

