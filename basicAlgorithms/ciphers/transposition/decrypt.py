from . import utils
def double_transposition_decrypt(ciphered_text: str, key: str) -> str:
  """
  Given the original key and the ciphered text, perform
  the ivnerse of the double transposition in order to get
  the original text

  Parameters:
    ciphered_text: the ciphered text given by a double
      transposition cipher
    key: the key used to encrypt the original text

  Returns:
    the decrypted text
  """
  rows = len(key[0])
  cols = len(key[1])
  row_permutation = utils.get_reverse_transposition_permutation(key[0])
  col_permutation = utils.get_reverse_transposition_permutation(key[1])

  # Pass the text to matrix
  ciphered_text_matrix = utils.text2matrix(ciphered_text,rows,cols)

  # Transpose the columns with the inverse column transposition
  ciphered_text_matrix = utils.transpose_columns(ciphered_text_matrix,col_permutation)

  # Transpose the rows with the inverse row transposition
  ciphered_text_matrix = utils.transpose_rows(ciphered_text_matrix,row_permutation)

  # Pass the matrix text to a string
  deciphered_text = utils.matrix2text(ciphered_text_matrix)

  # Remove all of the '_' extra characters that come from the original ciphering
  i = -1
  while deciphered_text[i] == "_":
    i -= 1
  if i + 1 < 0:
    return deciphered_text[:i+1]

  return deciphered_text
  
