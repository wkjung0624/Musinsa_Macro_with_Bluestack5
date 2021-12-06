# * adb commands 
#   - https://gist.github.com/Pulimet/5013acf2cd5b28e55036c82c91bd56d8

# * 크롬 원격 디버깅
#   - https://velog.io/@jeongsick82/Android-WebView-%EC%9B%90%EA%B2%A9-%EB%94%94%EB%B2%84%EA%B9%85
#   - https://backstreet-programmer.tistory.com/m/30   
#   - 하지만 어플에서의 WEBVIEW 작동이 어려웠음(다른방법이있나?), 크롬은 잘 동작함

# * 블루스택 윈도우창 가져오기
#   - https://pythondocs.net/pyautogui/pywinauto-pyautogui-%EB%A5%BC-%EC%9D%B4%EC%9A%A9%ED%95%9C-%ED%8A%B9%EC%A0%95-%EC%9C%88%EB%8F%84%EC%9A%B0-%EC%B0%BD-%ED%99%9C%EC%84%B1%ED%99%94-%ED%83%80%EC%9D%B4%ED%8B%80%EB%AA%85-%EC%9D%B4%EC%9A%A9/

# xml pretty print
import xml.dom.minidom

# Android environment
from appium import webdriver

# python controller
import pyautogui as pag
import pygetwindow as gw
import pywinauto

from time import sleep
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

sleep(3)
# 최초 권한 리스트 항목 모달창 동의
while True:
    sleep(0.5)
    if pag.screenshot().getpixel((win.left + 266, win.top + 724)) == (0,120,255):
        print("@@@@@@@@ 최초 권한 리스트 체크")
        os.system(click(400, 1200))
        break

# 첫화면 알림설정 동의
print("### 통화")
sleep(1)
while True:
    sleep(0.5)
    if pag.screenshot().getpixel((win.left + 386, win.top + 573)) == (0,120,255):
        print("@@@@@@@@ 첫 화면 알림설정 동의 체크")
        os.system(click(630, 950))
        break
print("### 통화")
sleep(1)
# 블프입장
while True:
    sleep(0.5)
    if pag.screenshot().getpixel((win.left + 450, win.top + 900)) == (0,120,255):
        print("블프 확인 버튼 체크")
        os.system(click(450, 1480))
        break
print("### 통화")
sleep(1)
# 특가 탭 클릭
while True:
    sleep(0.5)
    if pag.screenshot().getpixel((win.left + 5, win.top + 322)) == (0,120,255):
        os.system(click(564, 547))
        break
    

exit(0)
# 10:00 탭 클릭
# os.system(click(700, 800))
# sleep(0.5)

# 에어팟 아이템 탭 클릭
while True:
    sleep(0.5)
    if pag.screenshot().getpixel((win.left + 96, win.top + 616)) == (0,120,255):
        os.system(click(90, 955))
        break


# 520, 950
# screenshot 기능 동작을 위해 pip install pillow 필요함
# 구매하기 버튼, 색깔 RGB(0,120,255)
while True:
    sleep(0.5)
    if pag.screenshot().getpixel((win.left + 450, win.top + 930)) == (0,120,255):
        os.system(click(450, 1580))
        break
    
    pag.moveTo(200, 250)
    os.system(swipe(450, 100, 450, 800, 200))
    


# 옵션 선택창 구매버튼


# 구매시 로그인 버튼
while True:
    sleep(0.5)
    
    if pag.screenshot().getpixel((win.left + 300, win.top + 250)) == (0,0,0):
        
        pag.click(x=300,y=125)
        pag.typewrite('skyship36')
        sleep(0.1)
        pag.click(x=300,y=200)
        pag.typewrite('6xmyf5kb')
        
        #pag.click(x=300,y=250)
        os.system(click(500, 375))
        
        sleep(0.1)
        os.system(click(462, 1123))
        break

# 결제하기 버튼 클릭
while True:
    sleep(0.5)
    
    if pag.screenshot().getpixel((win.left + 376, win.top + 940)) == (0,0,0):
        os.system(click(630, 1530))
        sleep(0.1)
        # 전체 동의하기 버튼
        os.system(click(55, 1340))
        sleep(0.1)
        # 결제하기 버튼 클릭
        os.system(click(630, 1530))
        break

while True:
    sleep(0.5)
    
    if pag.screenshot().getpixel((win.left + 400, win.top + 950)) == (226,226,226):
        os.system(click(784, 292))
        break

# 현금영수증 발급방법 선택
while True:
    sleep(0.5)
    
    if pag.screenshot().getpixel((win.left + 330, win.top + 900)) == (246,68,68):
        # 현금영수증 방법
        os.system(click(450, 765))
        sleep(0.1)
        # 현금영수증 미발행 클릭
        os.system(click(450, 830))
        sleep(0.1)
        # 최종결제 완료
        os.system(click(650, 1525))
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