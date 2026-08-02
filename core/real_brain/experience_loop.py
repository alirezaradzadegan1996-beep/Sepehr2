

class ExperienceLoop:

    def record(self,experience):
        return {
            "experience":experience,
            "recorded":True,
            "status":"EXPERIENCE_RECORDING_LOOP_ACTIVE"
        }


experience_loop=ExperienceLoop()

