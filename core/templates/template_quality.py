import os


class TemplateQuality:


    def check(self,path):

        files=os.listdir(path)

        score=0

        if "main.py" in files:
            score+=40

        if "database.py" in files:
            score+=30

        if "test.py" in files:
            score+=30


        return {
            "score":score,
            "status":"good" if score>=70 else "weak"
        }


template_quality=TemplateQuality()
