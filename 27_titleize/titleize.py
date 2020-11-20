def titleize(phrase):
    """Return phrase in title case (each word capitalized).

        >>> titleize('this is awesome')
        'This Is Awesome'

        >>> titleize('oNLy cAPITALIZe fIRSt')
        'Only Capitalize First'
    """

    split_phrase = phrase.split(' ')
    res = [word.capitalize() for word in split_phrase]
    attach = ' '.join(res)
    return attach
        