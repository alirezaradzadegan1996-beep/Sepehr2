"""
Sepehr2 Cortex Bootstrap
راه‌اندازی اولیه سرویس‌های Cortex
"""

from core.cortex.cortex import cortex

# Services
from core.cortex.knowledge_service import KnowledgeService
from core.cortex.reasoning_service import ReasoningService
from core.cortex.memory_service import MemoryService
from core.cortex.context_service import ContextService
from core.cortex.router_service import RouterService
from core.cortex.planner_service import PlannerService
from core.cortex.health_service import HealthService
from core.cortex.event_service import EventService
from core.cortex.search_service import SearchService


def boot():

    print("🧠 Booting Sepehr OS...\n")

    # -------------------------
    # Register Services
    # -------------------------

    cortex.register_safe(
        "memory",
        MemoryService()
    )

    cortex.register_safe(
        "knowledge",
        KnowledgeService()
    )

    cortex.register_safe(
        "reasoning",
        ReasoningService()
    )

    cortex.register_safe(
        "context",
        ContextService()
    )

    cortex.register_safe(
        "router",
        RouterService(cortex)
    )

    cortex.register_safe(
        "planner",
        PlannerService()
    )

    cortex.register_safe(
        "health",
        HealthService(cortex)
    )

    cortex.register_safe(
        "events",
        EventService()
    )

    cortex.register_safe(
        "search",
        SearchService()
    )

    # -------------------------
    # Skills
    # -------------------------

    cortex.load_skills()


    print("✅ skills ready")
    print("✅ memory ready")
    print("✅ knowledge ready")
    print("✅ reasoning ready")
    print("✅ router ready")
    print("✅ planner ready")
    print("✅ health ready")
    print("✅ events ready")
    print("✅ search ready")

    print("\n🚀 Sepehr OS Ready")


    return cortex
