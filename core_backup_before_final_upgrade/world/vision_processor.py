class VisionProcessor:


    def analyze(self, frame):


        if not frame:

            return {
                "status":"no_frame"
            }


        return {

            "status":"processed",

            "frame": frame.get(
                "frame_id"
            ),

            "objects":[
                "unknown_object"
            ],

            "description":
                "image analyzed"

        }



vision_processor = VisionProcessor()
