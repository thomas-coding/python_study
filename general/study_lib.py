#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of build

import os
import struct


class Study_lib:
    '''
    Class for study lib
    '''

    input = ''

    def __init__(self, input):

        self.input = input

    def lib_os_test(self):
        import os
        #help(os)
        print('lib test')
        print(os.getcwd())
        print(os.system('date'))
        return
    
    def lib_random_test(self):
        import random
        value = random.randrange(100)
        print(value)
        return
    
    def lib_net_test(self):
        import requests
        import re
        res = requests.get('http://192.168.103.66/share/doc/arm/IP/gic/v3/')
        text=res.text
        #</td><td><a href="ARM_GIC-600_r1p6-00rel0_Technical_Reference_Manual.pdf">
        #pattern=r"</td><td><a href=\"(.+?)</a></td><td align=\""
        pattern=r"</td><td><a href=\"(.+?)\">"
        result=re.findall(pattern,text)
        for element in result:
            print(element)

        return

def study_lib_func():
    mystudy = Study_lib(1)
    mystudy.lib_os_test()
    mystudy.lib_random_test()
    mystudy.lib_net_test()
    return

