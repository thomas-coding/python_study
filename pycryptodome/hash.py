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
        from Crypto.Hash import SHA256
        # https://www.pycryptodome.org/src/hash/sha256
        # sha256('FirstSecond') = cad4c5623efc0ae67dbe8274e7ffc184ca91df37a8e844624240f8eef1300ce7
        print('hash sha256')
        hash_object = SHA256.new(data=b'First')
        print(hash_object.digest_size)
        print(hash_object.block_size)
        hash_object.update(b'Second')
        digest = hash_object.digest()
        hexdigest = hash_object.hexdigest()
        print(digest)
        print(hexdigest)
        return

def study_hash_func():
    mystudy = Study_hash(1)
    mystudy.hash_sha256()
    return

