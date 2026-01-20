import io
import contextlib
from droidrun import DroidAgent, DroidrunConfig

class DroidBridge:
    def __init__(self):
        self.config = DroidrunConfig()

    async def execute_task(self, user_goal):
        """
        Runs the DroidRun agent and captures its console output.
        Returns the logs as a string.
        """
        
        # We wrap the user's goal with a "System Instruction" for accessibility
        accessibility_prompt = (
            f"GOAL: {user_goal}\n"
            "IMPORTANT INSTRUCTION FOR BLIND ASSISTANCE:\n"
            "1. Perform the task as requested.\n"
            "2. When you are finished, or if you simply looked at the screen, you MUST print a final line formatted exactly like this:\n"
            "'VOICE_SUMMARY: [A short, natural sentence describing what you did or what you see for a blind user].'\n"
            "Example 1: 'VOICE_SUMMARY: I have opened WhatsApp and I see 3 unread messages.'\n"
            "Example 2: 'VOICE_SUMMARY: The screen shows the home page with the YouTube icon visible.'\n"
            "Ensure this summary is the very last thing you print."
        )

        # Initialize Agent
        agent = DroidAgent(
            goal=accessibility_prompt,
            config=self.config
            # Note: Ensure vision/reasoning are enabled in your DroidrunConfig or passed here if supported by your version
        )
        
        # Capture Output
        f = io.StringIO()
        try:
            with contextlib.redirect_stdout(f):
                await agent.run()
        except Exception as e:
            # Log the error but return what we have so far
            print(f"Agent Error: {e}")
            f.write(f"\nError: {str(e)}")
            
        return f.getvalue()