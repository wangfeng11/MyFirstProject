#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import _thread
from time import sleep, ctime
import logging

logging.basicConfig(level=logging.INFO)

loops = [2, 4]


# 加入锁概念
def loop(nloop, nsec, lock):
    logging.info("start loop" + str(nloop) + " at " + ctime())
    # 智能睡眠时间
    sleep(nsec)
    logging.info("end loop" + str(nloop) + " at " + ctime())
    # 释放锁
    lock.release()


def main():
    logging.info("start all at " + ctime())
    locks = []
    nloops = range(len(loops))
    # 加锁，开启一个子进程
    for i in nloops:
        # 声明一个锁
        lock = _thread.allocate_lock()
        # 加锁操作
        lock.acquire()
        # 获取所有锁
        locks.append(lock)
    # 执行线程
    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))
    for i in nloops:
        while locks[i].locked(): pass
    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()
