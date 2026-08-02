
class PrioritySelector:

    def select(self, queue):

        if not queue:
            return []

        return sorted(
            queue,
            key=lambda x:
                0 if x.get("priority") == "high" else 1
        )


priority_selector = PrioritySelector()

