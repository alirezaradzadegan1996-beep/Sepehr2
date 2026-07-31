import importlib
import pkgutil

from core.capabilities import registry
import core.capabilities


def discover():

    package = core.capabilities

    for _, name, _ in pkgutil.iter_modules(package.__path__):

        if name in [
            "registry",
            "loader",
            "bootstrap"
        ]:
            continue

        module = importlib.import_module(
            f"core.capabilities.{name}"
        )

        if hasattr(module, "capability"):
            registry.register(
                name,
                module.capability
            )

    return registry.list()
