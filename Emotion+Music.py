# IMPORTING NECESSARY LIBRARIES
import tkinter as tk
from PIL import Image, ImageTk
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array
from Spotify import Spotify

class Application:
    def __init__(self):
        # MODELS AND HAAR CASCADE FOR FACIAL DETECTION
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.model = load_model('EmotionDetectionModel.h5')
        self.emotions = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']
        self.capture = cv2.VideoCapture(0)
        self.emotion_prediction = ""

        # SPOTIFY PLAYER
        self.player = Spotify()

        # GUI
        self.root = tk.Tk()
        self.root.title("Emotion+Music")
        self.root['bg'] = "black"
        self.panel = tk.Label(self.root)
        self.panel.pack()

        # BUTTONS
        play = tk.Button(self.root, text="Play Music", fg="white", bg="green", command=self.playMusic)
        play.pack(fill="both", expand=True, padx=100, pady=10)

        stop = tk.Button(self.root, text="Close Program", fg="white", bg="green", command=self.stopCapture)
        stop.pack(fill="both", expand=True, padx=100, pady=10)

        self.startCapture() # poll function to display video


    def startCapture(self):
        # MAKE SURE FRAMES ARE BEING READ PROPERLY
        read, frame = self.capture.read()
        if (not read):
            print('Frames have NOT been read properly')

        # FACIAL DETECTION
        gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_detected = self.face_cascade.detectMultiScale(gray_img, 1.3, 5)  # detects and 'draws' rectangle around face

        for (x, y, w, h) in face_detected:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # actually draws the rectangle
            roi_gray = gray_img[y:y + h, x:x + w]  # region of interest (focus on the face)
            roi_gray = cv2.resize(roi_gray, (48, 48), interpolation=cv2.INTER_AREA)  # resize image for better processing

            # EMOTION DETECTION
            if np.sum([roi_gray]) != 0:
                roi = roi_gray.astype('float') / 255.0  # convert pixel values from 0-255 to 0-1 to make processing easier
                roi = img_to_array(roi)  # convert to array to pass onto model
                roi = np.expand_dims(roi, axis=0)

                prediction = self.model.predict(roi)[0]
                self.emotion_prediction = self.emotions[prediction.argmax()]

                cv2.putText(frame, self.emotion_prediction, (int(x), int(y)), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        # DISPLAY VIDEO FOOTAGE
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors BGR -> RGB
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.panel.imgtk = imgtk
        self.panel.config(image=imgtk)  # show the image

        cv2.waitKey(0)

        self.root.after(10, self.startCapture)  # repeat this function every 10 milliseconds

    def stopCapture(self):
        print("Closing program...")
        self.root.destroy()
        self.capture.release()

    def playMusic(self):
        if (self.emotion_prediction == self.emotions[0]):
            self.player.play_angry()

        elif (self.emotion_prediction == self.emotions[1]):
            self.player.play_happy()

        elif (self.emotion_prediction == self.emotions[2]):
            self.player.play_neutral()

        elif (self.emotion_prediction == self.emotions[3]):
            self.player.play_sad()

        elif (self.emotion_prediction == self.emotions[4]):
            self.player.play_surprise()

app = Application()
app.root.mainloop()