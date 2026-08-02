
from core.live.sepehr_live_runtime import sepehr_live_runtime
from core.interface.chat_interface import chat_interface


class SepehrTerminal:

    def send(self, text):

        request = chat_interface.receive(
            text
        )

        result = sepehr_live_runtime.run(
            request["input"]
        )

        return chat_interface.display(
            result
        )


sepehr_terminal = SepehrTerminal()
