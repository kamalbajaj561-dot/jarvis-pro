from __future__ import annotations


class Memory:
    def __init__(self) -> None:
        self._history: list[str] = []

    def add(self, text: str) -> None:
        self._history.append(text)

    def recent(self, n: int = 5) -> list[str]:
        return self._history[-n:]
