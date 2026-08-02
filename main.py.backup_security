from core.runtime.runtime_router_bridge import RuntimeRouterBridge, autonomous_pipeline
from core.cortex.cortex import cortex




def main():

    print("[SEPEHR] Runtime Started")

    while True:

        text = input("👤 ")

        if text in ["exit", "quit", "خروج"]:
            print("Sepehr stopped")
            break


        pipeline_result = autonomous_pipeline(text)
        route_result = pipeline_result
        print("[PIPELINE]", pipeline_result)




if __name__ == "__main__":
    main()