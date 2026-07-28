import json
import os

class MemoryService:

    def __init__(self):

        self.file = "data/memory.json"

        if not os.path.exists(self.file):

            with open(self.file,"w",encoding="utf-8") as f:
                json.dump({},f,ensure_ascii=False,indent=4)

    def boot(self):
        print("[Memory] Ready")

    def initialize(self):
        pass

    def can_handle(self,text):

        return (
            text.startswith("یاد بگیر")
            or
            text.startswith("یادت باشه")
            or
            text.startswith("حافظه")
        )

    def handle(self,text):

        if text.startswith("حافظه"):

            return self.load()

        value=text.replace("یاد بگیر","").replace("یادت باشه","").strip()

        data=self.load()

        data[str(len(data)+1)]=value

        self.save(data)

        return "✅ ذخیره شد."

    def load(self):

        with open(self.file,encoding="utf-8") as f:
            return json.load(f)

    def save(self,data):

        with open(self.file,"w",encoding="utf-8") as f:
            json.dump(
                data,
                f,
                ensure_ascii=False,
                indent=4
            )

memory_service=MemoryService()
