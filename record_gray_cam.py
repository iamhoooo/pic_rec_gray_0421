import cv2
import keyboard
import numpy as np
from datetime import datetime

# 웹캠 열기
cap = cv2.VideoCapture(0)

# 녹화를 위한 변수 초기화
fourcc = cv2.VideoWriter_fourcc(*'XVID')
fps = 20
frame_size = (640, 480)
is_color = False  # 회색으로 변환하기 위해 False로 설정
out = None
is_recording = False

while True:
    # 프레임 읽어오기
    ret, frame = cap.read()

    # 회색으로 변환
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 화면에 프레임 표시
    cv2.imshow('Webcam Recording', gray_frame)

    # 'r' 키를 눌러 녹화 시작
    if keyboard.is_pressed('r') and not is_recording:
        # 이전 녹화 파일 닫기
        if out is not None:
            out.release()

        # 현재 날짜와 시간을 이용하여 파일 이름 생성
        now = datetime.now()
        output_filename = now.strftime("%Y%m%d_%H%M%S.avi")
        
        # 새로운 녹화 파일 생성
        out = cv2.VideoWriter(output_filename, fourcc, fps, frame_size, is_color)
        is_recording = True
        print(f'Recording started. Output file: {output_filename}')

    # 's' 키를 눌러 녹화 종료
    if keyboard.is_pressed('s') and is_recording:
        # 녹화 종료
        out.release()
        is_recording = False
        print('Recording stopped')

    # 't' 키를 눌러 스크린샷 찍기
    if keyboard.is_pressed('t'):
        # 현재 날짜와 시간을 이용하여 파일 이름 생성
        now = datetime.now()
        screenshot_filename = now.strftime("%Y%m%d_%H%M%S.png")
        # 스크린샷 찍기
        cv2.imwrite(screenshot_filename, gray_frame)
        print(f'Screenshot saved as {screenshot_filename}')

    if is_recording:
        # 녹화 중인 경우 현재 프레임을 녹화 파일에 추가
        out.write(gray_frame)

    # 'q' 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 웹캠과 OpenCV 창 닫기
cap.release()
cv2.destroyAllWindows()