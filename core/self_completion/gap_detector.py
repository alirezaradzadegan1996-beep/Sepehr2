import os


class GapDetector:


    def detect(self):

        missing = []


        expected = [
            "planner",
            "builder",
            "tester",
            "debugger",
            "memory",
            "learning",
            "evolution"
        ]


        files = []

        for root,dirs,fs in os.walk("core"):

            for f in fs:

                files.append(f.lower())


        for item in expected:

            found = False

            for f in files:

                if item in f:
                    found = True


            if not found:
                missing.append(item)


        return {
            "missing": missing,
            "count": len(missing)
        }


gap_detector = GapDetector()
