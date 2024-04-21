#all necessary imports here
import speech_recognition as sr
from gtts import gTTS
import os
from openai import OpenAI

def get_response(text):
    response = client.chat.completions.create(model="gpt-4-turbo-2024-04-09",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": text},
    ])
    return response.choices[0].message.content




