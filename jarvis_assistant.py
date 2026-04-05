"""Backward-compatible shim for older imports."""

from jarvis.main import JarvisPro, main


class JarvisAssistant(JarvisPro):
    pass


if __name__ == "__main__":
    raise SystemExit(main())
