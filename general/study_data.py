#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of build

class Study_data:
    '''
    Class for study data
    '''

    input = ''

    def __init__(self, input):

        self.input = input

    def data_list(self):

        # list
        stack = [1, 3, 2]
        stack.append(4)
        print(stack)
        value = stack.pop()
        print(stack)
        print(value)
        stack.sort()
        print(stack)
        del stack[1]
        print(stack)

        # dict
        tel = {'tom':1111, 'lily':2222}
        print(tel)
        tel['tom'] = 3333
        print(tel)
        tel['test'] = 8888
        print(tel)
        if 'test' in tel:
            print(tel['test'])
        if 'jack' not in tel:
            tel['jack'] = 9999
        print(tel)

        for k, v in tel.items():
            print(v, end=' ')
        print('')

        basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
        for f in sorted(set(basket)):
            print(f)
        return

def study_data_func():
    my_data = Study_data(1)
    my_data.data_list()
    return

