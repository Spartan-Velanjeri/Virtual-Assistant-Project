# Virtual-Assistant-Project
This repo is the birth of a new Virtual Assistant. Work under progress

Currently running with Houndify as the primary STT and Espeak as the primary TTS. Can now play music (Preferably Back in Black by AC/DC)

Will be improving this repo to provide faster STT and more human TTS and with a lot of features. Stay tuned!

REQUIREMENTS!
Use virtualenv for creating a nuclear proof containment field :)

Main libraries to run the STT are portaudio and pyaudio (install in the same order)

      sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && pip3 install pyaudio //Python 3 is preferred

espeak --> sudo apt-get install espeak
Install this for the entire SpeechRecognition Suite
      
      pip3 install SpeechRecognition
      
Python bindings to play music 
  1. Install VLC player on your system
  2. Install Python Bindings to play music 
  
          pip3 install python-vlc (For python3)
      
          pip install python-vlc (For python)
      
Now you can run it!! Good Luck! 

Also do try out the Houndify Python SDK
https://static.houndify.com/sdks/python/2.0.0/houndify_python3_sdk_2.0.0.tar.gz
https://docs.houndify.com/sdks/docs/python

We plan to try out different STT (preferably offine ones) and benchmark them.
