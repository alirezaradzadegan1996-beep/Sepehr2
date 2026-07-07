from brain import brain
from commands import run
from voice import speak

print("🤖 سپهر V63 CLI فعال شد")
speak("سیستم فعال شد")

while True:

    text = input("تو: ")

    if text == "":
        continue

    if text == "exit":
        speak("خداحافظ")
        break

    cmd = brain(text)

    if cmd in ["wifi", "camera", "sms", "call"]:
        response = run(cmd)
    else:
        response = cmd

    print("سپهر:", response)
    speak(response)
