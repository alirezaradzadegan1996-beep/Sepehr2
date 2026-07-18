from core.cortex.service import Service


class SearchService(Service):

    name = "search"

    def search(self, text):
        text = text.strip()

        return {
            "success": True,
            "provider": "local",
            "query": text,
            "message": (
                "🔎 SearchService آماده است.\n"
                "جستجوی وب هنوز به سیستم متصل نشده است."
            ),
        }

    def handle(self, text):
        return self.search(text)
