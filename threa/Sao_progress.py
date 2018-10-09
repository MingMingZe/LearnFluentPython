import time
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor,as_completed


def fibonacc(n):
    return 1 if n < 2 else fibonacc(n-1)+fibonacc(n-2)

def sao_sleep(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    with ThreadPoolExecutor(3) as executor:
        # task_list = [executor.submit(fibonacc, (num)) for num in range(20, 35)]
        task_list = [executor.submit(sao_sleep, (i)) for i in [2, 3, 2, 3, 5]]
        t0 = time.time()
        for future in as_completed(task_list):
            result = future.result()
            print(result)
        print("thread spend {}".format(time.time()-t0))

    with ProcessPoolExecutor(3) as executor:
        # task_list = [executor.submit(fibonacc, (num)) for num in range(20, 35)]
        task_list = [executor.submit(sao_sleep, (i)) for i in [2, 3, 2, 3, 5]]
        t0 = time.time()
        for future in as_completed(task_list):
            result = future.result()
            print(result)
        print("progress spend {}".format(time.time()-t0))
