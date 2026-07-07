# core/brain.py

from core.cortex.bootstrap import boot

boot()
from core.matcher import get_best_match
from core.tools import run_tool
from core.decision import decide


def think(text):
    """
    مغز اصلی سپهر
    """

    print("========================================")
    print("        سپهر 2.0")
    print("========================================")
    print("برای خروج بنویس: خروج\n")

    # -------------------------
    # مرحله 1: تشخیص تصمیم
    # -------------------------

    concepts = []  # اگر later concept system داری اینو وصل می‌کنیم

    decision = decide(text, concepts)
    print(f"[DECISION]: {decision}")

    route = decision["route"]

    # -------------------------
    # مرحله 2: مسیر دهی
    # -------------------------

    if route == "knowledge":
        return handle_knowledge(text)

    if route in ["ads", "design", "code"]:
        return run_tool(route, text)

    return "❌ هیچ مسیری پیدا نشد"


# -------------------------
# بخش دانش (Knowledge Mode)
# -------------------------

def handle_knowledge(text):
    """
    سیستم ساده دانش
    """

    best = get_best_match(text)

    if not best:
        print("سپهر: این مورد را هنوز یاد نگرفتم ❌")
        return None

    answer = best.get("answer", "❌ پاسخی ندارم")
    print(f"سپهر: {answer}")
    return answer
