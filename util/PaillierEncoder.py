"""
platform: win
env: sec_env(phe included)
name: PaillierEncoder.py
dive into phe
"""

from phe import paillier
from util.Timer import Timer


def encode(target):
    """
    encode a list of data(float)
    :param target:
    :return:
    """
    timer = Timer()
    pubk, prvk = paillier.generate_paillier_keypair()
    enc_target = [pubk.encrypt(d) for d in target]
    timer.cut("encode")
    dec_target = [prvk.decrypt(c) for c in enc_target]
    timer.cut("decode")
    return dec_target


if __name__ == '__main__':
    print(encode([1, 2, 3, 3.14]))
