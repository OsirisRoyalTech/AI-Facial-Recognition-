# AI Facial Recognition
AI facial recognition Python script that adds an additional layer of security when accessing a laptop, you can use libraries like opencv for face detection, dlib or face_recognition for facial recognition, and pyttsx3 or other libraries for verbal feedback. 
The script will compare the user’s face to a stored image (the reference image) and only allow access if it matches.

# Requirements
1.	Install dependencies: <br /> You’ll need to install opencv-python, face_recognition, and pyttsx3.
pip install opencv-python face_recognition pyttsx3 <br />
2.	Facial Recognition Flow: <br /> 
o	The user will have to provide a reference image of their face. <br />
o	When they try to access the laptop, the script will capture an image of their face via the webcam and compare it to the stored reference image. <br />
o	If the face matches, the script will allow access; otherwise, it will deny access.

For educational purposes only
