
from pathlib import Path


class FileManager:

    def create(self, path, content):

        p = Path(path)
        p.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        p.write_text(
            content,
            encoding="utf-8"
        )

        return {
            "file": path,
            "status": "created"
        }


file_manager = FileManager()
