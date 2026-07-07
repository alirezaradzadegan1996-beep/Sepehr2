from core.chat import chat_response


def think(user_text):
    return chat_response(user_text)
    from core.tools import run_tool

    tool_result = run_tool(intent, text)

    if tool_result:
        print(tool_result)
        return tool_result
