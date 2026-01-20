import asyncio
from src.audio import AudioEngine
from src.agent import DroidBridge
from src.utils import extract_voice_summary

async def main():
    # 1. Initialize Modules
    audio = AudioEngine()
    bot = DroidBridge()
    
    audio.speak("DroidRun Accessibility Bridge Ready.")
    
    # 2. Main Interaction Loop
    while True:
        user_command = audio.listen()
        
        if user_command:
            # Check for exit commands
            if any(word in user_command.lower() for word in ["exit", "stop", "quit"]):
                audio.speak("Goodbye.")
                break
            
            # 3. Execute Task
            audio.speak("Working on it...")
            
            # Run the agent and capture the raw logs
            logs = await bot.execute_task(user_command)
            
            # Print logs for developer debugging
            print("--- AGENT LOGS ---")
            print(logs)
            print("------------------")
            
            # 4. Extract and Speak Summary
            summary = extract_voice_summary(logs)
            audio.speak(summary)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass