from __future__ import annotations

from jarvis.ai.intent import detect_rule_intent
from jarvis.ai.memory import Memory


class Brain:
    def __init__(self) -> None:
        self.memory = Memory()

    def detect_intent(self, command: str) -> tuple[str, str]:
        intent = detect_rule_intent(command)
        return intent, "rules"

    def generate_response(self, prompt: str, context: str | None = None) -> str:
        self.memory.add(prompt)
        if context:
            return f"{context}\n\nSuggestion: {prompt}"
        return f"Got it: {prompt}"
