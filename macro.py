#from PIL import ImageGrab
import pyautogui as pag
from time import sleep
import os

def click(coord_X, coord_Y):
    return f'adb shell input tap {coord_X} {coord_Y}'

def write(string):
    return f'adb shell input text {string}'

def swipe(coord_X1, coord_Y1, coord_X2, coord_Y2):
    # 43 = duration(ms)
    return f'adb shell input swipe {coord_X1} {coord_Y1} {coord_X2} {coord_Y2} 20'
    


# 나중엔 클래스를 만들어서 os.system 을 한번에 처리할수 있도록 바꿔

host = '127.0.0.1'
port = 63716

os.system(f'adb connect {host}:{port}') # abc connect 127.0.0.1:63716
os.system(f'adb devices')
os.system(f'adb shell wm size')

# 900 x 1600
# 페이지 로딩 느려지는거 예상해야함

# 일단 구매하기 활성화될때까지 무한반복
# 화면 새로고침
# os.system(swipe(450, 800, 450, 100))

# # 구매하기 버튼
# os.system(click(450, 1580))
# sleep(0.5)

# # 옵션 선택창 구매버튼
# os.system(click(850, 1580))

# 화면 내리기
os.system(swipe(450, 1580, 450, 1400))

# 전체동의 
os.system(click(40, 1350))

# 가상결제 시 전체동의
os.system(click(780, 300))
