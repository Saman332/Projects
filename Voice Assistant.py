import speech_recognition as sr
import pyttsx3
from googletrans import Translator  

def speak(text, language="en"):
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)  
    voices = engine.getProperty('voices')
    
    if language == "en":
        engine.setProperty('voice', voices[0].id)  
    else:
        engine.setProperty('voice', voices[1].id)
    
    engine.say(text)
    engine.runAndWait()
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎤 Please speak now in English...")
        audio = recognizer.listen(source)

    try:
        print("🔍 Recognizing speech...")
        text = recognizer.recognize_google(audio, language="en-US") 
        print(f"✅ You said: {text}")
        return text
    except sr.UnknownValueError:
        print("❌ Could not understand the audio.")
    except sr.RequestError as e:
        print(f"❌ API Error: {e}")
    return ""

def translate_text(text, target_language="es"):  
    translator = Translator()
    translation = translator.translate(text, dest=target_language)
    print(f"🌍 Translated text: {translation.text}")
    return translation.text

# Display language options to the user
def display_language_options():
    print("🌍 Available translation languages: ")
    print("1. Urdu (ur)")
    print("2. Punjabi (pa)")
    print("3. Spanish (es)")
    print("4. French (fr)")
    print("5. German (de)")
    print("6. Chinese (zh-cn)")
    print("7. Japanese (ja)")
    print("8. Korean (ko)")
    print("9. Arabic (ar)")

    # User selects language
    choice = input("Please select the target language number (1-8): ")
    language_dict = {
        "1": "ur",
        "2": "pa",
        "3": "es",
        "4": "fr",
        "5": "de",
        "6": "zh-cn",
        "7": "ja",
        "8": "ko",
        "9": "ar"
    }
    
    return language_dict.get(choice, "es")  # Default to Spanish if invalid input

# Main function to combine all steps
def main():
    target_language = display_language_options()
    
    original_text = speech_to_text()
    
    if original_text:
        translated_text = translate_text(original_text, target_language=target_language)
 
        speak(translated_text, language="en")  
        print("✅ Translation spoken out!")

if __name__ == "__main__":
    main()
