#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of build

import os

class Study_rsa:
    '''
    Class for study rsa
    '''

    input = ''

    def __init__(self, input):

        self.input = input
        return

    def rsa_2048(self):
        # https://www.pycryptodome.org/src/signature/pkcs1_v1_5#Crypto.Signature.pkcs1_15.PKCS115_SigScheme.sign
        from Crypto.PublicKey import RSA
        from Crypto.Signature import pkcs1_15
        from Crypto.Hash import SHA256
        print('rsa 2048')

        os.makedirs('test', exist_ok=True)

        key = RSA.generate(2048)
        private_key = key.export_key()
        file_out = open("test/private.pem", "wb")
        file_out.write(private_key)
        file_out.close()

        public_key = key.publickey().export_key()
        file_out = open("test/public.pem", "wb")
        file_out.write(public_key)
        file_out.close()

        os.remove('test/private.pem')
        os.remove('test/public.pem')
        os.removedirs("test")

        message = b'To be signed'
        h = SHA256.new(message)
        signature = pkcs1_15.new(key).sign(h)
        #print(signature)

        try:
            pkcs1_15.new(key).verify(h, signature)
            print('The signature is valid.')
        except (ValueError, TypeError):
            print('The signature is not valid.')

        return

def study_rsa_func():
    mystudy = Study_rsa(1)
    mystudy.rsa_2048()
    return

