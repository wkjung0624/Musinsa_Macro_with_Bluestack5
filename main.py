# * adb commands 
#   - https://gist.github.com/Pulimet/5013acf2cd5b28e55036c82c91bd56d8

# * 크롬 원격 디버깅
#   - https://velog.io/@jeongsick82/Android-WebView-%EC%9B%90%EA%B2%A9-%EB%94%94%EB%B2%84%EA%B9%85
#   - https://backstreet-programmer.tistory.com/m/30   
#   - 하지만 어플에서의 WEBVIEW 작동이 어려웠음(다른방법이있나?), 크롬은 잘 동작함

# * 실행 시간 측정
#   - https://opentutorials.org/module/2980/17436
    
# * 블루스택 윈도우창 가져오기
#   - https://pythondocs.net/pyautogui/pywinauto-pyautogui-%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%8A%B9%EC%A0%95-%EC%9C%88%EB%8F%84%EC%9A%B0-%EC%B0%BD-%ED%99%9C%EC%84%B1%ED%99%94-%ED%83%80%EC%9D%B4%ED%8B%80%EB%AA%85-%EC%9D%B4%EC%9A%A9/

# 사용법
# adb 설치
# 블루스택 설치 (+ 무신사 앱)
# JDK 설치
# 모듈 설치
#  - pip install pyautogui pywinauto
#  - appium 설치
# Node.js 설치
# 환경변수 등록
#  - appium 에서 설정 가능
#  - ANDROID_HOME >> C:\Users\Uni\AppData\Local\Android\Sdk
#  - JAVA_HOME >> C:\Program Files\Java\jdk-17.0.1

# Android environment
from appium import webdriver

# python controller
import pyautogui as pag
import pygetwindow as gw
import pywinauto

from time import sleep, time
import os

host = '127.0.0.1'
port = 57166

os.system(f'adb connect {host}:{port}')
os.system(f'adb devices')

# 어플 테스트에 필요한 정보들을 기입해 줍니다.
desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '7.1'
desired_caps['deviceName'] = 'Android Emulator'
# desired_caps['app'] = './musinsa.apk'
desired_caps['newCommandTimeout'] = 30000
desired_caps['autoGrantPermissions'] = True # 자동으로 권한 허용해주는것
desired_caps['appPackage'] = 'com.musinsa.store' # package: name='com.musinsa.store'
desired_caps['appActivity'] = 'com.musinsa.store.scenes.deeplink.DeepLinkActivity' # launchable-activity: name='com.musinsa.store.scenes.deeplink.DeepLinkActivity'
# desired_caps['udid'] = '127.0.0.1:63716' #adb devices

# 520, 950
# screenshot 기능 동작을 위해 pip install pillow 필요함
#skyship366xmyf5kb

def click(coord_X, coord_Y):
    return f'adb shell input tap {coord_X} {coord_Y}'

def swipe(coord_X1, coord_Y1, coord_X2, coord_Y2, duration):
    return f'adb shell input swipe {coord_X1} {coord_Y1} {coord_X2} {coord_Y2} {duration}'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

win = gw.getWindowsWithTitle('BlueStacks')[0] # 윈도우 타이틀에 Chrome 이 포함된 모든 윈도우 수집, 리스트로 리턴
if win.isActive == False:
    pywinauto.application.Application().connect(handle=win._hWnd).top_window().set_focus()
win.activate() # 윈도우 활성화
win.left, win.top = 0, 0
print(win.left, win.top, win.bottom, win.right)


# 최초 권한 리스트 항목 모달창 동의
while True:
    if pag.screenshot().getpixel((win.left + 266, win.top + 724)) == (0,120,255):
        print("@@@@@@@@ 최초 권한 리스트 체크")
        os.system(click(400, 1200))
        break

# 첫화면 알림설정 동의
while True:
    if pag.screenshot().getpixel((win.left + 386, win.top + 573)) == (0,120,255):
        print("@@@@@@@@ 첫 화면 알림설정 동의 체크")
        os.system(click(630, 950))
        break

# '오늘 그만 볼래요' 클릭
while True:
    if pag.screenshot().getpixel((win.left + 450, win.top + 900)) == (0,120,255):
        print("오늘 그만 볼랴요 클릭 체크")
        os.system(click(450, 1570))
        break

# 최초 로그인 하기 (알림종 모양)
while True:
    if pag.screenshot().getpixel((win.left + 100, win.top + 930)) == (0,0,0):
        print("로그인 버튼(알림종 모양) 클릭")
        os.system(click(43, 74))
        break

# 로그인 폼 작성
while True:
    
    if pag.screenshot().getpixel((win.left + 300, win.top + 250)) == (0,0,0):        

        os.system(click(500, 180))
        pag.write(f'skyship36')
        
        sleep(0.01) # 없으면 아이디 제대로 입력안됨
        
        os.system(click(500, 270))
        pag.write(f'6xmyf5kb')
        
        # 로그인 버튼 클릭
        os.system(click(500, 375))
        break

