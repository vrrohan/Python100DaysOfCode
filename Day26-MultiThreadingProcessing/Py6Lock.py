import time, multiprocessing

'''
why we need lock ?
- Becus 2 process or thread try to access a shared resource it creates lots of problems like data inconsistency
'''

def deposit(balance, lock) :
    for i in range(100) :
        time.sleep(0.01)
        #code between acquire() & release() is called critical section i.e. shared resource
        lock.acquire()
        balance.value = balance.value + 1
        lock.release()

def withdraw(balance, lock) :
    for i in range(100) :
        time.sleep(0.01)
        lock.acquire()
        balance.value = balance.value - 1
        lock.release()

if __name__ == '__main__' :
    balance = multiprocessing.Value('i', 200)
    #lets create a lock & pass that lock to both processes
    lock = multiprocessing.Lock()
    d = multiprocessing.Process(target=deposit, args=(balance, lock))
    w = multiprocessing.Process(target=withdraw, args=(balance, lock))
    d.start()
    w.start()
    d.join()
    w.join()
    print(balance.value)
