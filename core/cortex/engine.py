"""
Sepehr2 Cortex Engine
مدیریت اجرای سرویس‌ها + Action Chain
"""

from .decision_engine import DecisionEngine
from .action_chain import ActionChain

import time
import traceback


class CortexEngine:

    def __init__(self, registry):

        self.registry = registry

        self.decision_engine = DecisionEngine()

        self.action_chain = None

        self.before_hooks = []
        self.after_hooks = []
        self.middleware = []

        self.stats = {
            "runs": 0,
            "errors": 0,
            "total_time": 0.0,
        }


    # -------------------------
    # Hooks
    # -------------------------

    def add_before_hook(self, func):
        self.before_hooks.append(func)


    def add_after_hook(self, func):
        self.after_hooks.append(func)


    def add_middleware(self, func):
        self.middleware.append(func)



    # -------------------------
    # Decision
    # -------------------------

    def decide(self, text):

        return self.decision_engine.decide(text)



    # -------------------------
    # Execute
    # -------------------------

    def execute(
        self,
        service_name,
        method=None,
        *args,
        **kwargs
    ):

        if not self.registry.has(service_name):

            raise KeyError(
                f"Service '{service_name}' not found."
            )


        service = self.registry.get(service_name)


        start = time.perf_counter()


        try:

            # Before hooks

            for hook in self.before_hooks:

                hook(service_name)



            # Middleware

            for mw in self.middleware:

                mw(service_name)



            # -------------------------
            # Action Chain
            # -------------------------

            result = self.action_chain.run(
                service,
                method,
                *args,
                **kwargs
            )



            # After hooks

            for hook in self.after_hooks:

                hook(
                    service_name,
                    result
                )



            elapsed = (
                time.perf_counter()
                -
                start
            )


            self.stats["runs"] += 1

            self.stats["total_time"] += elapsed


            return result



        except Exception:

            self.stats["errors"] += 1

            traceback.print_exc()

            raise



    # -------------------------
    # Stats
    # -------------------------

    def average_time(self):

        if self.stats["runs"] == 0:

            return 0


        return (
            self.stats["total_time"]
            /
            self.stats["runs"]
        )



    def report(self):

        return {

            "runs":
                self.stats["runs"],

            "errors":
                self.stats["errors"],

            "average_time":
                self.average_time(),

            "middlewares":
                len(self.middleware),

            "before_hooks":
                len(self.before_hooks),

            "after_hooks":
                len(self.after_hooks),

        }
