class AppBuilder:

    @staticmethod
    def run(project, step):

        # مرحله 1: تحلیل
        if step == 1:
            return {
                "status": "analysis",
                "message": "تحلیل پروژه انجام شد."
            }

        # مرحله 2: ساختار
        if step == 2:
            return {
                "status": "structure",
                "message": "ساختار اولیه پروژه ساخته شد."
            }

        # مرحله 3: کد
        if step == 3:
            return {
                "status": "coding",
                "message": "کد اولیه تولید شد."
            }

        # مرحله 4: تست
        if step == 4:
            return {
                "status": "test",
                "message": "پروژه برای تست آماده است."
            }

        # مرحله های بعد
        if step > 4:
            return {
                "status": "done",
                "message": "پروژه کامل شده است."
            }
