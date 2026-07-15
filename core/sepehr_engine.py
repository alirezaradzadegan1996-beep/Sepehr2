from core.agent_engine import run_agent
from core.action_executor import execute
from core.agent_memory import remember_action
from core.agent_context import update_context
from core.goal_engine import get_goal



def chat(text):

    print("[SEPEHR] دریافت پیام")


    # 2 - تصمیم گیری Agent
    action = run_agent(text)



    # 3 - ذخیره تصمیم Agent
    remember_action(
        action,
        text
    )



    # 4 - اجرای عمل
    print("[SEPEHR] اجرای عمل")

    answer = execute(
        action,
        text
    )



    # 5 - بروزرسانی وضعیت
    goal = get_goal()


    if goal:

        update_context({

            "project": goal.get("title"),

            "topic": goal.get("topic"),

            "current_step": goal.get("current_step"),

            "current_task": goal.get("steps", [])

        })



    return answer
