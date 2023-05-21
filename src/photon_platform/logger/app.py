"""The main application class for the viewer."""

import subprocess

from .logger import Logger


def run() -> None:
    """Run the application."""
    reply = Logger().run()
    print(reply)

    if reply:
        subprocess.run(["vim", reply])
