#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of build


import sys
from hash import study_hash_func
from aes import study_aes_func
from rsa import study_rsa_func

# https://github.com/pyca/cryptography
# https://cryptography.io/en/latest/
# https://pypi.org/project/cryptography/

def help():
    print('0 -- hash')
    print('1 -- aes')
    print('2 -- rsa')

if __name__ == '__main__':
    print('study cryptography main')
    help()

    #arg = int(sys.argv[1])
    #print('arg:', arg)
    choice = int(input("Please enter an integer: "))
    if choice == 0:
        study_hash_func()
    elif choice == 1:
        study_aes_func()
    elif choice == 2:
        study_rsa_func()
    else:
        help()


