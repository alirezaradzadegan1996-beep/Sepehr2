
class SolutionGenerator:

    def generate(self, analysis):

        problem = analysis.get(
            "problem",
            {}
        )

        text = problem.get(
            "input",
            ""
        )

        if "داغ" in text or "گرم" in text:

            solution = (
                "دلایل احتمالی می‌تواند شامل کمبود مایع خنک‌کننده، "
                "خرابی فن، مشکل ترموستات، گرفتگی رادیاتور "
                "یا ایراد در سیستم خنک‌کننده باشد. "
                "برای بررسی دقیق‌تر باید دمای موتور، وضعیت فن "
                "و سطح آب رادیاتور بررسی شود."
            )

        elif "کاهش وزن" in text or "لاغر" in text:

            solution = (
                "برای کاهش وزن بهتر است مصرف کالری کنترل شود، "
                "پروتئین کافی دریافت شود، فعالیت بدنی منظم داشته باشید "
                "و خواب کافی را حفظ کنید. "
                "بهترین روش کاهش وزن، تغییر تدریجی سبک زندگی است."
            )

        elif "برنامه" in text or "طراحی" in text:

            solution = (
                "برای طراحی برنامه ابتدا باید هدف، امکانات، "
                "کاربران و ویژگی‌های موردنیاز مشخص شود."
            )

        else:

            solution = (
                "موضوع شما بررسی شد. "
                "برای پاسخ دقیق‌تر نیاز به اطلاعات بیشتری دارم."
            )

        return {
            "analysis": analysis,
            "solution": solution,
            "status": "created"
        }


solution_generator = SolutionGenerator()
