
def permutation_decrypt(ciphered_text:str,
                        key: str,
                        alphabet: str = "abcdefghijklmnopqrstuvwxyz"
                        ) -> str:
  """
  Given the ciphered text and key, decipher the text that
  was ciphered through the permutation cipher.

  Parameters:
    ciphered_text: the ciphered text to decrypt
    key: the key that was used originally to encrypt the the
      text
    alphabet: the ordered alphabet to be expected

  Returns:
    the original text that was encrypted
  """
  
  # Minimum requirements
  if set(alphabet) != set(key):
    print("Invalid key/alphabet")
    print("Key must be a permutation of the alphabet")
    return
  key2alphabet = {}
  for key_letter,  alphabet_letter in zip(list(key),list(alphabet)):
    key2alphabet[key_letter] = alphabet_letter
  
  text = ""

  for letter in ciphered_text:
    text += key2alphabet[letter]
  
  return text