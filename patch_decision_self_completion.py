from pathlib import Path

path = Path("core/decision/decision_core.py")

text = path.read_text(encoding="utf-8")

marker = """
            from core.capabilities.registry import registry
"""

insert = """
            # =====================================
            # SELF COMPLETION ROUTING
            # =====================================

            self_keywords = [
                "self upgrade",
                "self improve",
                "improve yourself",
                "upgrade yourself",
                "fix yourself",
                "repair yourself",
                "complete system",
                "missing capability",
                "missing module",
                "ارتقا",
                "بهبود خود",
                "خودت را ارتقا",
                "رفع مشکل خود",
                "ماژول کمبود"
            ]

            if any(k in t for k in self_keywords):

                return {
                    "route": "self_completion",
                    "decision": "self_improvement_task",
                    "confidence": 0.9
                }


"""

if insert.strip() not in text:
    text = text.replace(marker, insert + marker)

path.write_text(text, encoding="utf-8")

print("[✓] Self Completion routing added")
