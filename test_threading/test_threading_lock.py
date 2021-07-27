#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import _thread
import threading
from time import sleep, ctime
import logging

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


# 加入锁概念
def loop(nloop, nsec):
    logging.info("start loop" + str(nloop) + " at " + ctime())
    # 智能睡眠时间
    sleep(nsec)
    logging.info("end loop" + str(nloop) + " at " + ctime())


def main():
    logging.info("start all at " + ctime())
    threads = []
    nloops = range(len(loops))
    # 执行线程
    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)
    for i in nloops:
        threads[i].start()
    for i in nloops:
        threads[i].join()
    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()
