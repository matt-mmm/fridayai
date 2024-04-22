#all necessary imports here
import speech_recognition as sr
from gtts import gTTS
import os
from openai import OpenAI
import playsound

#insert your api key here!!!
client = OpenAI(api_key='your api key here')

#initializing speech recognition recognizer
r = sr.Recognizer()

#method to listen for key word (you can change to whatever you want to fit your needs)
def listen_for_key_word(r, key_word='friday'):
    #prompts user for key word
    print("Awaiting key word...")
    with sr.Microphone() as micinput:
        #while loop to listen using system mic and if key word is recognized to listen to the prompt
        while True:  
            audio = r.listen(micinput)
            try:
                text = r.recognize_google(audio).lower()
                if key_word in text:  
                    print("Wake word authorized, listening for prompt.")
                    #helper handle_command function
                    return handle_command(r, micinput)
            #base error handling
            except Exception as e:
                print("Error : " + str(e))

#method to parse command and prep to utilize model
def handle_command(r, micinput):
    #defines audio
    audio = r.listen(micinput)  
    #takes in your prompt from system mic, exports as text to be used in model
    try:
        prompt = r.recognize_google(audio)
        print(f"You said: {prompt}")
        #kill-switch: if the phrase "rudolph" is said, the assistant shuts down
        if prompt.lower() == "rudolph":  
            print("Shutting down, goodbye!")
            return None 
        return prompt
    #basic error handling
    except Exception as e:
        print("Error recognizing command: " + str(e))

#method to get response to text from model
def get_response(text):
    #you can replace the model with whatever you want, you can see the list of models in OpenAI README
    response = client.chat.completions.create(model="gpt-4-turbo-2024-04-09",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": text},
    ])
    #return model response to text
    return response.choices[0].message.content

#method to create, play and delete audio file with response given by model
def speak(text):
    #utilizes Google text to speech package, can choose what language you want
    tts = gTTS(text=text, lang='en')
    filename = 'response.mp3'
    #saving audio file
    tts.save(filename)
    #playing audio file
    playsound.playsound(filename)
    #deleting audio file
    os.remove(filename)





