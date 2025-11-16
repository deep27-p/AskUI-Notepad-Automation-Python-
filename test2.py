from askui import VisionAgent
import time

with VisionAgent() as agent:
    # Open Notepad
    agent.cli(r'start "" "notepad"')
    time.sleep(2)  # wait for Notepad to open

    # Type text directly (focus on Notepad manually if needed)
    agent.type("Hello I'm Appu")
