"""jumbler:  List dictionary words that match an anagram.
2023-09-28 by Owen Ferguson

Credits: 

"""

# DICT = 'shortdict.txt' # Short version for testing and debugging
DICT = 'dict.txt'      # Full dictionary word list

dict_file = open(DICT, 'r')

def find(anagram: str):
    '''Print words in DICT that match anagram.
  
    >>> find("AgEmo")
    omega
  
    >>> find("nosuchword")

    >>> find("alpha")
    alpha

    >>> find("KAWEA")
    awake
  
    '''
    anagram_normal = normalize(anagram)
    for line in dict_file:
        word = line.strip()
        if normalize(word) == anagram_normal:
            print(word)

def normalize(word: str) -> list[str]:
    '''Returns a list of characters that is canonical for anagrams.

    >>> normalize('gamma') == normalize('magam')
    True

    >>> normalize('MAGAM') == normalize('gamma')
    True

    >>> normalize('KAWEA') == normalize('awake')
    True

    >>> normalize('KAWEA') == normalize('gamma')
    False
    '''
    normalized = word.lower()
    result = sorted(normalized)
    return result

def main():
    anagram = input('Anagram to find> ')
    find(anagram)
    
if __name__ == '__main__':
    main()
    # import doctest
    # doctest.testmod()
    # print('Doctests complete!')