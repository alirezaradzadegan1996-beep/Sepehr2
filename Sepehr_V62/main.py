from brain import brain
from phone import execute
from voice import speak, listen

print("🤖 سپهر V62 فعال شد")
speak("سیستم فعال شد")

while True:

    text = listen()

    if text == "":
        continue

    print("تو:", text)

    if "خداحافظ" in text:
        speak("خداحافظ")
        break

    cmd = brain(text)

    if cmd in ["wifi", "bluetooth", "camera", "sms", "call"]:
        response = execute(cmd)
    else:
        response = cmd

    print("سپهر:", response)
    speak(response)
