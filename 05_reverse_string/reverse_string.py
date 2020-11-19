def reverse_string(phrase):
    """Reverse string,

        >>> reverse_string('awesome')
        'emosewa'

        >>> reverse_string('sauce')
        'ecuas'
    """

    arr = list(phrase)
    arr.reverse()
    return ''.join(arr)
    
