from gtts import gTTS
from playsound import playsound
file = "audio.mp3"
gTTS(
    text ="hello my name is alexa.",
    lang = "en"
).save(file)

playsound(file)
