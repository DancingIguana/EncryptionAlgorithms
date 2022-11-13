def text2matrix(text:str,n_rows:int,n_cols:int) -> list:
  """
  Given a text, accomodate it in a matrix of rows*cols

  There must not be empty rows when passing the text to the matrix
  and the whole text should fit inside. Any empty values from the
  last incomplete row are filled with '_'

  Paramters:
    text: the string of text to pass to the matrixc
    n_rows: number of rows of the matrix
    n_cols: number columns of the matrix

  Returns:
    matrix with the accomodated text
  """
  text_length = len(text)
  matrix_size = n_rows * n_cols
  #Check necessary requirements
  if matrix_size < text_length:
    print("Unable to fit text inside matrix.\nPlease insert a bigger size, at least of r*c = text length")
    return 

  if matrix_size - n_cols + 1 > text_length:
    print("Matrix is too large for text.")
    print("Make sure that the text all rows and columns, only the last row is not required to be filled in completely")
    return 
  
  text_index = 0
  matrix = []
  for r in range(n_rows):
    matrix_row = []
    for c in range(n_cols):
      if(text_index <text_length):
        matrix_row.append(text[text_index])
        text_index += 1

      # If the text was filled in completely in the matrix
      # Just fill in with blank spaces
      else:
        matrix_row.append("_")
    matrix.append(matrix_row)

  return matrix

def matrix2text(matrix:list) -> str:
  """
  Given a matrix it returns it as if it was a plaintext string
  by reading from left to right and up to down.

  Parameters:
    matrix: the 2D array containing the text

  Returns:
    the string of text provided by the matrix data
  """
  text = ""
  for row in matrix:
    text += "".join(row)
  
  return text

  
def transpose_rows(matrix:list, permutation:list) -> list:
  """
  Given a matrix transpose the rows given a permutation
  of numbers from 1 to number of rows.

  Parameters:
    matrix: the 2D matrix to transpose as a double list
    permutation: an array of the permutation from 1 to n_rows

  Returns:
    the transposed matrix
  """

  # Transpose the rows
  transposed_rows_matrix = []
  for row in permutation:
    transposed_rows_matrix.append(matrix[row-1])
  
  return transposed_rows_matrix

def transpose_columns(matrix:list,permutation:list) -> list:
  """
  Given a matrix transpose the columns given a permutation
  of numbers from 1 to number of columns.

  Parameters:
    matrix: the 2D matrix to transpose as a double list
    permutation: an array of the permutation from 1 to n_cols

  Returns:
    the transposed matrix
  """
  rows,cols = len(matrix),len(matrix[0])
  transposed_cols_matrix = [[0 for i in range(cols)] for j in range(rows)]
  current_col = 0
  for col in permutation:
    for row in range(len(matrix)):
      transposed_cols_matrix[row][current_col] = matrix[row][col-1]
    current_col += 1

  return transposed_cols_matrix


def get_reverse_transposition_permutation(permutation:list)->list:
  """
  Given the original transpositions's permutation get the inverse
  permutation to return to its original state

  Parameters:
    permutation: list of the permutatino used to cipher

  Returns:
    the inverse permutation to decipher
  """
  reverse_permutation = [0 for i in range(len(permutation))]
  # p2[0] is position of 1 in p1
  # p2[1] is position of 2 in p1
  # p2[2] is position of 3 in p1
  # ...
  for i, n in enumerate(permutation):
    # p2[n-1] is position of n (i+1) in p1
    reverse_permutation[n-1] = i+1

  return reverse_permutation