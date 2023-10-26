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

    def data(self):
        print('stud data enter')
        return 0

def study_data_func():
    my_data = Study_data(1)
    my_data.data()
    return 0

