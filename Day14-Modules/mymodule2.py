import sys, time
print('this is print statement 1')
print('this is print statement 2')

def getSystemInfo() :
    return 'Windows ' + str(sys.getwindowsversion()[0])

def getCurrentTime() :
    return str(time.localtime()[3]) + ':' + str(time.localtime()[4]) + ':' + str(time.localtime()[5])

listOFNames = ['mark', 'paul', 'steve', 'elon', 'jack']
