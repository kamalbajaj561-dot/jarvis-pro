from __future__ import annotations

from dataclasses import dataclass


@dataclass
class ActionResult:
    ok: bool
    message: str


def requires_confirmation(intent: str, command: str, guarded: tuple[str, ...]) -> bool:
    text = command.lower()
    return intent == "system_control" and any(word in text for word in guarded)
