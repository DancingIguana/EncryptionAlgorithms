
def shift(text:str, key: int) -> str:
    """
    Permorm a shift encryption by moving the letter from a text
    n spaces.

    Parameters:
        text: the text to cipher
        key: the number of spaces to move

    Returns:
        the ciphered text
    """
    n = len(text)
    shifted = [None]*n
    for i in range(n):
        shifted[(i+key)%n] = text[i]

    return "".join(shifted)