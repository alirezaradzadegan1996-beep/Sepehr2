import json

PROFILE_FILE = "data/profile.json"


def load_profile():
    with open(PROFILE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_profile(profile):
    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=4)


def remember(key, value):
    profile = load_profile()

    if "memory" not in profile:
        profile["memory"] = {}

    profile["memory"][key] = value

    save_profile(profile)


def recall(key):
    profile = load_profile()

    return profile.get("memory", {}).get(key)
