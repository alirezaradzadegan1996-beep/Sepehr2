import os
import subprocess


class ToolEngine:

    def run(self, command):

        cmd = command.lower().strip()

        # =====================
        # SYSTEM COMMANDS SAFE
        # =====================

        if cmd == "ls":
            return os.listdir(".")

        if cmd.startswith("echo "):
            return cmd.replace("echo ", "")

        # =====================
        # FILE OPERATIONS
        # =====================

        if cmd.startswith("read "):
            path = cmd.replace("read ", "")
            try:
                with open(path, "r", encoding="utf-8") as f:
                    return f.read()
            except:
                return "❌ فایل پیدا نشد"

        if cmd.startswith("write "):
            try:
                parts = cmd.replace("write ", "").split("|")
                path = parts[0]
                content = parts[1]
                with open(path, "w", encoding="utf-8") as f:
                    f.write(content)
                return "✅ فایل ساخته شد"
            except:
                return "❌ فرمت اشتباه"

        # =====================
        # SAFE SHELL (LIMITED)
        # =====================

        if cmd.startswith("run "):
            try:
                safe_cmd = cmd.replace("run ", "")
                result = subprocess.check_output(safe_cmd, shell=True, text=True)
                return result
            except Exception as e:
                return str(e)

        return "❌ دستور ناشناخته"
