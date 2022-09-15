import ciphers

def choose_cipher(text:str,option:str,key):
    """
    Perform a cipher depending on the chosen method,
    text and key.

    Parameters:
        text: the text to be ciphered
        option: the method to use. Available methods are:
            "permutation", "doubletransposition" and "shift"
        key: the key to use for ciphering
    
    Returns:
        the ciphered text
    """
    if option == "permutation":
        return ciphers.permutation_encrypt(
            text = text,
            key = key
        )
    if option == "doubletransposition":
        return ciphers.double_transposition_encrypt(
            text = text,
            key = key
        )
    if option == "shift":
        return ciphers.shift_encrypt(
            text=text,
            key = key
        )
    
    print("Invalid method")

def choose_decipher(ciphered_text:str,option:str,key):
    """
    Perform a decipher depending on the chosen method,
    text and key.

    Parameters:
        ciphered_text: the text to be ciphered
        option: the method to use. Available methods are:
            "permutation", "doubletransposition" and "shift"
        key: the key to use for ciphering
    
    Returns:
        the ciphered text
    """
    if option == "permutation":
        return ciphers.permutation_decrypt(
            ciphered_text = ciphered_text,
            key = key
        )
    if option == "doubletransposition":
        return ciphers.double_transposition_decrypt(
            ciphered_text= ciphered_text,
            key = key
        )
    if option == "shift":
        return ciphers.shift_decrypt(
            ciphered_text = ciphered_text,
            key = key
        )
    print("Invalid method")

def cipher(text:str, operation_keys_list:list) -> str:

    """
    Main ciphering method that follows the instructions provided by
    the list. Uses the instructions to pass through a pipeline of the
    indicated ciphers.

    Parameters:
        text: the text to encrypt
        operation_keys_list: list of tuples with two values (cipher_method,key).
            The text will be ciphered with the indicated methods, keys and in the
            order of the list. The valid cipher_methods are: "permutation",
            "doubletransposition" and "shift"
            
    Returns:
        The encrypted text

    Example:
        >>> encryption_pipeline = [
            {
                "method":"permutation",
                "key": "rfzisjncudbyekawohpgqxtmlv"
            },
            {
                "method":"shift",
                "key": "6"
            },
            {
                "method":"doubletransposition",
                "key": [[1,4,2,3],[3,2,1]]
            }
            ]
        >>> cipher(encryption_pipeline)
    """

    ciphered_text = text
    for method_key in operation_keys_list:
        ciphered_text = choose_cipher(
            text=ciphered_text,
            option=method_key["method"],
            key=method_key["key"])

    return ciphered_text
    
def decipher(ciphered_text: str, operation_keys_list) -> str:
    """
    Given an encrypt

    Parameters:
        ciphered_text: the ciphered text to decrypt
        operation_keys_list: list of tuples with two values (cipher_method,key).
            The text will be ciphered with the indicated methods, keys and in the
            order of the list. The valid cipher_methods are: "permutation",
            "doubletransposition" and "shift"
            
    Returns:
        The encrypted text

    Example:
        >>> decryption_pipeline = [
            {
                "method":"doubletransposition",
                "key": [[1,4,2,3],[3,2,1]]
            },
            {
                "method":"shift",
                "key": "6"
            }
            {
                "method":"permutation",
                "key": "rfzisjncudbyekawohpgqxtmlv"
            }
            ]
        >>> decipher(decryption_pipeline)
    """

    deciphered_text = ciphered_text
    for method_key in operation_keys_list:
        deciphered_text = choose_decipher(
            ciphered_text = deciphered_text,
            option = method_key["method"],
            key = method_key["key"])

    return deciphered_text
