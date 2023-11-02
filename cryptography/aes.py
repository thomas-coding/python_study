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
        # AES128(ECB) data = '1234567887654321' ciphertext = '8E9654EC7220B59BF8A48D750F879DFA'
        from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
        print('aes 128')
    
        data = b'1234567887654321'
        key = b'1122334455667788'

        cipher = Cipher(algorithms.AES(key), modes.ECB())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(data) + encryptor.finalize()
        hex_str = ciphertext.hex()
        print(ciphertext)
        print(hex_str)

        decryptor = cipher.decryptor()
        text = decryptor.update(ciphertext) + decryptor.finalize()
        print(text)
        text_hex_str = text.hex()
        print(text_hex_str)
        return

def study_aes_func():
    mystudy = Study_aes(1)
    mystudy.aes128()
    return

