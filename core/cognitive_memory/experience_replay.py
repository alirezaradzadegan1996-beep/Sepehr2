

class ExperienceReplay:

    def replay(self,experience):
        return {
            "experience":experience,
            "replay":"completed",
            "status":"EXPERIENCE_REPLAY_ACTIVE"
        }


experience_replay=ExperienceReplay()

