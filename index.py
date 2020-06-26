import cv2, face_recognition

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def capture():
    while True:
        ret, frame = cap.read()
        # Convert the image from BGR color (which OpenCV uses) to gray color
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_locations = face_recognition.face_locations(gray)
        # Draw a rectangle around the faces
        for top, right, bottom, left in face_locations:
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        cv2.imshow('Face Detection Program', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # When everything done, release the capture
            cap.release()
            cv2.destroyAllWindows()
            break

def main():
    capture();

if __name__ == "__main__":
    main()