#로그인 마치고 알림창 떴을때 뒤로가기 버튼 클릭
while True:
    if pag.screenshot().getpixel((win.left + 300, win.top + 250)) == (255,255,255):
        print("뒤로가기 버튼 클릭")
        os.system(click(40, 70))
        break
    
# # 블프창 진입
# sleep(0.5)
# os.system(click(450, 500))

# # 특가 탭 클릭
# while True:
#     sleep(0.5)
#     if pag.screenshot().getpixel((win.left + 5, win.top + 280)) == (4,100,208):
#         os.system(click(564, 547))
#         break
    
# exit(0)
# 10:00 탭 클릭
# os.system(click(700, 800))
# sleep(0.5)

# 에어팟 아이템 탭 클릭
# while True:
#     sleep(0.5)
#     if pag.screenshot().getpixel((win.left + 96, win.top + 616)) == (0,120,255):
#         os.system(click(90, 955))
#         break

########## 본게임 여기부터 ###################
# input("로그인부터 해")
# 구매하기 버튼, 색깔 RGB(0,120,255)
# 안되면 열릴때까지 refresh
input("macro ready")
start = 0

while True:
## 첫번째 - 상품화면
    while True:
        start = time()
        # 화면 갱신 제스처(쓸어내리기)
        os.system(swipe(450, 100, 450, 800, 200))
        # 딜레이
        sleep(0.5) # 너무 빠르면 안됨, 여기가 문제네
        
        if pag.screenshot().getpixel((win.left + 450, win.top + 930)) == (0,120,255):    
            # 최초로 구매버튼 클릭 
            
            os.system(click(600, 1550))
            break
        
    while True:
        # 장바구니 담기 배경색 감지시
        if pag.screenshot().getpixel((win.left + 90, win.top + 930)) == (51,51,51):    
            # 옵션 선택창 구매버튼 (이어서)
            os.system(click(600, 1550))
            break
    print("1")  
    
    

    ## 두번째 - 주문서작성
    while True:
        print("2")  
        # 최하단 결제하기(파란색) 버튼 감지시
        if pag.screenshot().getpixel((win.left + 45, win.top + 930)) == (0,120,255):    
            # --,---원 결제하기 버튼
            os.system(click(600, 1550))
            break

    while True:
        # 전체 동의하기 라디오박스 회색 배경(미체크) 감지시
        print("3")  
        if pag.screenshot().getpixel((win.left + 26, win.top + 814)) == (241,241,241):
            # 전체 동의하기 버튼
            os.system(click(55, 1340))
            break
            
    while True:    
        # 전체 동의하기 라디오박스 회색 배경(미체크) 감지시
        print("4")  
        if pag.screenshot().getpixel((win.left + 26, win.top + 814)) == (0,120,255):
            # --,---원 동의선택 후 결제하기 버튼 다시 클릭
            os.system(click(600, 1550))
            break





    # 세번째 - 이용약관 동의 화면
    while True:
        # 하단 회색 여백공간 감지 시
        print("5")  
        if pag.screenshot().getpixel((win.left + 240, win.top + 600)) == (226,226,226):
            # 이용약관 동의(전체) 체크박스 클릭
            os.system(click(784, 292))
            break

    while True:
        # 최하단 다음 버튼(빨간색) 감지 시
        if pag.screenshot().getpixel((win.left + 330, win.top + 900)) == (246,68,68):
            # 현금영수증 방법 리스트박스 클릭
            os.system(click(450, 765))
            break
        
    while True:    
        # 현금영수증 지출증빙용 리스트 아이템 흰 배경 감지 시
        if pag.screenshot().getpixel((win.left + 300, win.top + 600)) == (255,255,255):
            # 현금영수증 미발행 클릭
            os.system(click(450, 830))
            break
        
    while True:  
        # 하단 회색 여백공간 감지 시  
        if pag.screenshot().getpixel((win.left + 240, win.top + 600)) == (226,226,226):
            # 최종결제 완료
            os.system(click(650, 1525))
            print(time()-start)
            break
        
    if input("One more? (0 to exit)") == 0:
        break

# os.system('adb shell screencap -p /sdcard/screen.png') 화면캡처 후 저장
# os.system('adb shell screencap /sdcard/screen.dump')
# os.system('adb pull /sdcard/screen.png') 스마트폰 -> PC 로 캡처 옮김

pretty_xml_as_string = dom.toprettyxml()
print(pretty_xml_as_string)
# driver.switch_to.context('WEBVIEW')

# 가볍게 테스트를 해봅니다.
# 테스트 코드는 실행하는 앱에 따라서 다르게 나옵니다!
assert '지금 한강은' in driver.page_source
driver.quit()