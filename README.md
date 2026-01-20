An AI-powered voice bridge that helps visually impaired users navigate Android devices using [DroidRun](https://github.com/droidrun).

## How it Works
1. **Listens:** Captures voice commands via `speech_recognition`.
2. **Reasons:** Uses DroidRun (powered by LLMs) to navigate the UI or describe the screen.
3. **Speaks:** Extracts a natural language summary from the agent's logs and speaks it aloud using `gTTS`.

## Installation

1. **Prerequisites:**
   - Python 3.9+
   - An Android device/emulator connected via ADB.
   - DroidRun configured with your API keys.

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
