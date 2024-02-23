# Pizza calculator example code  -- pizza_calculator.py
import math 
import doctest

def pizza_calculator(diameter, cost): 
    ''' 
    (int, num) -> float 

    Calculates and returns the cost per square inch 
    of pizza for a pizza of given diameter and cost. 
    Examples: 

    >>> pizza_calculator(14, 18) 
    0.117
    >>> pizza_calculator(14, 20.25)  
    0.132
    ''' 

    area = circle_area(diameter)

    cost_per_inch = cost / area 
    cost_per_inch = round(cost_per_inch, 3) 
    return cost_per_inch

def circle_area(diameter):
    '''
    (int) -> float
    
    Calculates and returns the area of a circle given a diameter.
    Examples:
    
    >>> circle_area(5)
    19.634954084936208
    >>> circle_area(20)
    314.1592653589793
    '''

    return math.pi * (diameter / 2)**2 # pi * r**2 

print(doctest.testmod())