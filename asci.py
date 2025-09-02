import cv2
import os
import time

# ASCII characters (dark → light)
CHARS = "@%#*+=-:. "

def frame_to_ascii(frame, cols=120, rows=35):
    # resize frame to smaller (terminal size)
    frame = cv2.resize(frame, (cols, rows))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    ascii_frame = ""
    for r in range(rows):
        for c in range(cols):
            pixel = int(gray[r, c])  # 👈 cast to int
            ascii_frame += CHARS[pixel * len(CHARS) // 256]
        ascii_frame += "\n"
    return ascii_frame


# --- Load video ---
cap = cv2.VideoCapture("282995_small.mp4")

fps = cap.get(cv2.CAP_PROP_FPS)
delay = 1 / fps

while True:
    ret, frame = cap.read()
    if not ret:
        break

    ascii_art = frame_to_ascii(frame)

    os.system("cls" if os.name == "nt" else "clear")  # clear terminal
    print(ascii_art)

    time.sleep(delay)

cap.release()
