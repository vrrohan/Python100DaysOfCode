from multiprocessing import Pool
import time
'''
lets assume we have 4 cores. we we execute this program, os selects one of the core c2 while other cores are sitting idle
If you are doing heavy processing, giving single task to one core is not good idea while other cores are idle
can we run our code or divide our code  equally to all the cores - c1, c2, c3, c4
& in the end, we aggregate result of all 4 cores & create our final result. Here we are utilising all our 4 cores.
This is called parallel processing & process of dividing our work into 4 cores is MAP & process of aggregating the result back is called REDUCE.
'''

def fun(n) :
    sum = 0
    for x in range(1000) :
        sum += x*x
    return sum

if __name__ == '__main__' :
    start = time.time()
    #create an object of pool class
    #pool(processes = 3) it will create only 3 processes at a time
    p = Pool()
    #map() - it will divide work between multiple cores, this alone divides work between all cores(CPU), this also gives you result back
    result = p.map(fun, range(10000))
    print(result)
    end = time.time()
    p.close()
    p.join()
    print('time taken :', end-start)

    #serial processing
    t2start = time.time()
    result = []
    for x in range(10000) :
        result.append(fun(x))
    print('serial processing :', time.time() - t2start)
