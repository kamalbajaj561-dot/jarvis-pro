from __future__ import annotations


RULES = {
    "whatsapp": ("whatsapp", "message", "tell"),
    "coding": ("project", "code", "error", "analyze"),
    "business": ("business", "startup", "revenue", "growth"),
    "open_app": ("open", "launch", "start"),
    "search": ("search", "google"),
    "play": ("play", "youtube"),
    "system_control": ("volume", "shutdown", "restart", "screenshot", "lock"),
}


def detect_rule_intent(command: str) -> str:
    text = command.lower()
    for intent, words in RULES.items():
        if any(word in text for word in words):
            return intent
    return "general_chat"
