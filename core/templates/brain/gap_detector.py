import os


class TemplateGapDetector:


    def exists(self,name):

        path=f"core/templates/generated/{name}"

        return os.path.exists(path)



    def need_creation(self,name):

        return not self.exists(name)



gap_detector=TemplateGapDetector()
