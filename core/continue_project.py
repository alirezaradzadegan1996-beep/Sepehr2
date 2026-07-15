from core.project_manager import ProjectManager


def continue_project():

    pm = ProjectManager()

    project = pm.get_active()


    if not project:

        return "❌ هیچ پروژه فعالی وجود ندارد."


    return pm.continue_project()
