"""
todo: salvar dados de login do banco, e demais paths em variaveis de ambiente
"""

import cv2
import pytesseract
import mysql.connector

from database_scripts.plate_processing import detect_recognize_plate

if __name__ == "__main__":
    # Conexao com o banco
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="banco_placas"
        )
        cursor = conn.cursor()

    except mysql.connector.Error as err:
        print(f'Atencao!\nErro ao tentar se conectar com o banco de dados.\n{err}')

    # Diretorio do Tesseract
    pytesseract.pytesseract.tesseract_cmd = r'Z:\\placas_cd\\tesseract\\tesseract.exe'

    # Modelo HAAR Cascade (xml)
    model = 'Z:\\placas_cd\\train_dir\\cascade.xml'

    # Caminho do video de teste
    video = 'Z:\\placas_cd\\video.MTS'

    cap = cv2.VideoCapture(video)

    desired_width = 640
    desired_height = 480

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            break

        frame = cv2.resize(frame, (desired_width, desired_height))

        plate_result = detect_recognize_plate(frame=frame, model=model, conn=conn, cursor=cursor)

        if plate_result == "sim":
            print("Placa autorizada!")
        
        elif plate_result == "não":
            print("Placa não autorizada. Acesso negado!")

        cv2.imshow('Video com Placas Detectadas', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()
    cursor.close()
    conn.close()
