from __future__ import annotations


class Speaker:
    def __init__(self, enabled: bool = True) -> None:
        self.enabled = enabled

    def say(self, message: str) -> None:
        if self.enabled:
            print(message)
