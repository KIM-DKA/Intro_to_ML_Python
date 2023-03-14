
import time 
import pyautogui 

# 1분 간격으로 180번 돌리면 3시간 동안은 사라질 수 있음 (해상도 1724 x 1117)

for i in range(0,1000):
    print(i)
    pyautogui.moveTo(100,100)    
    time.sleep(60) # 60초에 한번씩 움직이기 
    pyautogui.moveTo(500,500)
    
