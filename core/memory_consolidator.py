import json
import os


MEMORY_FILE = "data/learning_score.json"
KNOWLEDGE_FILE = "data/consolidated_knowledge.json"



def load_memory():

    if not os.path.exists(MEMORY_FILE):
        return []


    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)




def load_knowledge():

    if not os.path.exists(KNOWLEDGE_FILE):
        return []


    with open(KNOWLEDGE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)




def save_knowledge(data):

    with open(
        KNOWLEDGE_FILE,
        "w",
        encoding="utf-8"
    ) as f:

        json.dump(
            data,
            f,
            ensure_ascii=False,
            indent=4
        )




def consolidate():

    memories = load_memory()

    knowledge = load_knowledge()


    added = 0


    for item in memories:

        score = item.get("score", 0)
        uses = item.get("uses", 0)


        # تجربه قوی
        if score >= 5 and uses >= 5:


            exists = False


            for k in knowledge:

                if (
                    k["question"] == item["question"]
                ):
                    exists = True



            if not exists:

                knowledge.append(
                    {
                        "question": item["question"],
                        "answer": item["answer"],
                        "source": "experience"
                    }
                )

                added += 1



    save_knowledge(knowledge)


    print(
        "[CONSOLIDATOR] منتقل شد:",
        added
    )


    return knowledge
