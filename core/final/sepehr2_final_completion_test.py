
from core.final.autonomous_full_cycle import autonomous_full_cycle
from core.final.global_health_check import global_health_check
from core.final.final_self_test import final_self_test


def run():

    return {
        "cycle":
            autonomous_full_cycle.run(),

        "health":
            global_health_check.check(),

        "test":
            final_self_test.run(),

        "status":"SEPEHR2_COMPLETED"
    }
