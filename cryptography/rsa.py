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
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import (
            padding, rsa, utils
        )
        digest = hashes.Hash(hashes.SHA256())
        digest.update(b"First")
        print('rsa 2048')
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
        )
        public_key = private_key.public_key()

        message = b'To be signed'
        digest = hashes.Hash(hashes.SHA256())
        digest.update(message)
        h = digest.finalize()
        #import hashlib
        #h = hashlib.sha256(b"To be signed").digest()
        signature = private_key.sign(
            h,
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            utils.Prehashed(hashes.SHA256())
        )

        #new_data = h[:5] + b'000' + h[7:]
    
        try:
            public_key.verify(
                signature,
                h,
                padding.PSS(
                    mgf=padding.MGF1(hashes.SHA256()),
                    salt_length=padding.PSS.MAX_LENGTH
                ),
                utils.Prehashed(hashes.SHA256())
            )
            print('The signature is valid.')
        except (ValueError, TypeError):
            print('The signature is not valid.')
        return

def study_rsa_func():
    mystudy = Study_rsa(1)
    mystudy.rsa_2048()
    return

