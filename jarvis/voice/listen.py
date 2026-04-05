from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Heard:
    heard: bool
    text: str = ""


class Listener:
    def __init__(self, enabled: bool = True) -> None:
        self.enabled = enabled

    def wait_for_wake_word(self, wake_word: str) -> Heard:
        return Heard(True, wake_word)

    def listen_once(self, retries: int = 1) -> Heard:
        return Heard(True, "open youtube")
