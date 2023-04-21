import cv2

# 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 흑백, 칼라 전환 변수 초기화
show_color = True

def mouse_callback(event, x, y, flags, param):
    global show_color

    # 마우스 왼쪽 버튼이 눌러졌을 때
    if event == cv2.EVENT_LBUTTONDOWN:
        # 흑백, 칼라 전환
        show_color = not show_color

# 카메라 윈도우 생성
cv2.namedWindow('Camera')

# 마우스 이벤트 콜백 함수 등록
cv2.setMouseCallback('Camera', mouse_callback)

while True:
    # 비디오 프레임 읽어오기
    ret, frame = cap.read()

    if show_color:
        # 칼라로 화면에 출력하기
        cv2.imshow('Camera', frame)
    else:
        # 흑백으로 변환하기
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        # 변환된 이미지를 화면에 출력하기
        cv2.imshow('Camera', gray)

    # 'q' 키를 누르면 종료하기
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# 객체 해제 및 윈도우 닫기
cap.release()
cv2.destroyAllWindows()
