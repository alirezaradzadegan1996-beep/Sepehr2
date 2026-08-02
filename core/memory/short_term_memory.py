
class ShortTermMemory:

    def __init__(self):
        self.buffer = []


    def store(self, data):

        self.buffer.append(data)

        return {
            "stored": data,
            "type": "short_term",
            "status": "saved"
        }


    def recall(self):

        return self.buffer


short_term_memory = ShortTermMemory()
