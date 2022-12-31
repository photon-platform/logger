"""
logger run script
"""

from .logger import Logger

import subprocess

if __name__ == "__main__":
    app = Logger()
    reply = app.run()
    print(reply)

    if reply:
        subprocess.run(['vim', reply])

    
