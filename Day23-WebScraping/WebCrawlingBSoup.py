from bs4 import BeautifulSoup as bs
import requests
MEDIUM_WEBSITE_TECH_COLUMN_LINK = 'https://medium.com/topic/technology'

def isMediumSiteAccessible(medium_response) :
    try :
        medium_response.raise_for_status()
        print('Getting response from ' + str(MEDIUM_WEBSITE_TECH_COLUMN_LINK) + ' status : ' + str(medium_response.status_code) + ' OK')
        return True
    except Exception as e :
        print('Unable to get response from medium', e)

def getAllH3LatestTechArticlesWithLinks(src_code) :
    listOfAllH3Headings = []
    listOfAllH3Links = []
    #find all headings... h2 Tags in source code
    mediumH3Headings = src_code.findAll('h3')
    for h3 in mediumH3Headings :
        listOfAllH3Headings.append(h3)
    for h3links in mediumH3Headings :
        aTags = h3links.find('a')
        listOfAllH3Links.append(aTags.attrs['href'])
    print('All Latest Medium Tech Articles With Links : \n')
    for ((index, latestArticles), articleLink) in zip(enumerate(listOfAllH3Headings), listOfAllH3Links) :
        print(str(index+1) + ') ' + latestArticles.text)
        print('link:- ' + str(articleLink) + '\n')

def getAllH4PopularTechArticlesWithLinks(src_code) :
    listOfAllH4Headings = []
    #find all headings... h2 Tags in source code
    mediumH4Headings = src_code.findAll('h4')
    for h4 in mediumH4Headings :
        listOfAllH4Headings.append(h4)
    print('\nFew Popular Medium Tech Articles : \n')
    for (index, popularArticles) in enumerate(listOfAllH4Headings):
        print(str(index+1) + ') ' + popularArticles.text)

#Main program execution
medium_response = requests.get(MEDIUM_WEBSITE_TECH_COLUMN_LINK, verify=False)
if isMediumSiteAccessible(medium_response) :
    #Process and extract site data
    MEDIUM_TECH_PAGE_SOURCE_CODE = medium_response.content
    src_code = bs(MEDIUM_TECH_PAGE_SOURCE_CODE, features="html.parser")
    getAllH3LatestTechArticlesWithLinks(src_code)
    getAllH4PopularTechArticlesWithLinks(src_code)
else :
    print('unable to access')
