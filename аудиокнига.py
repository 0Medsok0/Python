from gtts import gTTS
import os

with open(r"C:\Users\Acer\Desktop\3.txt", 'r') as f:
    text = f.read()

audio = 'audio.mp3'
langue = 'ru'
sp = gTTS(text=text, lang=langue, slow=False)
sp.save(audio)