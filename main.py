import speech_recognition as sr
import webbrowser
import pyttsx3
import musiclibrary
import requests
# import google.generativeai as genai
# import genai
# import google
import api


recognizer = sr.Recognizer()

engine = pyttsx3.init()
# newsapi = "e342c08c9f8a409a91b43fdd0f92bc19"
# genai_api = "AIzaSyDa4uPEoukYxJYIE7YxHCTlFnuqGdzWNHY"
def speak(text):
    engine.say(text)
    engine.runAndWait()

def processcommand(c):
    print(c)
    if "open google" in c.lower():
        webbrowser.open("http://google.com")
    elif  "open facebook" in c.lower():
        webbrowser.open("http://facebook.com")
    elif  "open youtube" in c.lower():
        webbrowser.open("http://youtube.com")
    elif  "open linkedin" in c.lower():
        webbrowser.open("http://linkedin.com") 
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musiclibrary.music[song]
        webbrowser.open(link)

    elif 'news' in c.lower():
        rr = requests.get("https://newsapi.org/v2/everything?q=tesla&from=2025-04-15&sortBy=publishedAt&apiKey=e342c08c9f8a409a91b43fdd0f92bc19")
        if rr.status_code == 200:
         data = rr.json()
         print("Fetched articles:")
         for article in data['articles'][:5]:  # Limit to first 5 for preview
          speak(article['title'])

        else:
         print("Error:", rr.status_code, rr.text)

    else :
        from google import genai
        client = genai.Client(api_key="AIzaSyDa4uPEoukYxJYIE7YxHCTlFnuqGdzWNHY")
        response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents= c.lower(),
)
        speak(response.text)     

if __name__ == "__main__":
    speak("initializing jarvis")
while True:
    r = sr.Recognizer()
    
    print("recognizing...")
    try:
        with sr.Microphone() as source :
         print("Listening.....")
         audio = r.listen(source , timeout=2 , phrase_time_limit=3)
         word =   r.recognize_google(audio)
         print(word)
         if(word.lower() == "jarvis"):
             speak("yaa")
             with sr.Microphone() as source:
                 print("jarvis active ....")
                 audio = r.listen(source)
                 command = r.recognize_google(audio)
                 processcommand(command)
                 
    except sr.UnknownValueError:
        print("jarvis could not understand audio")
    except sr.RequestError as e:
        print("Jarvis error;{0}".format(e))
