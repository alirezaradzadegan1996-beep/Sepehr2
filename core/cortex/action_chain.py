from .decision_types import DecisionType


class ActionChain:
    """
    مدیریت اجرای چند اکشن در Sepehr2 Cortex
    """

    def __init__(self, cortex):
        self.cortex = cortex


    def execute(self, decision, text):

        results = []

        features = decision.metadata.get(
            "features",
            []
        )


        # -------------------------
        # Main Action
        # -------------------------

        main_result = self.cortex.get(
            decision.service.replace(
                "Service",
                ""
            ).lower()
        )


        if main_result:

            if hasattr(main_result, "handle"):

                result = main_result.handle(text)

                results.append(result)



        # -------------------------
        # Memory Action
        # -------------------------

        if (
            "memory" in features
            and decision.decision_type != DecisionType.MEMORY.value
        ):

            memory = self.cortex.get(
                "memory"
            )

            if memory:

                memory.remember(
                    "last_project_request",
                    text
                )

                results.append(
                    "🧠 درخواست در حافظه ذخیره شد."
                )


        return results
