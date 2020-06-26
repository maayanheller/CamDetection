import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

def capture():
    while True:
        ret, frame = cap.read()
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