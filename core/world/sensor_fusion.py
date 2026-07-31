class SensorFusion:


    def combine(self, vision=None, audio=None):


        result = {

            "type":"multi_sensor_event",

            "sources":[],

            "observations":[],

            "confidence":0.0

        }


        confidence = 0



        if vision:


            result["sources"].append(
                "vision"
            )


            result["observations"].append(
                vision
            )


            confidence += 0.5



        if audio:


            result["sources"].append(
                "audio"
            )


            result["observations"].append(
                audio
            )


            confidence += 0.5



        result["confidence"] = confidence



        if len(result["sources"]) == 2:

            result["interpretation"] = (
                "visual and audio event detected"
            )


        elif "vision" in result["sources"]:

            result["interpretation"] = (
                "visual event detected"
            )


        elif "audio" in result["sources"]:

            result["interpretation"] = (
                "audio event detected"
            )


        else:

            result["interpretation"] = (
                "no event"
            )



        return result



sensor_fusion = SensorFusion()
