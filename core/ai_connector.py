from core.providers.openai_provider import ask_openai



def ask_ai(text):

    answer = ask_openai(text)


    if not answer:
        return None


    answer = answer.strip()


    if len(answer) < 5:
        return None


    return answer
