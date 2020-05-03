#Usage
#python test.py --detector Tools/face_detection_model --embedding-model Tools/openface_nn4.small2.v1.t7 --recognizer output/recognizer.pickle --le Tools/output/le.pickle


import numpy as np
import argparse
import imutils
import pickle
import time
import cv2
import os
import speech_recognition as sr
import vlc
import subprocess
import datetime

ap = argparse.ArgumentParser()
ap.add_argument("-d", "--detector", required=True,
	help="path to OpenCV's deep learning face detector")
ap.add_argument("-m", "--embedding-model", required=True,
	help="path to OpenCV's deep learning face embedding model")
ap.add_argument("-r", "--recognizer", required=True,
	help="path to model trained to recognize faces")
ap.add_argument("-l", "--le", required=True,
	help="path to label encoder")
ap.add_argument("-c", "--confidence", type=float, default=0.5,
	help="minimum probability to filter weak detections")
args = vars(ap.parse_args())

# Capturing your face
cam = cv2.VideoCapture(0)
cv2.namedWindow("test")

while True:
    ret, frame = cam.read()
    cv2.imshow("test", frame)
    if not ret:
        break
    k = cv2.waitKey(1)
    if k%256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        image = frame
        break

# load our serialized face detector from disk
print("[INFO] loading face detector...")
protoPath = os.path.sep.join([args["detector"], "deploy.prototxt"])
modelPath = os.path.sep.join([args["detector"],
	"res10_300x300_ssd_iter_140000.caffemodel"])
detector = cv2.dnn.readNetFromCaffe(protoPath, modelPath)

# load our serialized face embedding model from disk
print("[INFO] loading face recognizer...")
embedder = cv2.dnn.readNetFromTorch(args["embedding_model"])

# load the actual face recognition model along with the label encoder
recognizer = pickle.loads(open(args["recognizer"], "rb").read())
le = pickle.loads(open(args["le"], "rb").read())

# load the image, resize it to have a width of 600 pixels (while
# maintaining the aspect ratio), and then grab the image dimensions
#image = cv2.imread(args["image"])
image = imutils.resize(image, width=600)
(h, w) = image.shape[:2]

# construct a blob from the image
imageBlob = cv2.dnn.blobFromImage(
	cv2.resize(image, (300, 300)), 1.0, (300, 300),
	(104.0, 177.0, 123.0), swapRB=False, crop=False)

# apply OpenCV's deep learning-based face detector to localize
# faces in the input image
detector.setInput(imageBlob)
detections = detector.forward()

# loop over the detections
for i in range(0, detections.shape[2]):
	# extract the confidence (i.e., probability) associated with the
	# prediction
	confidence = detections[0, 0, i, 2]

	# filter out weak detections
	if confidence > args["confidence"]:
		# compute the (x, y)-coordinates of the bounding box for the
		# face
		box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
		(startX, startY, endX, endY) = box.astype("int")

		# extract the face ROI
		face = image[startY:endY, startX:endX]
		(fH, fW) = face.shape[:2]

		# ensure the face width and height are sufficiently large
		if fW < 20 or fH < 20:
			continue

		# construct a blob for the face ROI, then pass the blob
		# through our face embedding model to obtain the 128-d
		# quantification of the face
		faceBlob = cv2.dnn.blobFromImage(face, 1.0 / 255, (96, 96),
			(0, 0, 0), swapRB=True, crop=False)
		embedder.setInput(faceBlob)
		vec = embedder.forward()

		# perform classification to recognize the face
		preds = recognizer.predict_proba(vec)[0]
		j = np.argmax(preds)
		proba = preds[j]
		name = le.classes_[j]

# use the audio file as the audio source
r = sr.Recognizer()

#use Microphone to record live Speech
with sr.Microphone() as source:
    print ('Say Something!')
    audio = r.listen(source)
    print ('Done!')
    a = (datetime.datetime.today().hour)
    print(a)


if(0 <= a <= 11):
    subprocess.call(['espeak','Good Morning Mr. {}'.format(name)])
elif (12 <= a <= 16):
    subprocess.call(['espeak','Good Afternoon Mr. {}'.format(name)])
else:
    subprocess.call(['espeak','Good Evening Mr. {}'.format(name)])


# recognize speech using Houndify
HOUNDIFY_CLIENT_ID = "Enter your Client_ID"  # Get it on Houndify Speech to Text API
HOUNDIFY_CLIENT_KEY= "Enter your Client_key"  # Get it on Houndify Speech to Text API

try:
    a = r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)
    print("Houndify thinks you said ==> " + a )
    print(type(a))
	# This part is where you can change the program and customize it based on the face recognition result
    if (a == "play music" and name == "Parthan"): # The idea is to customize based on who's asking
        subprocess.call(['espeak','Playing Back in Black by AC DC'])
        p = vlc.MediaPlayer("Back_in_black.mp3")
        p.play()
        time.sleep(500)
        p.stop()
# Try more elif statements for different recognized faces

except sr.UnknownValueError:
    print("Houndify could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Houndify service; {0}".format(e))
