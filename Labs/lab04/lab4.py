def hello(firstname: str): 
    '''Prints greeting to person's name (arg)''' 
    print(f'Hello, {firstname}!') 
    return None 

def ciao(firstname: str): 
    '''Prints goodbye to person's name (arg)''' 
    print(f'Ciao, {firstname}!') 
    return None

def greeting(f, s: str):
    '''Calls function using given string and prints what function is being called'''
    print(f'Calling {f.__name__}:')
    f(s)
    return None
