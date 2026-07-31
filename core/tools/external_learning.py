from datetime import datetime


class ExternalLearning:


    def __init__(self):

        self.sources = [
            "web",
            "api",
            "database"
        ]

        self.learned = []



    def search_external(self, query):

        result = {
            "query": query,
            "source": "web",
            "information": "external knowledge found",
            "status": "received"
        }

        return result



    def learn(self, information):

        self.learned.append(
            information
        )

        return {
            "knowledge_added": True,
            "total_learned": len(self.learned),
            "status": "learned"
        }



    def get_status(self):

        return {
            "sources": self.sources,
            "learned_items": len(self.learned),
            "status": "active"
        }




    def research(self, query):

        result = {
            "query": query,
            "sources": [
                "web",
                "api",
                "external_ai"
            ],
            "information": "external knowledge collected",
            "status": "received"
        }


        return result



    def learn_from_external(self, query, information):

        self.learned.append({
            "query": query,
            "information": information
        })


        return {
            "query": query,
            "saved": True,
            "knowledge_added": information,
            "status": "learned"
        }



learner = ExternalLearning()


data = learner.search_external(
    "latest AI technology"
)


print(data)


print(
    learner.learn(data)
)


print(
    learner.get_status()
)


print(
    {
        "status":"external_learning_active",
        "time":str(datetime.now())
    }
)