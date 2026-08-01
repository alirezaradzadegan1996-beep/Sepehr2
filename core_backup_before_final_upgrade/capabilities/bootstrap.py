from core.capabilities.loader import discover


def load_capabilities():

    loaded = discover()

    print("[Capability] Loaded:", loaded)

    return loaded


load_capabilities()
