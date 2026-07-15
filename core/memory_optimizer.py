import json
import os


FILE = "data/learning_score.json"



def load_memory():

    if not os.path.exists(FILE):
        return []


    with open(FILE, "r", encoding="utf-8") as f:
        return json.load(f)




def analyze_memory():

    data = load_memory()


    if not data:
        print("[OPTIMIZER] حافظه خالی است")
        return []



    report = []


    for item in data:

        score = item.get("score", 0)
        uses = item.get("uses", 0)


        if score >= 5 and uses >= 5:

            status = "strong"


        elif score <= 0:

            status = "weak"


        else:

            status = "normal"



        report.append(
            {
                "question": item["question"],
                "answer": item["answer"],
                "score": score,
                "uses": uses,
                "status": status
            }
        )


    return report




def print_report():

    report = analyze_memory()


    print("===== MEMORY REPORT =====")


    for item in report:

        print(
            item["status"],
            "|",
            item["question"],
            "| score:",
            item["score"],
            "| uses:",
            item["uses"]
        )
