from core.actions.base_action import BaseAction
from core.action_result import ActionResult


class RememberAction(BaseAction):

    name = "remember"

    def execute(self, context):

        text = context.get("text", "")

        if not text:
            return ActionResult(
                success=False,
                error="متنی برای ذخیره وجود ندارد."
            )

        context.set("memory_saved", True)

        return ActionResult(
            success=True,
            output=f"Memory saved: {text}"
        )
