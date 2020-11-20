def repeat(phrase, num):
    """Return phrase, repeated num times.

        >>> repeat('*', 3)
        '***'

        >>> repeat('abc', 2)
        'abcabc'

        >>> repeat('abc', 0)
        ''

    Ignore illegal values of num and return None:

        >>> repeat('abc', -1) is None
        True

        >>> repeat('abc', 'nope') is None
        True
    """
    res = []
    if num == 0:
        return ''
    if (isinstance(num, int) == False) or (num < 0):
        return None
    for el in range(0, num):
        res.append(phrase)
        final = ''.join(res)
    return final
