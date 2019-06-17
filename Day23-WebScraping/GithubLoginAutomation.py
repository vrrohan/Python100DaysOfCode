from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests, bs4, time

def checkWebsitePageResponseStatus(response, spring_boot_app_creator_website) :
    """This method checks the response status of website, whether website is available or not. status=200 means its available"""
    try :
        #check if Response status is 200 or not
        response.raise_for_status()
        print('Wesbite Response : ' + str(response.status_code) + ' Ok')
    except Exception as excp :
        print('Error while getting Response from website : ' + spring_boot_app_creator_website, str(excp))

def loadAndMaximizeGithubLoginPage(browser) :
    """This Automated function first maximize github homepage, then finds Sign-in button & clicks on it to go to login page"""
    try :
        browser.maximize_window()
        dropboxLoginPage = browser.find_element_by_link_text('Sign in').click()
    except Exception as e :
        print('Element not found', e)

def automateEmailAddressOrUsername(browser) :
    """This Automated function finds username input area & sends username to input area"""
    try :
        browser.find_element_by_name('login').send_keys('vrrohan')
    except Exception as e :
        print('Username Element not found', e)

def automateLoginPassword(browser) :
    """This Automated function finds password input area & sends Password to input area"""
    try :
        browser.find_element_by_name('password').send_keys('testgithub7')
    except Exception as e :
        print('Password Element not found', e)

def automateLoginButton(browser) :
    """This Automated function finds login button & clicks on it to login the user"""
    try :
        browser.find_element_by_name('commit').click()
    except Exception as e :
        print('Login Element not found', e)

def createNewGuthibRepository(browser, repositoryVisibility) :
    try :
        time.sleep(0.8)
        browser.find_element_by_link_text('New').click()
        time.sleep(0.8)
        browser.find_element_by_name('repository[name]').send_keys(repositoryName)
        time.sleep(0.8)
        browser.find_element_by_class_name('js-repository-readme-choice').click()
        time.sleep(0.8)
        if (repositoryVisibility.lower=='public') :
            browser.find_element_by_id('repository_visibility_public').click()
        else :
            browser.find_element_by_id('repository_visibility_private').click()
        time.sleep(0.8)
        browser.find_element_by_xpath('/html/body/div[4]/main/div/form/div[3]/button').click()
        print('repository created successfully')
    except Exception as e :
        print('Some Repository creating element not found', e)

def getRepositoryLink(browser) :
    try :
        browser.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div[1]/div[3]/details[2]/summary').click()
        time.sleep(1)
        newGitReposLink = browser.find_element_by_xpath('/html/body/div[4]/div/main/div[2]/div[1]/div[3]/details[2]/div/div/div[1]/div[1]/div/input').get_attribute('value')
        print(newGitReposLink)
    except Exception as e :
        print('Unable to find newly created repository link', e)

#Github Homepage Website Link
github_homepage_website_link = 'http://github.com/'
repositoryName = str(input('Enter Repository Name to create : '))
repositoryVisibility = str(input('Make Repository public or private : '))
#Get the content from Dropbox Homepage
githubResponse = requests.get(github_homepage_website_link)
try :
    checkWebsitePageResponseStatus(githubResponse, github_homepage_website_link)
except Exception as excp :
    print(excp)
#Get chromedriver to test on chrome browser
browser = webdriver.Chrome(executable_path=r"D:\python\chromedriver_win32\chromedriver.exe")
browser.get(github_homepage_website_link)
browser.set_page_load_timeout(15)
loadAndMaximizeGithubLoginPage(browser)
print('Login Page loaded...')
#After Login Page is loaded, sleep for 2 seconds
time.sleep(0.8)
automateEmailAddressOrUsername(browser)
time.sleep(0.8)
automateLoginPassword(browser)
automateLoginButton(browser)
time.sleep(2)
createNewGuthibRepository(browser, repositoryVisibility)
time.sleep(5)
getRepositoryLink(browser)
