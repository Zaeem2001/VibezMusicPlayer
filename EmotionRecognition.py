# IMPORTING NECESSARY LIBRARIES
import cv2
import numpy as np
from keras.models import load_model
from keras.preprocessing import image
from keras.preprocessing.image import img_to_array

class Emotion:
    def __init__(self):
        # MODELS AND HAAR CASCADE FOR FACIAL DETECTION
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        self.model = load_model('EmotionDetectionModel.h5')
        self.emotions = ['Angry', 'Happy', 'Neutral', 'Sad', 'Surprise']

        self.capture = cv2.VideoCapture(0)

    def startCapture(self):
        self.capture = cv2.VideoCapture(0)

        while True:
            # MAKE SURE FRAMES ARE BEING READ PROPERLY
            read, frame = self.capture.read()
            if (not read):
                print('Frames have NOT been read properly')
                break

            # FACIAL DETECTION
            gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            face_detected = self.face_cascade.detectMultiScale(gray_img, 1.3,
                                                               5)  # detects and 'draws' rectangle around face

            for (x, y, w, h) in face_detected:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # actually draws the rectangle
                roi_gray = gray_img[y:y + h, x:x + w]  # region of interest (focus on the face)
                roi_gray = cv2.resize(roi_gray, (48, 48),
                                      interpolation=cv2.INTER_AREA)  # resize image for better processing

                # EMOTION DETECTION
                if np.sum([roi_gray]) != 0:
                    roi = roi_gray.astype(
                        'float') / 255.0  # convert pixel values from 0-255 to 0-1 to make processing easier
                    roi = img_to_array(roi)  # convert to array to pass onto model
                    roi = np.expand_dims(roi, axis=0)

                    prediction = self.model.predict(roi)[0]
                    emotion_prediction = self.emotions[prediction.argmax()]

                    cv2.putText(frame, emotion_prediction, (int(x), int(y)), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

            # DISPLAY VIDEO FOOTAGE
            cv2.imshow('Emotion Detector', frame)

            # emergency break
            if cv2.waitKey(20) & 0xFF == ord(' '):
                break

