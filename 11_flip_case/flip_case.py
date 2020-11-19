def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    res = []
    for ltr in phrase:
        if (ltr == to_swap.upper()) or (ltr == to_swap.lower()):
            cur = ltr.swapcase()
            res.append(cur)
        else:
            res.append(ltr)
    final = ''.join(res)
    return final
