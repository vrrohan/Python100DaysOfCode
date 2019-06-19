import pyautogui, requests, random
from selenium import webdriver
from bs4 import BeautifulSoup as bs
pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True
GAME_2048_WEBLINK = 'http://play2048.co/'
GOOGLE_CHROME_DRIVER_WINDOWS_PATH = 'D:\\Python\\python for web\\chromedriver_win32\\chromedriver.exe'
GAME_2048_WEBPAGE_LOAD_TIMEOUT = 45

def getResponseFrom2048Link(gameLinkResponse) :
    try :
        gameLinkResponse.raise_for_status()
        print('2048 Game Response OK, Status : ' + str(gameLinkResponse.status_code))
    except Exception as e :
        print('Error getting response from 2048...', e)

def displayWebsiteInChrome(browser) :
    try :
        browser.get(GAME_2048_WEBLINK)
        browser.set_page_load_timeout(GAME_2048_WEBPAGE_LOAD_TIMEOUT)
    except Exception as e :
        print('Website timeout, unable to load website in 45 secs', e)

#Main Program execution starts from here...
gameLinkResponse = requests.get(GAME_2048_WEBLINK)
getResponseFrom2048Link(gameLinkResponse)
botMoves = int(input('select bot moves between 75 to 300 : '))
if botMoves >= 75 and botMoves <=300 :
    #Get the object for handling chrome browser
    browser = webdriver.Chrome(executable_path=GOOGLE_CHROME_DRIVER_WINDOWS_PATH)
    displayWebsiteInChrome(browser)
    #get to start the game
    pyautogui.click(200, 200)
    keyPresses = ['left', 'down']
    leftDownPressed = 1
    rightPressed = 1
    for i in range(botMoves) :
        key = keyPresses[random.randint(0, len(keyPresses)-1)]
        if i%15==0 and i>=15 :
            pyautogui.press('right')
            print('right pressed', i)
        else :
            pyautogui.press(key)
            print(str(key) + ' key pressed...' +  str(i))
else :
    print('bot moves limit out of given range. execution stops.')
