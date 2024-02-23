'''lecture 2'''

li = [1,2,3,4,5,6,7,8,9,10]

def evens(x: list):
    '''given a list of int, returns list of even numbers in original list'''
    result = [] # initialize empty list
    for elem in x:
        if elem % 2 == 0: # checks if int is even using modulus
            result.append(elem) # adds even int to list
    return result # returns new list with even numbers

print(evens(li))