def two_list_dictionary(keys, values):
    """Given keys and values, make dictionary of those.
    
        >>> two_list_dictionary(['x', 'y', 'z'], [9, 8, 7])
        {'x': 9, 'y': 8, 'z': 7}
        
    If there are fewer values than keys, remaining keys should have value
    of None:
    
        >>> two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3])
        {'a': 1, 'b': 2, 'c': 3, 'd': None}
    
    If there are fewer keys, ignore remaining values:

        >>> two_list_dictionary(['a', 'b', 'c'], [1, 2, 3, 4])
        {'a': 1, 'b': 2, 'c': 3}
   """
    key_len = len(keys)
    val_len = len(values)

    if key_len == val_len:
        res = {keys[idx]: values[idx] for idx in range(0, key_len)}
            
    elif val_len < key_len:
        res = {keys[i]: values[i] for i in range(0, val_len)}
        for j in range(val_len, key_len):
            res[keys[j]] = None

    else:
        res = {keys[i]: values[i] for i in range(0, key_len)}

    return res
