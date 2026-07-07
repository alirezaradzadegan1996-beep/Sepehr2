from core.dynamic_memory import load_profile, save_profile


def show_memory():

    profile = load_profile()

    memory = profile.get("memory", {})

    if not memory:
        return "چیزی در حافظه ندارم."

    text = "چیزهایی که می‌دانم:\n"

    for key, value in memory.items():
        text += f"- {key}: {value}\n"

    return text



def forget(key):

    profile = load_profile()

    memory = profile.get("memory", {})

    if key in memory:
        del memory[key]
        save_profile(profile)
        return "فراموش کردم ✅"

    return "این مورد را ندارم."
