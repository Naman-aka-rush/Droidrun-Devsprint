import speech_recognition as sr
from gtts import gTTS
import os
from playsound import playsound
import random

class AudioEngine:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def speak(self, text):
        if not text or len(text) < 2:
            return
        
        # Clean text to remove the tag if it accidentally slipped in
        clean_text = text.replace("VOICE_SUMMARY:", "").strip()
        print(f"Assistant: {clean_text}") 
        
        filename = f"speech_{random.randint(1, 100000)}.mp3"
        try:
            tts = gTTS(text=clean_text, lang='en', slow=False)
            tts.save(filename)
            playsound(filename)
        except Exception as e:
            print(f"Audio Error: {e}")
        finally:
            if os.path.exists(filename):
                try:
                    os.remove(filename)
                except:
                    pass

    def listen(self, timeout=40, phrase_time_limit=40):
        self.speak("I am listening.")
        
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                print("Listening...")
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=phrase_time_limit)
        
            print("Processing audio...")
            command = self.recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.WaitTimeoutError:
            print("Timeout.")
            return None
        except Exception as e:
            print(f"Mic Error: {e}")
            return None