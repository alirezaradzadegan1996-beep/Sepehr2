class MemoryRouter:

    def route(self, memory_type):

        return {
            "route": memory_type,
            "status": "MEMORY_ROUTER_ACTIVE"
        }


memory_router = MemoryRouter()
