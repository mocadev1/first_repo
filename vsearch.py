"""We are stating that the "phrase" argument is expected to be a string
   and that the function return a set to its caller"""
def search4vowels(phrase:str) -> set:
    """Return any vowels found in a supplied word."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))
