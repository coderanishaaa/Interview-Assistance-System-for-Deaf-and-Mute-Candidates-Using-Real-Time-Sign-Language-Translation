import cv2
from cvzone.HandTrackingModule import HandDetector
from cvzone.ClassificationModule import Classifier
import numpy as np
import math
import speech_recognition as sr
import threading  # To handle speech recognition without freezing the video

# Initialize video capture and modules
cap = cv2.VideoCapture(0)
detector = HandDetector(maxHands=1)
classifier = Classifier("keras_model.h5", "labels.txt")
offset = 20
imgSize = 300

labels = ["Hello", "Thank you", "Yes"]  # Labels for recognized signs

# Variables to store questions and answers
question_text = "Listening for interviewer..."  # Default question text
answer_text = ""  # The answer given by the candidate in sign language

# Initialize the recognizer for interviewer questions
recognizer = sr.Recognizer()

def listen_for_question():
    global question_text
    while True:  # Continuous listening loop
        with sr.Microphone() as source:
            try:
                recognizer.adjust_for_ambient_noise(source, duration=1)  # Adjust for background noise
                print("Listening for a question...")  # Debugging statement
                audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)  # Capture the question
                question_text = recognizer.recognize_google(audio)  # Recognize the question
                print("Question recognized:", question_text)
            except sr.UnknownValueError:
                question_text = "Could not understand the question."
                print("Error: Could not understand the audio.")  # Debugging statement
            except sr.RequestError as e:
                question_text = f"Error: {e}"
                print(f"Could not request results; {e}")  # Debugging statement
            except sr.WaitTimeoutError:
                question_text = "No question detected."
                print("Error: No question detected.")  # Debugging statement

# Start the listening thread for real-time voice recognition
listening_thread = threading.Thread(target=listen_for_question, daemon=True)
listening_thread.start()

while True:
    success, img = cap.read()
    imgOutput = img.copy()
    hands, img = detector.findHands(img)

    # Detect hands and classify the gesture if hands are detected
    if hands:
        hand = hands[0]
        x, y, w, h = hand['bbox']

        imgWhite = np.ones((imgSize, imgSize, 3), np.uint8) * 255
        imgCrop = img[y - offset:y + h + offset, x - offset:x + w + offset]

        aspectRatio = h / w

        if aspectRatio > 1:
            k = imgSize / h
            wCal = math.ceil(k * w)
            imgResize = cv2.resize(imgCrop, (wCal, imgSize))
            wGap = math.ceil((imgSize - wCal) / 2)
            imgWhite[:, wGap: wCal + wGap] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            answer_text = labels[index]  # Update the answer text with the recognized sign

        else:
            k = imgSize / w
            hCal = math.ceil(k * h)
            imgResize = cv2.resize(imgCrop, (imgSize, hCal))
            hGap = math.ceil((imgSize - hCal) / 2)
            imgWhite[hGap: hCal + hGap, :] = imgResize
            prediction, index = classifier.getPrediction(imgWhite, draw=False)
            answer_text = labels[index]  # Update the answer text with the recognized sign

        cv2.rectangle(imgOutput, (x - offset, y - offset - 70), 
                      (x - offset + 400, y - offset + 60 - 50), (0, 255, 0), cv2.FILLED)
        cv2.putText(imgOutput, answer_text, (x, y - 30), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 0, 0), 2)
        cv2.rectangle(imgOutput, (x - offset, y - offset), 
                      (x + w + offset, y + h + offset), (0, 255, 0), 4)

        cv2.imshow('Candidate Screen - Sign Recognition', imgWhite)  # Candidate's detected sign

    # Create interviewer screen with question text
    interviewer_screen = np.ones((300, 600, 3), np.uint8) * 50  # Dark background for question screen
    cv2.putText(interviewer_screen, "Interviewer Question:", (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(interviewer_screen, question_text, (30, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    cv2.imshow("Interviewer Screen", interviewer_screen)

    # Create candidate screen with answer text
    candidate_screen = np.ones((300, 600, 3), np.uint8) * 50  # Dark background for answer screen
    cv2.putText(candidate_screen, "Candidate Answer:", (30, 50), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
    cv2.putText(candidate_screen, answer_text, (30, 100), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 2)
    cv2.imshow("Candidate Screen", candidate_screen)

    # Exit loop on pressing 'esc'
    if cv2.waitKey(1) & 0xFF == 27:  # 27 is the 'esc' key
        break

cap.release()
cv2.destroyAllWindows()
