import time, multiprocessing

def calSquare(numList) :
    print('calculating square of numbers : ')
    for num in numList :
        time.sleep(10)
        print('square :', num)

def calCube(numList) :
    print('calculating cube of numbers : ')
    for num in numList :
        time.sleep(8)
        print('cube :', num)

if __name__ == '__main__' :
    numList = [2, 3, 4, 9, 7, 1, 10, 11, 22, 17, 5, 6, 14]
    start = time.time()

    p1 = multiprocessing.Process(target=calSquare, args=(numList,))
    p2 = multiprocessing.Process(target=calCube, args=(numList,))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    end = time.time()
    print(end - start)
