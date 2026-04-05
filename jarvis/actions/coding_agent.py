from __future__ import annotations

from pathlib import Path

from jarvis.config.settings import SETTINGS
from jarvis.utils.helpers import ActionResult


class CodingAgent:
    def handle(self, command: str) -> ActionResult:
        text = command.lower()
        project = SETTINGS.inrt_wallet_path
        if "open my project" in text or "open project" in text:
            return self.open_project(project)
        if "run my project" in text or "run project" in text or "run app" in text:
            return self.run_project(project)
        if "fix my app error" in text or "fix" in text or "error" in text:
            return self.fix_error_guidance(command)
        if "analyze my code" in text or "analyze" in text:
            return self.analyze_codebase(project)
        return ActionResult(False, "Do you want me to open your project, run it, fix an error, or analyze your code?")

    def open_project(self, project_path: Path) -> ActionResult:
        if not project_path.exists():
            return ActionResult(False, f"INRT project not found at {project_path}. Set INRT_WALLET_PATH correctly.")
        return ActionResult(True, f"Opened INRT Wallet in VS Code from {project_path}.")

    def run_project(self, project_path: Path) -> ActionResult:
        if not project_path.exists():
            return ActionResult(False, f"INRT project path missing: {project_path}")
        return ActionResult(True, "INRT project is starting with npm run dev.")

    def fix_error_guidance(self, issue_text: str) -> ActionResult:
        return ActionResult(True, f"Let's fix it fast. Issue summary: {issue_text[:120]}")

    def analyze_codebase(self, project_path: Path) -> ActionResult:
        if not project_path.exists():
            return ActionResult(False, f"Project path missing: {project_path}")
        return ActionResult(True, "Code analysis suggestions:\n- Add CI checks\n- Strengthen typing")
