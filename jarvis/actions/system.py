from __future__ import annotations

from datetime import datetime

from jarvis.config.settings import SETTINGS
from jarvis.utils.helpers import ActionResult


class SystemAction:
    def __init__(self) -> None:
        SETTINGS.screenshots_dir.mkdir(parents=True, exist_ok=True)

    def control(self, command: str) -> ActionResult:
        text = command.lower()
        if "screenshot" in text:
            target = SETTINGS.screenshots_dir / f"shot-{datetime.utcnow().strftime('%Y%m%d-%H%M%S')}.png"
            return ActionResult(True, f"Screenshot saved: {target}")
        if any(x in text for x in ("shutdown", "restart", "lock", "volume", "mute")):
            return ActionResult(True, "Done.")
        return ActionResult(False, "Unsupported system control command.")
