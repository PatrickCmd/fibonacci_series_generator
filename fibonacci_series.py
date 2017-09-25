"""Prints fibonacci series from 0 to 0 nth term
    Usage:
        python fibonacci_series.py
 """

def generate_fibonacci_series(n):
    """Generate fibonacci series from 0 to nth term
    args:
        n->nth term of fibonnaci series    
    Returns:
        A list of numbers of fibpnacci series to the nth term
    """
    n1 = 0
    n2 = 1
    count = 0
    fibonacci_series = []
    
    if not isinstance(n, int):
        raise ValueError('nth term must be an integer')
    elif n <= 0:
        raise ValueError("nth term must be postive")
    elif n == 1:
        fibonacci_series.append(n1)
        return fibonacci_series
    else:
        while count < n:
            fibonacci_series.append(str(n1))
            nth = n1 + n2
            n1, n2 = n2, nth
            count += 1
    return fibonacci_series

if __name__ == '__main__':
    nterms = 10
    print('Fibonacci series form 0 to {}: {}' \
           .format(nterms, ' '.join(generate_fibonacci_series(nterms))))
    
    nterms = 30
    print('Fibonacci series form 0 to {}: {}' \
           .format(nterms, ' '.join(generate_fibonacci_series(nterms))))
         
