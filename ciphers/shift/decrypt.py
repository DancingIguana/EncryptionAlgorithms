from ..permutation.decrypt import permutation_decrypt
from .shift import shift

def shift_decrypt(ciphered_text: str, key: int, alphabet: str = "abcdefghijklmnopqrstuvwxyz"):
    permutation_key = shift(
        text = alphabet,
        key = key
    )
    return permutation_decrypt(
        ciphered_text = ciphered_text,
        key = permutation_key
    )