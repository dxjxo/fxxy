# -*- coding:utf-8 -*-
__author__ = 'Administrator'
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
import time
def run(n):
    semaphore.acquire()
    time.sleep(1)
    print("run the thread: %s" %n)
    semaphore.release()

if __name__ == '__main__':
    semaphore  = threading.BoundedSemaphore(3) #设置最多允许3个线程同时运行
    for i in range(20):
        t = threading.Thread(target=run,args=(i,))
        t.start()
while threading.active_count() != 1:
    pass
else:
    print('----done---')