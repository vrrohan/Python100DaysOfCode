import time, multiprocessing

'''
This program does it creates 2 processes -
1. Main program which contains result list :- result = []
2. Child process calSquare which contains its own copy of result list :- result = []

Since, we have separate copy of result[]
Hence, when we run this code, nothing gets displayed in result[] becus the global variable result = [] is in different process
So, how do we share data between these 2 processes ?
Solution :- Use shared memory, memory lives outside both processes. 2 ways for shared memory :-
(a) Value
(b) Array
'''
#result = []

def calSquare(numList, result, value) :
    #lets change value to 3.14 in child process
    print(value.value)
    value.value = 3.147
    print('calculating square of numbers : ')
    #we cannot use append with this result, we can access it via index number hence using with enumerate function to store each square result to its index
    for (idx, num) in enumerate(numList) :
        time.sleep(0.2)
        result [idx] = num*num

if __name__ == '__main__' :
    numList = [2, 3, 4, 9, 7, 1, 10, 11, 22, 17, 5, 6, 14]
    start = time.time()
    #specify data-type - i for integer, d for double & specify its size
    result = multiprocessing.Array('i', len(numList))
    #value is similar to array but its single value
    value = multiprocessing.Value('d', 0.11)
    #Then pass this shared memory result into p1 process
    p1 = multiprocessing.Process(target=calSquare, args=(numList, result, value))

    p1.start()
    p1.join()
    end = time.time()
    print(end - start)
    print('result is :', result[:])
    print('value is :', value.value)
