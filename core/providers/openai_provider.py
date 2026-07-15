import os
import requests


API_URL = "https://api.openai.com/v1/chat/completions"

MODEL = "gpt-4.1-mini"



def ask_openai(text):

    api_key = os.getenv("OPENAI_API_KEY")


    if not api_key:

        print("[OPENAI] API key missing")
        return None


    api_key = api_key.strip()


    if any(ord(c) > 127 for c in api_key):

        print("[OPENAI] Invalid API key characters")
        return None



    headers = {

        "Authorization": f"Bearer {api_key}",

        "Content-Type": "application/json"

    }



    data = {

        "model": MODEL,

        "messages": [

            {
                "role": "user",
                "content": text
            }

        ],

        "temperature": 0.7

    }



    try:

        response = requests.post(

            API_URL,

            headers=headers,

            json=data,

            timeout=30

        )


        result = response.json()



        if response.status_code != 200:

            print("[OPENAI STATUS]", response.status_code)
            print(result)
            return None



        if "choices" in result:

            answer = result["choices"][0]["message"]["content"]

            if answer:

                return answer.strip()



        return None



    except Exception as e:

        print("[OPENAI ERROR]", e)

        return None
