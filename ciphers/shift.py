def reverse_shift(ciphered_text: str, key: int) -> str:
    """
    Decipher a ciphered text by the shift cipher.

    Parameters:
        ciphered_text: the encrypted text
        key: the key used to encrypt the text
    
    Returns:
        the deciphered text
    """
    n = len(ciphered_text)
    shifted = [None]*n
    if key < 0:
        key = n - key

    for i in range(n):
        shifted[(i-key)%n] = ciphered_text[i]

    return "".join(shifted)



