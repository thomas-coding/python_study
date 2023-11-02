#   Copyright (C) 2022 Jinping Wu.
#
#   Author: Jinping Wu <wunekky@gmail.com>
#
# This file is part of build

class Study_hash:
    '''
    Class for study hash
    '''

    input = ''

    def __init__(self, input):

        self.input = input
        return

    def hash_sha256(self):
        import cryptography
        # https://cryptography.io/en/latest/hazmat/primitives/cryptographic-hashes/
        # sha256('FirstSecond') = cad4c5623efc0ae67dbe8274e7ffc184ca91df37a8e844624240f8eef1300ce7
        print('hash sha256')
        from cryptography.fernet import Fernet
        from cryptography.hazmat.primitives import hashes
        digest = hashes.Hash(hashes.SHA256())
        digest.update(b"First")
        digest.update(b"Second")
        print(digest.finalize())

        return

def study_hash_func():
    mystudy = Study_hash(1)
    mystudy.hash_sha256()
    return

