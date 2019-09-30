import time, threading

def calSquare(numList) :
    print('calculating square of numbers : ')
    for num in numList :
        time.sleep(0.5)
        print('square :', num)

def calCube(numList) :
    print('calculating cube of numbers : ')
    for num in numList :
        time.sleep(0.3)
        print('cube :', num)

numList = [2, 3, 4, 9, 7, 1, 10, 11, 22, 17, 5, 6, 14]
start = time.time()

print(calSquare(numList))
print(calCube(numList))

end = time.time()

print(end - start)

start = time.time()
#we create 2 threads, pass name of function in target & list of tuples to arguments
threadOne = threading.Thread(target=calSquare, args=(numList,))
threadTwo = threading.Thread(target=calCube, args=(numList,))
threadOne.start()
threadTwo.start()

threadOne.join()
threadTwo.join()
end = time.time()

print('finished in', end-start, 'time')
