import cv2

# 컬러 이미지 불러오기
img = cv2.imread('MG.jpg')

# 이미지를 흑백으로 변환하기
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 이미지 크기를 변경하여 화면에 출력하기
cv2.namedWindow('Gray Image', cv2.WINDOW_NORMAL)  # 창의 이름 지정
cv2.resizeWindow('Gray Image', 1000, 700)  # 창의 크기 지정
cv2.imshow('Gray Image', gray)
cv2.waitKey(0)
cv2.destroyAllWindows()
