#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of build

class Study_aes:
    '''
    Class for study aes
    '''

    input = ''

    def __init__(self, input):

        self.input = input
        return

    def aes128(self):
        # https://www.pycryptodome.org/src/examples#encrypt-data-with-aes
        # AES128(ECB) data = '1234567887654321' ciphertext = '8E9654EC7220B59BF8A48D750F879DFA'
        from Crypto.Cipher import AES
        #from Crypto.Random import get_random_bytes
        print('aes 128')

        data = b'1234567887654321'
        key = b'1122334455667788'

        #key = get_random_bytes(16)
        cipher = AES.new(key, AES.MODE_ECB)
        ciphertext = cipher.encrypt(data)
        print(ciphertext)

        #ciphertext, tag = cipher.encrypt_and_digest(data)
        #file_out = open("encrypted.bin", "wb")
        #[ file_out.write(x) for x in (cipher.nonce, tag, ciphertext) ]
        #file_out.close()

        return

def study_aes_func():
    mystudy = Study_aes(1)
    mystudy.aes128()
    return

