from gtts import gTTS
import os


def voice (voice):
    
    tts = gTTS(text=str(voice), lang='pt')
    tts.save("voice.mp3")
    os.system("mpg321 voice.mp3")

