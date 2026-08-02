
class CapabilityRanking:

    def rank(self, capabilities):

        return {
            "ranking": capabilities,
            "best": capabilities[0],
            "status":"ranked"
        }


capability_ranking_upgrade = CapabilityRanking()
