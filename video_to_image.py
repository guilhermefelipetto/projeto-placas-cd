"""codigo que quebra mp4 em frames (png) para fazer as negativas"""

import cv2

def frame(video_path):
    cap = cv2.VideoCapture(video_path)

    frame_num = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_name = f"negatives\\frame_{frame_num:04d}.png"
        cv2.imwrite(frame_name, frame)
        frame_num += 1

    cap.release()
