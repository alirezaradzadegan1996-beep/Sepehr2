from core.runtime.runtime_router_bridge import RuntimeRouterBridge, autonomous_pipeline
from core.cortex.cortex import cortex
from core.security.runtime_security import runtime_security




def main():

    print("[SEPEHR] Runtime Started")

    while True:

        text = input("👤 ")

        if text in ["exit", "quit", "خروج"]:
            print("Sepehr stopped")
            break


        security = runtime_security.authorize(
            voice=True,
            face=True,
            device=True,
            biometric=True
        )

        if not security["allowed"]:
            print("[SECURITY]", security)
            continue

        pipeline_result = autonomous_pipeline(text)
        route_result = pipeline_result
        print("[PIPELINE]", pipeline_result)




if __name__ == "__main__":
    main()