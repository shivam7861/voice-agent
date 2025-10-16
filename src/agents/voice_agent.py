from livekit.agents import Agent
from src.utils.logger import get_logger

logger = get_logger("VoiceAgent")

class VoiceAgent(Agent):
    def __init__(self):
        super().__init__(instructions="You are a helpful voice AI assistant.")
        logger.info("VoiceAgent initialized successfully.")

    async def on_message(self, message, participant):
        logger.info(f"Received message: {message}")
        # You can access these directly
        # transcription = self.session.stt
        # response = self.session.llm.generate(...)
        await self.session.say("Got your message! How can I assist?")
