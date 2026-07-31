from pathlib import Path


path = Path("core/builder/full_builder_engine.py")


text = path.read_text(encoding="utf-8")


if "intent_analyzer" not in text:

    text = text.replace(
        "from datetime import datetime",
        "from datetime import datetime\nfrom core.projects.intent_analyzer import intent_analyzer"
    )


old = """    def build(self, request):

        name = request.replace(
            " ",
            "_"
        )
"""


new = """    def build(self, request):

        intent = intent_analyzer.analyze(request)


        name = request.replace(
            " ",
            "_"
        )
"""


text = text.replace(old,new)


old2 = """        pipeline = []


        analysis = self.analyze(request)
"""

new2 = """        pipeline = []


        pipeline.append(intent)


        analysis = self.analyze(request)
"""


text = text.replace(old2,new2)


path.write_text(text, encoding="utf-8")


print("Intent Analyzer connected to Builder")
