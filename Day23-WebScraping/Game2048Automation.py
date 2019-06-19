import pyautogui, requests, random
from selenium import webdriver
from bs4 import BeautifulSoup as bs
pyautogui.PAUSE = 0.8
pyautogui.FAILSAFE = True

g2048_game_weblink = 'http://play2048.co/'

def getResponseFrom2048Link(gameLinkResponse) :
    try :
        gameLinkResponse.raise_for_status()
        print('2048 Game Response OK, Status : ' + str(gameLinkResponse.status_code))
    except Exception as e :
        print('Error getting response from 2048...', e)

def displayWebsiteInChrome(browser) :
    try :
        browser.get(g2048_game_weblink)
        browser.set_page_load_timeout(45)
    except Exception as e :
        print('Website timeout, unable to load website in 45 secs', e)

gameLinkResponse = requests.get(g2048_game_weblink)
getResponseFrom2048Link(gameLinkResponse)
botMoves = int(input('select bot moves between 75 to 300 : '))
#Get the object for handling chrome browser
browser = webdriver.Chrome(executable_path=r"D:\python\chromedriver_win32\chromedriver.exe")
displayWebsiteInChrome(browser)
#get to start the game
pyautogui.click(200, 200)
pyautogui.press('down')
pyautogui.press('left')
pyautogui.press('left')
pyautogui.press('right')
keyPresses = ['left', 'right', 'up', 'down']
soup = bs(gameLinkResponse.text, 'html.parser')
print(soup)
for i in range(botMoves) :
    key = keyPresses[random.randint(0, len(keyPresses)-1)]
    pyautogui.press(key)
    res = requests.get(g2048_game_weblink)
    ss = bs(res.text, 'html.parser')
    s = ss.findAll(class_='tile-inner')
    print(browser.find_element_by_xpath('/html/body/div[3]/div[4]/div[3]/div[5]/div'))
    print('inner tile : ', s)
    print('key pressed : ' + key)
