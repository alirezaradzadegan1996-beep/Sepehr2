
class RealMemory:

    def __init__(self):

        self.storage = []


    def save(self, data):

        self.storage.append(data)

        return {
            "data": data,
            "status": "saved"
        }


    def recall(self):

        return {
            "memory": self.storage,
            "status": "retrieved"
        }


real_memory = RealMemory()
