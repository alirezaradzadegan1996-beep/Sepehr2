from core.reasoning_memory import find_project_reason
from core.smart_memory import find_best_answer
from core.topic_classifier import detect_topic
from core.topic_memory import find_topic_answer
from core.cortex.cortex import cortex
from core.thinking_engine import choose_best


def reason(text):
    print("[REASON] شروع تحلیل...")

    candidates = []

    # ---------- Project Decision Memory ----------
    project_memory = find_project_reason(text)

    if project_memory:
        candidates.append(project_memory)

    # ---------- Smart Memory ----------
    smart = find_best_answer(text)

    if smart:
        candidates.append(smart)

    # ---------- Topic Memory ----------
    topic = detect_topic(text)
    topic_answer = find_topic_answer(topic)

    if topic_answer:
        candidates.append(topic_answer)

    # ---------- Knowledge ----------
    knowledge = None

    try:
        knowledge_service = cortex.get("knowledge")

        if knowledge_service:
            knowledge = knowledge_service.search(text)

    except KeyError:
        from core.knowledge import search_knowledge

        knowledge = search_knowledge(text)

    if knowledge:
        candidates.append(
            {
                "source": "knowledge",
                "answer": knowledge,
                "rank": 0,
            }
        )

    # ---------- انتخاب بهترین ----------
    if not candidates:
        print("[REASON] نیاز به تولید پاسخ")
        return None

    best = choose_best(candidates)

    return best
