from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests, bs4, time
import pyautogui, os
pyautogui.PAUSE = 2
pyautogui.FAILSAFE = True
GOOGLE_CHROME_WEBDRIVER_PATH = r'D:\Python\python for web\chromedriver_win32\chromedriver.exe'
GITHUB_USER_ACCOUNT_LOGIN_USERNAME = 'vrrohan'
GITHUB_USER_ACCOUNT_LOGIN_PASSWORD = 'testgithub7'
#Github Homepage Website Link
GITHUB_HOMEPAGE_WEBSITE_LINK = 'http://github.com/'
GITBASH_WINDOWS_LOCATION = r'C:\Program Files\Git\git-bash.exe'
LOCAL_GITHUB_REPOSITORY_WINDOWS_LOCATION = r'cd d:/gitrohan'
CREATE_NEW_REPOSITORY_BUTTON_XPATH = '/html/body/div[4]/main/div/form/div[3]/button'
NEWLY_CREATED_REPOSITORY_CLONE_OR_DOWNLOAD_BUTTON_XPATH = '/html/body/div[4]/div/main/div[2]/div[1]/div[3]/details[2]/summary'
NEW_GITHUB_REPOSITORY_CLONE_LINK_XPATH = '/html/body/div[4]/div/main/div[2]/div[1]/div[3]/details[2]/div/div/div[1]/div[1]/div/input'
GITHUB_USER_ACCOUNT_DROPDOWN_MENU_XPATH = '/html/body/div[1]/header/div[6]/details/summary/img'
GITHUB_USER_ACCOUNT_LOGOUT_BUTTON_XPATH = '/html/body/div[1]/header/div[6]/details/details-menu/form/button'
GITHUB_PAGE_LOAD_TIMEOUT = 45

def checkWebsitePageResponseStatus(response, GITHUB_HOMEPAGE_WEBSITE_LINK) :
    """This method checks the response status of website, whether website is available or not. status=200 means its available"""
    try :
        #check if Response status is 200 or not
        response.raise_for_status()
        print('Wesbite Response : ' + str(response.status_code) + ' Ok')
    except Exception as e :
        print('Error while getting Response from website : ' + GITHUB_HOMEPAGE_WEBSITE_LINK, str(e))

def loadAndMaximizeGithubLoginPage(browser) :
    """This Automated function first maximize github homepage, then finds Sign-in button & clicks on it to go to login page"""
    try :
        browser.set_page_load_timeout(GITHUB_PAGE_LOAD_TIMEOUT)
        browser.maximize_window()
        dropboxLoginPage = browser.find_element_by_link_text('Sign in').click()
        print('Login Page loaded...')
    except Exception as e :
        print('Element not found', e)

def automateEmailAddressOrUsername(browser) :
    """This Automated function finds username input area & sends username to input area"""
    try :
        time.sleep(0.8)
        browser.find_element_by_name('login').send_keys(GITHUB_USER_ACCOUNT_LOGIN_USERNAME)
    except Exception as e :
        print('Username Element not found', e)

def automateLoginPassword(browser) :
    """This Automated function finds password input area & sends Password to input area"""
    try :
        time.sleep(0.8)
        browser.find_element_by_name('password').send_keys(GITHUB_USER_ACCOUNT_LOGIN_PASSWORD)
    except Exception as e :
        print('Password Element not found', e)

def automateLoginButton(browser) :
    """This Automated function finds login button & clicks on it to login the user"""
    try :
        time.sleep(0.8)
        browser.find_element_by_name('commit').click()
        print('User finally logged in!!!')
    except Exception as e :
        print('Login Element not found', e)

def createNewGuthibRepository(browser, repositoryVisibility) :
    """This Automated function will create a new repository, make it public or private with readme file"""
    try :
        browser.set_page_load_timeout(GITHUB_PAGE_LOAD_TIMEOUT)
        browser.find_element_by_link_text('New').click()
        time.sleep(0.8)
        browser.find_element_by_name('repository[name]').send_keys(repositoryName)
        time.sleep(0.8)
        if (repositoryVisibility.lower()=='public') :
            browser.find_element_by_id('repository_visibility_public').click()
        elif (repositoryVisibility.lower()=='private') :
            browser.find_element_by_id('repository_visibility_private').click()
        time.sleep(0.8)
        browser.find_element_by_class_name('js-repository-readme-choice').click()
        time.sleep(0.8)
        browser.find_element_by_xpath(CREATE_NEW_REPOSITORY_BUTTON_XPATH).click()
    except Exception as e :
        print('Some Repository creating element not found', e)

