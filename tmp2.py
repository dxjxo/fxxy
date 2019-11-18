# -*- coding:utf-8 -*-
__author__ = 'Administrator'
#!/usr/bin/env python
# -*- coding:utf-8 -*-
import threading
def start():
    print("---start---1")
    event.isSet()
    event.wait()    #阻塞
    print("---start---2")

if __name__ == "__main__":
    event = threading.Event()
    t = threading.Thread(target=start)
    t.start()

    result=input(">>:")
    if result == "set":
        event.set() #设定set，wait不阻塞