# Interview Assistance System for Deaf and Mute Candidates

## 📄 Project Overview

The **Interview Assistance System** is an AI-powered real-time communication interface designed to bridge the communication gap between interviewers and deaf-mute candidates. This inclusive system enables smooth, two-way interaction by converting **spoken language to text** and **sign language to text/speech** using computer vision and speech recognition technologies.



IEEE Paper ID: `979-8-3315-3536-0/25/$31.00 ©2025 IEEE`

---

## 🚀 Key Features

- 🔤 Real-time **sign language recognition** to text/speech
- 🎤 Real-time **speech-to-text conversion**
- 🧠 **Machine Learning**-based gesture classification
- 📷 **Computer Vision** using OpenCV and CvZone for hand tracking
- 🧵 **Multithreading** for simultaneous audio and video processing
- 💬 Dual-screen UI for seamless interaction
- 🌐 Supports ASL, BSL, and Indian Sign Language variants

---

## 🧠 Technologies Used

- **Python**
- **OpenCV**
- **cvzone.HandTrackingModule**
- **SpeechRecognition (Google Speech API)**
- **Machine Learning Models (CNN/LSTM)**
- **Multithreading (Python threading module)**

---

## ⚙️ System Workflow

1. **Video Capture**: Live webcam feed is used to capture sign gestures.
2. **Gesture Recognition**: Hand gestures are detected and classified using trained ML models.
3. **Speech Recognition**: Interviewer’s audio is transcribed into text using Google Speech API.
4. **Multithreading**: Audio and video processing happen concurrently for real-time interaction.
5. **User Interface**: Recognized gestures and transcribed text are displayed on respective screens.

---

## 📝 Input/Output

- **Input**: 
  - Live video feed from candidate
  - Audio input from interviewer

- **Output**: 
  - Text/speech translation of sign language
  - Real-time text transcription of spoken questions

---

## 📊 Results

- High accuracy for simple gestures like **“Yes” (~100%)** and **“Hello” (~85%)**
- Detection speed: ~1 nanosecond per word
- Effective in quiet environments with stable lighting and proper hand visibility
- Limitations: Performance drops with background noise, gesture ambiguity, and lighting variation

---

## 🔮 Future Enhancements

- Add support for more sign languages (regional/international)
- Improve model accuracy with deep learning (e.g., VGG, ResNet, Transformer-based)
- Integrate noise cancellation for robust speech recognition
- Expand to educational, boardroom, and public communication scenarios

---

## 📚 Citation

If you use or reference this work, please cite the IEEE paper:

