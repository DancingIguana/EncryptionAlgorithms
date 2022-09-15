from . import utils

def double_transposition_encrypt(text: str,key: tuple) -> str:
  """
  Perform a double transposition encryption for a text.

  Parameters:
    text: a string of text,
    key: it consists of a tuple with two elements:
      - a list of the permutation of rows
      - a list of the permutation of columns
  
  Returns:
    encripted text
  """

  row_permutation = key[0]
  col_permutation = key[1]
  rows = len(row_permutation)
  cols = len(col_permutation)

  # Permutation of rows is a sequence with numbers from 1 to rows
  for i, row in enumerate(sorted(row_permutation)):
    if i + 1 != row:
      print("Make sure that the permutation of rows is from 1 to n_rows")
      return

  # Permutation of columns is a sequence with numbers from 1 to columns
  for i, col in enumerate(sorted(col_permutation)):
    if i + 1 != col:
      print("Make sure that the permutation of columns is from 1 to n_columns")
      return

  # Pass text to a matrix of r * c
  matrix = utils.text2matrix(text,rows,cols)

  # Transpose the rows
  transposed_rows_matrix = utils.transpose_rows(matrix,row_permutation)

  # Transpose the columns
  transposed_rows_cols_matrix = utils.transpose_columns(transposed_rows_matrix,col_permutation)

  # Pass the matrix to the text string
  ciphered_text = utils.matrix2text(transposed_rows_cols_matrix)

  return ciphered_text

