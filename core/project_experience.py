from core.project_memory import ProjectMemory


class ProjectExperience:

    def __init__(self):
        self.project_memory = ProjectMemory()

    def find_similar_projects(self, project_type):

        projects = self.project_memory.get_projects()
        similar = []

        for project in projects:

            if project.get("type") != project_type:
                continue

            if project.get("status") != "completed":
                continue

            if project.get("test_status") != "passed":
                continue

            failures = project.get(
                "experience_failures",
                0
            )

            successes = project.get(
                "experience_successes",
                0
            )

            feedback_score = project.get(
                "feedback_score",
                0
            )

            if failures >= 3 and failures > successes:
                continue

            if feedback_score <= -30:
                continue

            similar.append(project)

        return similar

    def score_project(self, project, goal=""):

        score = 0

        if project.get("status") == "completed":
            score += 30

        if project.get("test_status") == "passed":
            score += 40

        if project.get("architecture"):
            score += 10

        if project.get("files"):
            score += 10

        if project.get("features"):
            score += 5

        if project.get("suggestions"):
            score += 5

        project_name = project.get("name", "").lower()
        goal_text = goal.lower()

        stop_words = {
            "یک",
            "اپ",
            "برنامه",
            "بساز",
            "برای",
            "با",
            "و",
            "در",
            "از",
            "جدید"
        }

        goal_words = {
            word
            for word in goal_text.split()
            if word not in stop_words
        }

        project_words = {
            word
            for word in project_name.split()
            if word not in stop_words
        }

        common_words = goal_words.intersection(project_words)

        score += len(common_words) * 10

        feedback_score = project.get(
            "feedback_score",
            0
        )

        score += feedback_score

        return score

    def apply_feedback(self, project_id, success):

        # جلوگیری از استفاده از حافظه قدیمی
        self.project_memory.load()

        for project in self.project_memory.memory:

            if project.get("id") != project_id:
                continue

            current_score = project.get(
                "feedback_score",
                0
            )

            if success:
                current_score += 10
            else:
                current_score -= 15

            project["feedback_score"] = current_score

            project["experience_successes"] = project.get(
                "experience_successes",
                0
            )

            project["experience_failures"] = project.get(
                "experience_failures",
                0
            )

            if success:
                project["experience_successes"] += 1
            else:
                project["experience_failures"] += 1

            self.project_memory.save()

            return {
                "updated": True,
                "project_id": project_id,
                "success": success,
                "feedback_score": current_score
            }

        return {
            "updated": False,
            "project_id": project_id
        }

    def get_experience(self, project_type, goal=""):

        projects = self.find_similar_projects(project_type)

        if not projects:
            return {
                "found": False,
                "project_type": project_type,
                "projects_count": 0,
                "best_project_id": None,
                "best_score": 0,
                "architecture": [],
                "files": [],
                "features": [],
                "suggestions": []
            }

        scored_projects = []

        for project in projects:

            score = self.score_project(
                project,
                goal
            )

            scored_projects.append(
                (
                    score,
                    project
                )
            )

        scored_projects.sort(
            key=lambda item: item[0],
            reverse=True
        )

        best_score, best_project = scored_projects[0]

        successes = best_project.get(
            "experience_successes",
            0
        )

        failures = best_project.get(
            "experience_failures",
            0
        )

        if best_score >= 130 and successes >= 2:
            confidence = "high"
        elif best_score >= 100:
            confidence = "medium"
        else:
            confidence = "low"

        if failures > successes:
            confidence = "low"

        return {
            "found": True,
            "project_type": project_type,
            "projects_count": len(projects),
            "confidence": confidence,
            "experience_successes": successes,
            "experience_failures": failures,
            "best_project_id": best_project.get("id"),
            "best_project_name": best_project.get("name"),
            "best_score": best_score,
            "architecture": best_project.get(
                "architecture",
                []
            ),
            "files": best_project.get(
                "files",
                []
            ),
            "features": best_project.get(
                "features",
                []
            ),
            "suggestions": best_project.get(
                "suggestions",
                []
            )
        }
