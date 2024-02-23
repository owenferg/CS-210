def power_check(n):
    if n == 1:
        return True
    elif n % 2 != 0:
        return False
    elif n == 0:
        return False
    else:
        return power_check(n/2)
    
