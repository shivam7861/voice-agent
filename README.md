# Voice Agent Microservice

A modular, voice-enabled AI assistant built with **LiveKit Agents**, supporting **speech-to-text (STT), text-to-speech (TTS), LLM responses**, and noise cancellation. Designed with a **micro-architecture**, separating agents, sessions, and utilities for maintainability and scalability.  

---

## 📁 Project Structure

  voice-agent/
  ├── src/
  │ ├── agents/
  │ │ ├── init.py
  │ │ └── voice_agent.py # Voice agent logic
  │ ├── sessions/
  │ │ ├── init.py
  │ │ └── entrypoint.py # Orchestrates agent sessions
  │ ├── utils/
  │ │ ├── init.py
  │ │ └── logger.py # Logger setup
  │ │ └── config.py # Loads .env and API keys
  │ └── main.py # Entrypoint to run the agent
  ├── .env # Environment variables and API keys
  ├── requirements.txt
  ├── README.md
  └── .gitignore


---

## ⚡ Features

- **Voice interaction** via LiveKit Agents.
- **Speech-to-text (STT)** with AssemblyAI.
- **Text-to-speech (TTS)** with ElevenLabs.
- **Language understanding** using Groq LLM.
- **Voice activity detection (VAD)** with Silero.
- **Noise cancellation** via BVC plugin.
- Modular micro-architecture for easier maintenance.

---

## 🛠️ Setup Instructions

1. **Clone the repository**
```bash
git clone <your_repo_url>
cd voice-agent-micro
---
2. **Create and activate a virtual environment**
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

3.  ** Install dependencies **
pip install -r requirements.txt

4.  ** Create .env file in the project root with your API keys: **
LIVEKIT_API_KEY=your_livekit_api_key
LIVEKIT_API_SECRET=your_livekit_api_secret
LIVEKIT_URL=wss://your-livekit-server-url
ASSEMBLYAI_API_KEY=your_assemblyai_key
ELEVENLABS_API_KEY=your_elevenlabs_key
GROQ_API_KEY=your_groq_key


5. ** Running the Voice Agent **
python -m src.main dev
dev enables development mode for LiveKit agents.
The agent will automatically connect to LiveKit, initialize STT, TTS, and LLM, and start interacting with users.

