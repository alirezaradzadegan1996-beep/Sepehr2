from pathlib import Path

path = Path("core/builder/full_builder_engine.py")

text = path.read_text(encoding="utf-8")

text = text.replace(
"from datetime import datetime",
"from datetime import datetime\nfrom core.projects.engine.test_engine import test_engine\nfrom core.projects.engine.debug_engine import debug_engine"
)

text = text.replace(
'''    def test(self, name):

        return {
            "project":name,
            "tests":"executed",
            "status":"passed"
        }
''',
'''    def test(self, name):

        return test_engine.run(name)
'''
)

text = text.replace(
'''    def debug(self, name):

        return {
            "project":name,
            "errors":0,
            "status":"clean"
        }
''',
'''    def debug(self, name):

        result = self.test(name)

        if result.get("status") == "failed":

            return debug_engine.analyze(
                result.get("output")
            )

        return {
            "project":name,
            "errors":0,
            "status":"clean"
        }
'''
)

path.write_text(text, encoding="utf-8")

print("Builder TestEngine connected")
