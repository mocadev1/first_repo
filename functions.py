def add(a, b : float) -> float:
    """ Returns the addition of two numbers """
    return float(a + b)

def substraction(a, b: float) -> float:
    """ Returns the substraction of two numbers """
    if(a < 0):
        return 0
    return float (a - b)