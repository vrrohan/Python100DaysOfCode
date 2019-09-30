import time, multiprocessing

'''
This queue is different than queue module
'''
def calSquare(numList, q) :
    print('calculating square of numbers : ')
    #this queue is a data structures which is FIFO put() to insert data & get() to retrieve data
    for num in numList :
        q.put(num*num)

if __name__ == '__main__' :
    numList = [2, 3, 4, 9, 7, 1, 10, 11, 22, 17, 5, 6, 14]
    q = multiprocessing.Queue()
    #Then pass this shared memory result into p1 process
    p1 = multiprocessing.Process(target=calSquare, args=(numList, q))

    p1.start()
    p1.join()
    #iterating through queue & getting elements from front of queue, check if queue is not empty
    while q.empty() is False :
        print(q.get())
