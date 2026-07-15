from core.project_intent import detect_project_intent
from core.goal_engine import has_goal
from core.reasoning_engine import reason


def run_agent(text):

    print("[AGENT] شروع تصمیم گیری")


    intent = detect_project_intent(text)

    print("[AGENT] Intent:", intent)



    if intent == "start_project":

        return {
            "action": "start_project"
        }



    if intent == "next_step" and has_goal():

        return {
            "action": "next_step"
        }



    if intent == "complete_step" and has_goal():

        return {
            "action": "complete_step"
        }



    if intent == "project_status" and has_goal():

        return {
            "action": "project_status"
        }



    if intent == "project_advice" and has_goal():

        return {
            "action": "project_advice"
        }



    # --------------------------
    # یادگیری تجربه
    # --------------------------

    if intent == "experience_report" and has_goal():

        return {
            "action": "learn_experience"
        }



    # --------------------------
    # یادگیری تصمیم
    # --------------------------

    if intent == "decision_report" and has_goal():

        return {
            "action": "learn_decision"
        }



    result = reason(text)


    if result:

        return {
            "action": "reason",
            "result": result
        }



    return {
        "action": "local_ai"
    }
