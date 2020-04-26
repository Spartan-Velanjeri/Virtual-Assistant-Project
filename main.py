import speech_recognition as sr
import vlc
from time import sleep
import subprocess
import datetime as dt

# use the audio file as the audio source
r = sr.Recognizer()

#use Microphone to record live Speech
with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('Done!')
    a = (datetime.datetime.today().hour)
    if(0 < a < 11):
        subprocess.call(['espeak','Good Morning Sir!'])
    else if (12<16):
        subprocess.call(['espeak','Good Afternoon Sir!'])
    else:
        subprocess.call(['espeak','Good Evening Sir!'])


# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "Your Client ID here"  # Houndify client IDs should be inside the double quotes
HOUNDIFY_CLIENT_KEY= "Your client_key here"  # Houndify client keys should be inside the double quotes

try:
    a = r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)
    print("Houndify thinks you said ==> " + a )
    if (a == "play music"):
        subprocess.call(['espeak','Playing Back in Black by AC DC'])
        p = vlc.MediaPlayer("Back_in_black.mp3")
        p.play()
        sleep(500)
        p.stop()

except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))
