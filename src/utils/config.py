import os
from dotenv import load_dotenv

load_dotenv()


LIVEKIT_URL = os.getenv("LIVEKIT_URL")

LIVEKIT_API_KEY = os.getenv("LIVEKIT_API_KEY")

LIVEKIT_API_SECRET = os.getenv("LIVEKIT_API_SECRET")

ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")

ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

if ([LIVEKIT_API_KEY,ASSEMBLYAI_API_KEY, ELEVENLABS_API_KEY, GROQ_API_KEY]):
    print("all api keys are present")
