#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of build

from study_control import study_control_func
from study_data import study_data_func
from study_file import study_file_func
from study_lib import study_lib_func
import sys

def help():
    print('0 -- control')
    print('1 -- data')
    print('2 -- file')
    print('3 -- lib')

if __name__ == '__main__':
    print('study main')
    help()

    #arg = int(sys.argv[1])
    #print('arg:', arg)
    choice = int(input("Please enter an integer: "))
    if choice == 0:
        study_control_func()
    elif choice == 1:
        study_data_func()
    elif choice == 2:
        study_file_func()
    elif choice == 3:
        study_lib_func()
    else:
        help()


