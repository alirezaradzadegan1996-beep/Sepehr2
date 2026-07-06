# core/decision.py

def decide(text, concepts):
    """
    مغز تصمیم‌گیر سپهر
    خروجی: route + reason
    """

    print("🧠 Decision Layer فعال شد")

    # -------------------------
    # Code / App Detection
    # -------------------------
    if is_code_request(text):
        return {
            "route": "code",
            "reason": "code/app request detected"
        }

    # -------------------------
    # Ads Detection
    # -------------------------
    if is_ads_request(text):
        return {
            "route": "ads",
            "reason": "marketing request detected"
        }

    # -------------------------
    # Design Detection
    # -------------------------
    if is_design_request(text):
        return {
            "route": "design",
            "reason": "design request detected"
        }

    # -------------------------
    # Default Knowledge
    # -------------------------
    return {
        "route": "knowledge",
        "reason": "default knowledge mode"
    }


# =================================================
# 🧠 SMART DETECTORS
# =================================================

def is_code_request(text):

    keywords = [
        "اپ", "برنامه", "کد", "سایت", "پروژه", "ساخت"
    ]

    app_types = [
        "ماشین حساب",
        "حساب",
        "مدیریت",
        "فروشگاه",
        "چت",
        "ربات",
        "یادداشت",
        "تودو",
        "todo"
    ]

    # حالت عمومی
    if any(k in text for k in keywords):
        return True

    # حالت اپ‌های مشخص
    if any(a in text for a in app_types):
        return True

    return False


def is_ads_request(text):

    keywords = [
        "تبلیغ", "بازاریابی", "فروش", "کمپین"
    ]

    return any(k in text for k in keywords)


def is_design_request(text):

    keywords = [
        "طراحی", "لوگو", "رنگ", "UI", "UX", "ظاهر"
    ]

    return any(k in text for k in keywords)
