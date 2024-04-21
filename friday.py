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

