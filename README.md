# Virtual-Assistant-Project
This repo is the birth of a new Virtual Assistant. Work under progress

Currently running with Houndify as the primary STT and Espeak as the primary TTS. Can now play music (Preferably Back in Black by AC/DC)

Will be improving this repo to provide faster STT and more human TTS and with a lot of features. Stay tuned!

REQUIREMENTS!
Use virtualenv for creating a nuclear proof containment field :)

Main libraries to run the STT are portaudio and pyaudio (install in the same order)

      sudo apt-get install portaudio19-dev python-all-dev python3-all-dev && pip3 install pyaudio //Python 3 is preferred

Espeak The TTS engine 

      sudo apt-get install espeak
      
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

//////////////////////////////////////////////////////////////////////////////////

Face Recognition Included now!
In order to run the program with your face to be recognised

1. In the Dataset Folder, replace the folder with my name, into your name and your photos. Remember the more the pictures, the better would be the accuracy. Also add more unknown faces, so as to further improve accuracy.

2. Next step is to Run the extract_embeddings.py file. The command to run is present in the python code itself. Check the arguments used along with the python file while running the code. 

3. Next is to Run the Train_model.py to train the SVC model for your respective dataset. The command to run is again present in the code itself.

4. Finally run the Main.py to run the Virtual Assistant which now has the capability to recognise the face used in the dataset. Also make sure to tweak the program to add your own customization. 

The way this program works is that, you have to position your face to the webcam and hit esc button to take your picture. We are working on making it a real stream rather than taking a picture of the frame.

Remember the possibilites of Vision + Voice Assistant is immense!

Finally I would like to thank you Dr Adrian Rosebrock for the wonderful tutorial and help regarding the face recognition model. Do check out his website (pyimagesearch.com)

Keep Hacking!!
