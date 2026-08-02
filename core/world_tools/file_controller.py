

from pathlib import Path

class FileController:

    def create(self,name):
        Path(name).write_text(
            "Sepehr test file",
            encoding="utf-8"
        )

        return {
            "file":name,
            "created":True,
            "status":"FILE_SYSTEM_CONTROLLER_ACTIVE"
        }


file_controller=FileController()

