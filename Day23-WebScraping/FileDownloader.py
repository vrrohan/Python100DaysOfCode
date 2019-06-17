#Download a file from a web-address & save it to some location into your system
import requests
#http://file.allitebooks.com/20190112/Java%20XML%20and%20JSON,%202nd%20Edition.pdf - java ebook pdf
#https://docs.spring.io/spring/docs/3.0.x/spring-framework-reference/pdf/spring-framework-reference.pdf
fileDownloadAddress = str(input('Enter File Download Url : '))
#get() takes string of url to download & returns a response object given back by web-server
res = requests.get(fileDownloadAddress)
#now check response, if there is any error while downloading the file
try :
    res.raise_for_status()
    print('Response : ' + str(res.status_code) + ' OK')
except Exception as ex :
    print('Error while downloading file : ' + str(ex))
#Now save the file to hard-disk of computer, open file in binary-write mode
if res.status_code == requests.codes.ok :
    fileNameSavedAs = str(input('Save File as (.pdf): '))
    with open(fileNameSavedAs, 'wb') as fileDownloaded :
        #iter_content returns 100000 bytes of content on each iteration & write to file MyDownloadSpringDocs.pdf file one by one
        for bytess in res.iter_content(100000) :
            fileDownloaded.write(bytess)
        print('File Download successfully...')
else :
    print('Unable to save & extract file')
