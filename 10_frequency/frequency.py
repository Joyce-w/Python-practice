def frequency(lst, search_term):
    """Return frequency of term in lst.
    
        >>> frequency([1, 4, 3, 4, 4], 4)
        3
        
        >>> frequency([1, 4, 3], 7)
        0
    """

    if search_term in lst:
        num = lst.count(search_term)
        return num
    else:
        return 0

