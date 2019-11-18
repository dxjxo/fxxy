# -*- coding:utf-8 -*-
__author__ = 'Administrator'
from multiprocessing import Process
import time
def start(name):
    time.sleep(1)
    print('hello', name)

if __name__ == '__main__':
    p = Process(target=start, args=('zhangsan',))
    p1 = Process(target=start, args=('lisi',))
    p.start()
    p1.start()
    p.join()
