class AutoProjectPipeline:

    """
    اجرای خودکار چرخه ساخت پروژه
    """

    def __init__(
        self,
        manager
    ):
        self.manager = manager


    def run(
        self,
        task
    ):

        print(
            "[AUTO PIPELINE] Starting..."
        )


        # مرحله ۱
        print(
            "[AUTO PIPELINE] Creating project..."
        )

        result = self.manager.start_project(
            task
        )


        project = self.manager.get_active()

        if not project:
            return (
                "❌ پروژه ساخته نشد."
            )


        # مرحله ۲
        print(
            "[AUTO PIPELINE] Building..."
        )


        build_result = self.manager.builder.build(
            f"projects/{project['id']}",
            project["analysis"]["optimization"],
            project["analysis"]
        )


        # مرحله ۳
        print(
            "[AUTO PIPELINE] Testing..."
        )


        test_result = self.manager.run_test()


        # مرحله ۴
        print(
            "[AUTO PIPELINE] Learning..."
        )


        self.manager.save()


        return {
            "project": project.get(
                "goal"
            ),

            "build": build_result,

            "test": test_result,

            "status": "completed"
        }
