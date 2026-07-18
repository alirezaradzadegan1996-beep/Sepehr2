"""
Sepehr2 Cortex Context Service
مدیریت وضعیت مکالمه و کانتکست
"""


class ContextService:

    name = "context"

    def __init__(self):
        self.history = []
        self.current_topic = None
        self.last_input = None
        self.last_answer = None


    def update(self, text, answer=None):
        self.last_input = text

        if answer:
            self.last_answer = answer

        self.history.append(
            {
                "input": text,
                "answer": answer
            }
        )


    def get_context(self):
        return {
            "last_input": self.last_input,
            "last_answer": self.last_answer,
            "topic": self.current_topic,
            "history_size": len(self.history)
        }


    def set_topic(self, topic):
        self.current_topic = topic


    def get_history(self):
        return self.history


    def clear(self):
        self.history = []
        self.current_topic = None
        self.last_input = None
        self.last_answer = None
