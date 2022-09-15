
from ..permutation.encrypt import permutation_encrypt
from .shift import shift

def shift_encrypt(text: str, key: int, alphabet: str = "abcdefghijklmnopqrstuvwxyz"):
    permutation_key = shift(
        text = alphabet,
        key = key
    )
    return permutation_encrypt(
        text = text,
        key = permutation_key
    )