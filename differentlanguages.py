import speech_recognition as sr
import pyttsx3
from googletrans import Translator

# Initialize the recognizer
r = sr.Recognizer()
translator = Translator()

# Function to convert text to speech
def SpeakText(command):
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

while True:
    try:
        with sr.Microphone() as source2:
            r.adjust_for_ambient_noise(source2, duration=0.2)
            print("Listening...")
            audio2 = r.listen(source2)

            # Recognize speech using Google Speech Recognition
            MyText = r.recognize_google(audio2, language='hi-IN')  # Replace 'es-ES' with the desired language code
            print(f"Recognized Text (in source language): {MyText}")

            # Translate text to English
            translated_text = translator.translate(MyText, dest='en').text
            print(f"Translated Text (in English): {translated_text}")

            SpeakText(translated_text)

    except sr.RequestError as e:
        print(f"Could not request results; {e}")

    except sr.UnknownValueError:
        print("Unknown error occurred")
