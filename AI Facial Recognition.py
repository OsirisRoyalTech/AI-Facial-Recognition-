import cv2
import face_recognition
import pyttsx3
import os

# Initialize text-to-speech engine
engine = pyttsx3.init()


# Function to speak text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Load reference image (your face) to compare against
def load_reference_image(image_path):
    if not os.path.exists(image_path):
        print(f"Reference image not found at {image_path}")
        speak("Reference image not found. Please set up your face first.")
        return None
    reference_image = face_recognition.load_image_file(image_path)
    reference_encoding = face_recognition.face_encodings(reference_image)[0]
    return reference_encoding


# Compare the captured image with the reference image
def compare_faces(reference_encoding, captured_image):
    # Get face locations and encodings in the captured image
    face_locations = face_recognition.face_locations(captured_image)
    face_encodings = face_recognition.face_encodings(captured_image, face_locations)

    if len(face_encodings) == 0:
        return False

    for face_encoding in face_encodings:
        # Compare the reference face with each detected face
        match = face_recognition.compare_faces([reference_encoding], face_encoding)
        if match[0]:
            return True
    return False


# Function to access the laptop using facial recognition
def face_recognition_login(reference_image_path):
    speak("Please look at the camera for verification.")
    print("Please look at the camera for verification.")

    # Load reference encoding
    reference_encoding = load_reference_image(reference_image_path)
    if reference_encoding is None:
        return

    # Initialize webcam
    video_capture = cv2.VideoCapture(0)

    while True:
        ret, frame = video_capture.read()
        if not ret:
            speak("Failed to grab image from the camera.")
            break

        # Show live webcam feed (optional)
        cv2.imshow("Camera", frame)

        # Check if the face matches the reference
        if compare_faces(reference_encoding, frame):
            speak("Face recognized! Access granted.")
            print("Access granted.")
            break
        else:
            speak("Face not recognized. Please try again.")
            print("Face not recognized. Please try again.")

        # Exit after some time or if the user presses the 'q' key
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close windows
    video_capture.release()
    cv2.destroyAllWindows()


# Main function to initiate the facial recognition login process
def main():
    # Specify the path to the reference image (e.g., 'my_face.jpg')
    reference_image_path = "my_face.jpg"

    speak("Welcome to your laptop. Starting facial recognition security.")
    print("Starting facial recognition security.")

    # Start the face recognition process
    face_recognition_login(reference_image_path)


if __name__ == "__main__":
    main()
