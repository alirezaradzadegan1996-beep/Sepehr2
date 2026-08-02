
from core.learning.experience_store import experience_store
from core.learning.pattern_analyzer import pattern_analyzer


class LearningEngine:

    def learn(self, experience):

        saved = experience_store.save(
            experience
        )

        analysis = pattern_analyzer.analyze(
            [experience]
        )

        return {
            "memory": saved,
            "analysis": analysis,
            "knowledge": "updated",
            "status": "LEARNING_ACTIVE"
        }


learning_engine = LearningEngine()
