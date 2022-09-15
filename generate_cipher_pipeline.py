import random
import json
def generate_random_cipher_pipeline(n:int,alphabet:str,shift_range:tuple,r:int,c:int):
    """
    Given a number of ciphers, the alphabet and the number of 
    rows and columns for a matrix where the text fits, generate a
    pipeline of methods randomly chosen with randomly generated keys
    to pass through a ciphering pipeline.

    Parameters:
        n: the number of methods to apply (they may be repeated)
        alphabet the alphabet of the text to encrypt
        r: number of rows the text has if passed into a matrix
        c: the number of columns the text has if passed into a matrix

    Returns:
        List of the methods to use
    """
    operations_keys = []
    methods = ["shift","permutation","doubletransposition"]
    for i in range(n):
        method = random.choice(methods)
        key = None
        if method == "shift":
            key = random.randint(shift_range[0],shift_range[1])
        if method == "permutation":
            key = list(alphabet)
            random.shuffle(key)
            key = "".join(key)
        if method == "doubletransposition":
            row_permutation = [i + 1 for i in range(r)]
            col_permutation = [i +1 for i in range(c)]

            random.shuffle(row_permutation)
            random.shuffle(col_permutation)
            key = [row_permutation,col_permutation]
        
        method_key = {
            "method": method,
            "key": key
        }
        operations_keys.append(method_key)
    
    return operations_keys

if __name__ == "__main__":
    with open("input.json","r") as f:
        data = json.load(f)
    
    n = int(input("Number of ciphering methods to use: "))
    shift_lower = int(input("Shift lower key value: "))
    shift_upper = int(input("Shift higher key value: "))
    r = int(input("Number of matrix rows: "))
    c = int(input("Number of matrix columns: "))

    data["cipherPipeline"] = generate_random_cipher_pipeline(
        n = n,
        alphabet="abcdefghijklmnopqrstuvwxyz",
        shift_range=(shift_lower,shift_upper),
        r = r,
        c = c
    )

    with open("input.json","w") as f:
        json.dump(data,f,indent = 6)