def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """
    lowercase = phrase.lower().replace(' ', '')
    lowercase_lst = list(lowercase)

    reverse = list(lowercase)
    reverse.reverse()
    
    for idx in range(len(lowercase_lst)):
        if lowercase[idx] != reverse[idx]:
            return False
        else:
            return True

