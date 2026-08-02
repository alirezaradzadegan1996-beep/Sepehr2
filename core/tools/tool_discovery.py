
from core.tools.plugin_registry import plugin_registry


class ToolDiscovery:

    def discover(self):

        return {
            "tools": list(
                plugin_registry.plugins.keys()
            ),
            "status": "discovered"
        }


tool_discovery = ToolDiscovery()
