import cv2, face_recognition, os
from time import gmtime, strftime

today = strftime("%Y-%m-%d %H-%M-%S", gmtime())
print(today)

filename = today + ".mp4"
res = '720p'
frames_per_second = 24.0

def change_res(cap, width, height):
    cap.set(3, width)
    cap.set(4, height)


STD_DIMENSIONS = {
    "480p": (640, 480),
    "720p": (1280, 720),
    "1080p": (1920, 1080),
    "4k": (3840, 2160),
}


def get_dims(cap, res='1080p'):
    width, height = STD_DIMENSIONS["480p"]
    if res in STD_DIMENSIONS:
        width, height = STD_DIMENSIONS[res]
    # change the current caputre device
    # to the resulting resolution
    change_res(cap, width, height)
    return width, height


VIDEO_TYPE = {
    'avi': cv2.VideoWriter_fourcc(*'XVID'),
    'mp4': cv2.VideoWriter_fourcc(*'XVID'),
}


def get_video_type(filenameparam):
    filenameparam, ext = os.path.splitext(filenameparam)
    if ext in VIDEO_TYPE:
        return VIDEO_TYPE[ext]
    return VIDEO_TYPE['avi']


cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
out = cv2.VideoWriter(filename, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 3, get_dims(cap, res))
cascPath = "./haarcascade_frontalface_default.xml"
face_cascade = cv2.CascadeClassifier(cascPath)
face_locations = []

def capture():
    frame_count = 0
    while True:
        ret, frame = cap.read()
        # Convert the image from BGR color (which OpenCV uses) to gray color
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face_locations = face_recognition.face_locations(gray)
        # Draw a rectangle around the faces
        for top, right, bottom, left in face_locations:
            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)
        if ret == True and len(face_locations) >= 1:
            out.write(frame)
            frame_count = frame_count + 1
            print(frame_count)
        cv2.imshow('Face Detection Program', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            # When everything done, release the capture
            cap.release()
            out.release()
            cv2.destroyAllWindows()
            break

def main():
    capture();

if __name__ == "__main__":
    main()