#-*- coding:utf-8 -*-

import time
import sys

def print_log():
    current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    print(current_time)
    f = open('E:/log/write.log', 'a')
    f.write(current_time)
    f.write('\n')
    f.close()

if __name__ =='__main__':
    print_log()
