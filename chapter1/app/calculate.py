class Calculate(object):
    def add(self, x, y):
        """Takes two integers and adds them together
        to produce the result.
        >>> c = Calculate()
        >>> c.add(1,1)
        3
        >>> c.add(25, 125)
        150
        
        >>> c.add(1.0, 1.0)
        Traceback (most recent call last):
        ...
        TypeError: Invalid type: <class 'float'> and <class 'float'>
        """
        if type(x) == int and type(y) == int:
            return x + y
        else:
            raise TypeError(f"Invalid type: {type(x)} and {type(y)}")


if __name__ == '__main__': #pragma: no cover
    import doctest
    doctest.testmod(extraglobs={'c': Calculate()})