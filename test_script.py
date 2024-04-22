"""script para testar o modelo xml"""

import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'Z:\\placas_cd\\tesseract\\tesseract.exe'

def detect_plate(frame):
    plate_cascade = cv2.CascadeClassifier('Z:\\placas_cd\\train_dir\\cascade.xml')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in plates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)

        roi = gray[y:y + h, x:x + w]

        plate_text = pytesseract.image_to_string(roi, config='--psm 11')

        print(f'placa {plate_text}')

    return frame

video = 'Z:\\placas_cd\\video.MTS'
cap = cv2.VideoCapture(video)

desired_width = 640
desired_height = 480

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (desired_width, desired_height))

    frame_with_plates = detect_plate(frame)

    cv2.imshow(video, frame_with_plates)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
