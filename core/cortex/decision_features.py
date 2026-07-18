"""
Sepehr2 Cortex Decision Features
تشخیص قابلیت‌های جانبی تصمیم
"""



FEATURE_RULES = {

    "memory": [
        "حافظه",
        "ذخیره",
        "ذخیره کن",
        "ثبت کن",
        "یادت",
        "به خاطر بسپار",
        "remember",
        "save",
    ],


    "code": [
        "کد",
        "کدنویسی",
        "پایتون",
        "python",
        "java",
        "cpp",
        "code",
    ],


    "search": [
        "جستجو",
        "وب",
        "گوگل",
        "google",
        "search",
    ],


    "learning": [
        "یاد بگیر",
        "آموزش",
        "یادگیری",
        "learn",
    ],


    "project": [
        "پروژه",
        "اپ",
        "اپلیکیشن",
        "برنامه",
        "بساز",
        "create",
        "project",
    ],

}



def detect_features(text: str):

    """
    تشخیص قابلیت‌های جانبی موجود در درخواست
    """

    if not text:
        return []


    text = text.lower().strip()


    features = []


    for feature, keywords in FEATURE_RULES.items():

        for keyword in keywords:

            if keyword.lower() in text:

                features.append(feature)
                break



    return features
