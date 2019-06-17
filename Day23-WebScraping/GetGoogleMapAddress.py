import webbrowser as web, sys
from selenium import webdriver

#Get address from command line
addressToSearch = str(input('Enter Address : '))
addressList = addressToSearch.split(' ')
#Google Maps address
#To install pyperclip module - pip install --user pyperclip
googleMapsAddress = 'https://www.google.com/maps/place/' + ' '.join(addressList[:])
web.open(googleMapsAddress)
#Get chromedriver to test on chrome browser
chromeBrowser = webdriver.Chrome(executable_path=r"D:\python\chromedriver_win32\chromedriver.exe")
#This will open google maps in another chrome browser
chromeBrowser.get(googleMapsAddress)
chromeBrowser.set_page_load_timeout(8)
chromeBrowser.find_element_by_id('searchbox-searchbutton').click()
