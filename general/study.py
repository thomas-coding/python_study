#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of build

from study_control import study_control_func
from study_data import study_data_func

def help():
    print('0 -- control')
    print('1 -- data')

if __name__ == '__main__':
    print('study main')
    help()
    choice = int(input("Please enter an integer: "))
    if choice == 0:
        study_control_func()
    elif choice == 1:
        study_data_func()
    else:
        help()


