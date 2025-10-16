from src.utils import config
import os
from livekit import agents
from src.sessions.entrypoint import entrypoint
if __name__ == "__main__":
    agents.cli.run_app(agents.WorkerOptions(entrypoint_fnc=entrypoint))
