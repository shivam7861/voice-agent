# src/sessions/entrypoint.py

from livekit import agents
from livekit.agents import AgentSession, RoomInputOptions
from livekit.plugins import groq, assemblyai, elevenlabs, noise_cancellation, silero
from src.agents.voice_agent import VoiceAgent

async def entrypoint(ctx: agents.JobContext):
    # Initialize session with all AI components
    session = AgentSession(
        stt=assemblyai.STT(
            end_of_turn_confidence_threshold=0.7,
            min_end_of_turn_silence_when_confident=160,
            max_turn_silence=2400,
        ),
        vad=silero.VAD.load(),
        llm=groq.LLM(model="llama-3.1-8b-instant"),
        tts=elevenlabs.TTS(
            voice_id="ODq5zmih8GrVes37Dizd",
            model="eleven_multilingual_v2"
        ),
    )

    await session.start(
        room=ctx.room,
        agent=VoiceAgent(),
        room_input_options=RoomInputOptions(
            noise_cancellation=noise_cancellation.BVC()
        ),
    )

    # Initial greeting
    await session.generate_reply(
        instructions="Greet the user briefly and offer your assistance."
    )
