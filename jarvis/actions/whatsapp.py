from __future__ import annotations

from jarvis.ai.brain import Brain
from jarvis.utils.helpers import ActionResult


class WhatsAppAction:
    def __init__(self, brain: Brain) -> None:
        self.brain = brain

    def send(self, command: str) -> ActionResult:
        return ActionResult(True, f"Prepared WhatsApp action: {command}")
