import doctest

def as_triangle(length: int):
    '''
    A non-fruitful recursive function that prints inverted triangles compose of sucessively shorter lines of *
    '''
    # base case (if length <=0, nothing happens)
    if length > 0:
        print('*' * length)
        as_triangle(length - 1) # recursive call

def bowtie(length: int):
    '''
    Draws bowtie pattern of * given param length'''
    # base case (if length <= 0), nothing happens)
    if length > 0:
        print('*' * length)
        bowtie(length - 1)
        if length > 1:
            print('*' * length)

#bowtie(3)

def check_vowel(letter: str)-> int:
    """
    Returns 1 if given letter is a vowel, 0 otherwise
    """
    if letter.upper() in ['A', 'E', 'I', 'O', 'U']:
        return 1
    return 0

def count_vowels(string: str) -> int:
    """
    Returns count of vowels in the given string

    >>> count_vowels('abc de')
    2
    >>> count_vowels('Hi Everyone!')
    5
    """
    count = 0

    if len(string) > 0:
        count = check_vowel(string[0])
        count += count_vowels(string[1:])
    
    return count