def getRepositoryLink(browser) :
    """This Automated function will goto clone section of newly created repository, copy the https link of newly created repository & return it back to command line so that it is cloned to local system"""
    try :
        browser.set_page_load_timeout(GITHUB_PAGE_LOAD_TIMEOUT)
        browser.find_element_by_xpath(NEWLY_CREATED_REPOSITORY_CLONE_OR_DOWNLOAD_BUTTON_XPATH).click()
        time.sleep(0.8)
        newGitReposLink = browser.find_element_by_xpath(NEW_GITHUB_REPOSITORY_CLONE_LINK_XPATH).get_attribute('value')
        print('Repository Link : ' + str(newGitReposLink))
        return str(newGitReposLink)
    except Exception as e :
        print('Unable to find newly created repository link', e)

def enterKeyPress() :
    """This Automated function will control the desktop gitbash, upon each command written by automation, it presses the enter to execute the command in gitbash"""
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

def openGitBashAndGotoGitFolder() :
    """This Automated function will open gitbash on your local system & move to your local github repository"""
    time.sleep(1)
    os.startfile(GITBASH_WINDOWS_LOCATION)
    pyautogui.click(100, 100)
    pyautogui.typewrite(LOCAL_GITHUB_REPOSITORY_WINDOWS_LOCATION)
    enterKeyPress()

def gitCloneRepositoryToDesktop(newGitRepoLink) :
    """This Automated function will clone the remote github repository to your local system"""
    pyautogui.typewrite(r'ls -lt')
    enterKeyPress()
    pyautogui.typewrite('git clone ' + newGitRepoLink)
    enterKeyPress()
    time.sleep(8)
    print('remote git repository successfully cloned to local system...')

def createGitRemoteAddNewOrigin(newGitRepoLink, repositoryName, originName) :
    """This Automated function will add a new origin of newly cloned remote github repository"""
    pyautogui.typewrite('cd ' + str(repositoryName))
    enterKeyPress()
    pyautogui.typewrite('git remote -v')
    enterKeyPress()
    pyautogui.typewrite('git remote add ' + originName + ' ' + str(newGitRepoLink))
    enterKeyPress()
    time.sleep(2)
    pyautogui.typewrite('exit')
    enterKeyPress()
    print('git remote origin added to local system')
    print('git automation completed successfully...')

def gitLoggoutFromBrowser(browser) :
    """This Automated function will run only of it is unable to create new github repository, it will logout from the user account and also closes the automated chrome browser"""
    try :
        browser.find_element_by_xpath(GITHUB_USER_ACCOUNT_DROPDOWN_MENU_XPATH).click()
        time.sleep(0.5)
        browser.find_element_by_xpath(GITHUB_USER_ACCOUNT_LOGOUT_BUTTON_XPATH).click()
        time.sleep(0.5)
        browser.quit()
    except Exception as e :
        print('Unable to find Logout Button', e)

#Main Program execution starts from here
repositoryName = str(input('Enter Repository Name to create : '))
repositoryVisibility = str(input('Make Repository public or private : '))
originName = str(input('Your local origin name : '))
#Get the content from Github Homepage
githubResponse = requests.get(GITHUB_HOMEPAGE_WEBSITE_LINK)
try :
    checkWebsitePageResponseStatus(githubResponse, GITHUB_HOMEPAGE_WEBSITE_LINK)
except Exception as e :
    print('Problem getting response from ', GITHUB_HOMEPAGE_WEBSITE_LINK, str(e))
#Get chromedriver to test on chrome browser
browser = webdriver.Chrome(executable_path=GOOGLE_CHROME_WEBDRIVER_PATH)
#opens github homepage in automated chrome web-browser
browser.get(GITHUB_HOMEPAGE_WEBSITE_LINK)
#First fully load the github homepage & then maximize it.
#Also a page load timeout is set to 45 secs. If page didn't load fully within 45 secs it will throw an error & program stops execution.
loadAndMaximizeGithubLoginPage(browser)
#After Login Page is loaded, sleep for 0.8 seconds for each email address, password and login automation
automateEmailAddressOrUsername(browser)
automateLoginPassword(browser)
automateLoginButton(browser)
#After login, @users homepage, automation on creating new repository
#A page load timeout is set to 30 secs
createNewGuthibRepository(browser, repositoryVisibility)
#After new repository is created, get the https link of newly created repository on command line
#Here page load timeout is set to 20 secs
newGitRepoLink = getRepositoryLink(browser)
if newGitRepoLink is not None :
    print('new repository created successfully on github')
    #Now open gitbash & automate it using pyautogui
    openGitBashAndGotoGitFolder()
    #Now clone newly created repository
    gitCloneRepositoryToDesktop(newGitRepoLink)
    #Now create git remote for new git repository
    createGitRemoteAddNewOrigin(newGitRepoLink, repositoryName, originName)
else :
    print('Repository already created. Unable to create new Repository with name : ' + repositoryName)
    print('Automation process shutting down.')
    gitLoggoutFromBrowser(browser)
    print('Automation Logged-out Github from chrome browser.')
