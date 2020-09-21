"""We are stating that the "phrase" argument is expected to be a string
   and that the function return a set to its caller"""
def search4vowels(phrase:str) -> set:
    """Return any vowels found in a supplied phrase."""
    vowels = set('aeiou')
    return vowels.intersection(set(phrase))

def search4letters(phrase:str, letters:str='aeiou') -> set:
    """Return a set of the 'letters' found in 'phrase'"""
    return set(letters).intersection(set(phrase))
