import numpy as np

def isprime(n):

    if n == 1:
        return False
    
    elif n == 2 or n == 3:
        return True

    else:
        for i in range(2, int(np.sqrt(n)) + 1):
            if n%i == 0:
                return False
            else:
                return True
            