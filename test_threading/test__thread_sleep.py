#!/usr/bin/env python
# -*- conding:utf-8 -*-
# author:wangfeng
import _thread
from time import sleep, ctime
import logging

logging.basicConfig(level=logging.INFO)


def loop0():
    logging.info("start loop0 at " + ctime())
    sleep(4)
    logging.info("end loop0 at " + ctime())


def loop1():
    logging.info("start loop1 at " + ctime())
    sleep(2)
    logging.info("end loop1 at " + ctime())


def main():
    logging.info("start all at " + ctime())
    # _thread没有守护线程的概念，如果主线程结束，_thread将会被强制结束
    _thread.start_new_thread(loop0, ())
    _thread.start_new_thread(loop1, ())
    # loop0()
    # loop1()
    sleep(6)
    logging.info("end all at " + ctime())


if __name__ == '__main__':
    main()
