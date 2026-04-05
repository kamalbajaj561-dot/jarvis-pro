from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class Settings:
    wake_word: str = "jarvis"
    dry_run: bool = True
    ask_confirmation_for: tuple[str, ...] = ("shutdown", "restart", "lock")
    inrt_wallet_path: Path = Path(os.getenv("INRT_WALLET_PATH", "/tmp/INRT-Wallet"))
    screenshots_dir: Path = Path("./screenshots")


SETTINGS = Settings()
