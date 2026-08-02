import json
import os
import re
from datetime import datetime


class KnowledgeBrain:

    def __init__(self):

        self.file = "data/knowledge_brain.json"

        os.makedirs(
            "data",
            exist_ok=True
        )

        if not os.path.exists(self.file):

            with open(
                self.file,
                "w",
                encoding="utf-8"
            ) as f:

                json.dump(
                    {},
                    f,
                    ensure_ascii=False
                )


    def _normalize(self, text):

        text = str(text).lower()

        replacements = {
            "چیست": "",
            "چی هست": "",
            "است": "",
            "؟": "",
            "?": ""
        }

        for old,new in replacements.items():

            text = text.replace(
                old,
                new
            )

        return text.strip()


    def _keywords(self, text):

        normalized = self._normalize(text)

        words = re.findall(
            r"[\wآ-ی]+",
            normalized
        )

        return words



    def add_knowledge(self, topic, info):

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            data = json.load(f)


        data[topic] = info


        with open(
            self.file,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=2
            )


        return {
            "status":"knowledge_added",
            "topic":topic
        }



    def query(self, question):

        with open(
            self.file,
            "r",
            encoding="utf-8"
        ) as f:

            data=json.load(f)


        # direct match

        if question in data:

            return {
                "topic":question,
                "answer":data[question],
                "source":"knowledge_brain",
                "status":"found"
            }


        # semantic keyword match

        query_words = set(
            self._keywords(question)
        )


        best = None
        score = 0


        for topic,info in data.items():

            topic_words = set(
                self._keywords(topic)
            )


            current = len(
                query_words.intersection(
                    topic_words
                )
            )


            if current > score:

                score = current
                best = (
                    topic,
                    info
                )


        if best and score > 0:

            return {
                "topic":best[0],
                "answer":best[1],
                "source":"knowledge_brain_semantic",
                "score":score,
                "status":"found"
            }


        return {
            "topic":question,
            "answer":None,
            "source":"knowledge_brain",
            "status":"not_found"
        }



    def search(self, topic):

        return self.query(topic)


    def learn(self, topic, information):

        return self.add_knowledge(
            topic,
            information
        )


brain = KnowledgeBrain()
