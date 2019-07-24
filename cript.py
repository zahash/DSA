import itertools
import re

def substitute(equation, mapping): # substitutes each unique character with a number
    for char, num in mapping:
        equation = equation.replace(char, str(num))
    
    return equation

def validate(numeric_equation): # evaluates and validates the numeric_equation
    numbers_starting_with_zero = re.findall(r"\b0\d", numeric_equation)
    
    if len(numbers_starting_with_zero) == 0 and eval(numeric_equation) is True:
        return True
    else:
        return False

def cript(equation): # the main function
    chars = list(set(c for c in equation if c.isalpha()))
    orderings = itertools.permutations(range(10), len(chars))
    
    for order in orderings:
        mapping = zip(chars, order)
        numeric_equation = substitute(equation, mapping)
        
        if validate(numeric_equation):
            return numeric_equation
    
    return None


def test():
    equation1 = 'odd + odd == even'
    equation2 = 'fire + water == steam'
    equation3 = 'USA + USSR == PEACE'
    
    mapping1 = [('d', 5),('e', 1),('n', 0),('o', 2),('v', 9)]
    mapping2 = [('f', 1),('i', 2),('r', 3),('e', 4),('w', 5),
                ('a', 6),('t', 7),('s', 8),('m', 9)]
    
    numeric_equation1 = '234 + 5643 == 87984'
    numeric_equation2 = '1234 + 0543 == 7469'
    numeric_equation3 = '932 + 9338 == 10270'
    numeric_equation4 = '655 + 655 == 1310'
    
    assert substitute(equation1, mapping1) == '255 + 255 == 1910'
    assert substitute(equation2, mapping2) == '1234 + 56743 == 87469'
    assert substitute(equation1, mapping1) != '155 + 155 == 2920'
    
    assert validate(numeric_equation1) is False
    assert validate(numeric_equation2) is False
    assert validate(numeric_equation3) is True
    
    assert cript(equation1) == numeric_equation4
    assert cript(equation3) == numeric_equation3
    
    
    print("All tests Done")
    


if __name__ == '__main__':
    test()
    
    equation = 'USA + USSR == PEACE'
    print(cript(equation))
    
    