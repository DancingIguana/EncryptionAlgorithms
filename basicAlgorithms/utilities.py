def normalize(s):
    """
    Cleans the string of text by:
    - removing accents
    - Passing all letters to lowercase
    - Removing all non alphanumeric characters
    - Removing whitespaces
    - Replacing ñ to 'ni'
    """
    s = s.lower()
    replacements = (
        ("á", "a"),
        ("é", "e"),
        ("í", "i"),
        ("ó", "o"),
        ("ú", "u"),
        ("ñ", "ni"),
        (" ", ""),
        ("¿", ""),
        ("?", ""), 
        (".", ""),
        (",", ""),
        (":", ""),
        ("!", ""),
        ("¡", ""),
        (";", ""),
    )
    for a, b in replacements:
        s = s.replace(a, b)
    return s