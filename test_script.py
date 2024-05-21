"""script para testar o modelo xml"""

import cv2
import pytesseract
import re
import time

pytesseract.pytesseract.tesseract_cmd = r'Z:\\placas_cd\\tesseract\\tesseract.exe'

# Função para verificar se a placa é válida
def placa_valida(plate_text: str) -> bool:
    pattern = r'^[A-Z]{3}\d[A-Z]\d{2}$'
    return re.match(pattern, plate_text) is not None

# Função para processar a placa válida (exemplo: salvar no banco de dados)
def process_plate(plate_text: str):
    print(f'Processando a placa: {plate_text}')
    # Aqui você pode adicionar o código para salvar no banco de dados ou outras ações necessárias

# Função para detectar placas no frame
def detect_plate(frame):
    plate_cascade = cv2.CascadeClassifier('Z:\\placas_cd\\train_dir\\cascade.xml')

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    for (x, y, w, h) in plates:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        roi = gray[y:y + h, x:x + w]

        plate_text = pytesseract.image_to_string(roi, config='--psm 11').replace('|', '').replace(' ', '')
        print(f'{plate_text}')

        if placa_valida(plate_text):
            print(f'Placa válida detectada: {plate_text}')
            return plate_text, frame

    return None, frame

video = 'Z:\\placas_cd\\video.MTS'
cap = cv2.VideoCapture(video)

desired_width = 640
desired_height = 480

# Inicializar a flag de pausa
pause_detection = False

while cap.isOpened():
    ret, frame = cap.read()

    if not ret:
        break

    frame = cv2.resize(frame, (desired_width, desired_height))

    if not pause_detection:
        plate_text, frame_with_plates = detect_plate(frame)
        
        if plate_text:
            pause_detection = True
            process_plate(plate_text)
            time.sleep(5)  # Simulação de tempo de processamento
            pause_detection = False

    cv2.imshow(video, frame if pause_detection else frame_with_plates)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
