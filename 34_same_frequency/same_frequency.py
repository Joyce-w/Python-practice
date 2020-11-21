def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    num1 = str(num1)
    num2 = str(num2)

    if len(num1) != len(num2):
        return False
    
    else:
        res1 = {num1[digit]:num1.count(num1[digit]) for digit in range(0, len(num1))} 
        res2 = {num2[digit]:num2.count(num1[digit]) for digit in range(0, len(num2))} 

        if set(res1.items()) ^ set(res2.items()):
            return False
        else:
            return True

