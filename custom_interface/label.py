from typing import Callable, Union    

def looper(fn: Callable, n:int, *args, **kwargs):
    """
    Call a function `n` times

    Parameters
    ----------
    fn: Callable
        Function to be called.
    n: int
        Number of times to call `func`.
    *args
        Positional arguments to be passed to `func`.
    **kwargs
        Keyword arguments to be passed to `func`.

    Example
    -------
    >>> def foo(a:Union[float, int], b:Union[float, int]):
    ...    '''The function to pass'''
    ...    print(a+b)
    >>> looper(foo, 3, 2, b=4)
    6
    6
    6       
    """
    for i in range(n):
        fn(*args, **kwargs)

def foo(a:Union[float, int], b:Union[float, int]):
  '''The function to pass'''
  print(a+b)
looper(foo, 3, 2, b=4)