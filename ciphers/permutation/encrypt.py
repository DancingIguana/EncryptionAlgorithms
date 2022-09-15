def permutation_encrypt(text: str, 
                key: str, 
                alphabet: str = "abcdefghijklmnopqrstuvwxyz"
                ) -> str:
  """
  Perform a permutation encryption by doing a substitution of
  the alphabet letters. This substitution depends on a permutation
  of the alphabet itself.

  Parameters:
    text: the text to cipher
    key: the key used to cipher the text (a permutation of the
      alphabet)
    alphabet: the ordered alphabet to be expected
  
  Returns:
    the encrypted text
  """

  # Minimum requirements
  if set(alphabet) != set(key):
    print("Invalid key/alphabet")
    print("Key must be a permutation of the alphabet")
    return

  alphabet2key = {}
  for alphabet_letter, key_letter in zip(list(alphabet),list(key)):
    alphabet2key[alphabet_letter] = key_letter

  ciphered_text = ""

  for letter in text:
    ciphered_text += alphabet2key[letter]
  
  return ciphered_text
