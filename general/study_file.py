#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of build

import os
import struct


class Study_file:
    '''
    Class for study file
    '''

    input = ''

    def __init__(self, input):

        self.input = input

    def file_str_test(self):
        print('file test')
        os.makedirs('test', exist_ok=True)
        f = open('test/strfile', 'w', encoding="utf-8")
        f.write('This is a test1\n')
        f.write('This is a test2\n')
        f.flush()
        f.closed
        f = open('test/strfile', 'r+', encoding="utf-8")
        #line1 = f.readline()
        #print(line1)
        for line in f:
            print(line)
        f.closed
        os.remove('test/strfile')
        os.removedirs("test")
        return

    def file_binary_test(self):
        print('file test')
        os.makedirs('test', exist_ok=True)
        f = open('test/binfile', 'w+b')
        binary = bytearray([0x12, 0x34, 0x56, 0x78]) 
        f.write(binary)
        f.flush()
        f.closed
        f = open('test/binfile', 'rb')
        size = os.path.getsize('test/binfile')
        for i in range(size):
            data = f.read(1)
            num = struct.unpack('B', data)
            print(hex(num[0]), end=' ')
        print('\n')
        f.closed
        os.remove('test/binfile')
        os.removedirs("test")
        return

def study_file_func():
    mystudy = Study_file(1)
    mystudy.file_str_test()
    mystudy.file_binary_test()
    return

