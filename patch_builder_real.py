from pathlib import Path

path = Path("core/builder/full_builder_engine.py")

text = path.read_text(encoding="utf-8")

text = text.replace(
'''from datetime import datetime
import os
import json
''',
'''import os

from core.projects.engine.code_engine import code_engine
from core.projects.engine.test_engine import test_engine
from core.projects.engine.debug_engine import debug_engine
'''
)

old = '''    def generate_code(self, name):

        return {
            "project":name,
            "code_engine":"active",
            "status":"generated"
        }
'''

new = '''    def generate_code(self, name):

        files = {
            "main.py": """def main():
    print("Sepehr generated app running")


if __name__ == "__main__":
    main()
""",

            "database.py": """import sqlite3


def connect():
    return sqlite3.connect("data.db")
""",

            "test.py": """print("Generated test")
"""
        }

        result = []

        for filename, content in files.items():

            result.append(
                code_engine.create_file(
                    name,
                    filename,
                    content
                )
            )

        return {
            "files": result,
            "status":"code_generated"
        }
'''

if old not in text:
    print("generate_code block not found")
else:
    text = text.replace(old,new)
    path.write_text(text,encoding="utf-8")
    print("Builder patched successfully")
