'''

hopper, kay, liskov, perlis and ritchie
live on different floors of a five-floor
building. 

Hopper does not live on the top floor.
kay does not live on the bottom floor.
liskov does not live on either the top floor or the bottom floor.
perlis lives on a higher floor than does kay.
ritchie does not live on a floor adjacent to liskov's
liskov does not live on a floor adjacent to kay's

where does everyone live???

'''

import itertools


def floor_puzzle():
    orderings = itertools.permutations([1,2,3,4,5])
    
    return next((hopper, kay, liskov, perlis, ritchie)
                for (hopper, kay, liskov, perlis, ritchie) in orderings
                if hopper != 5
                if kay != 1
                if not(liskov == 5 or liskov == 1)
                if abs(liskov - kay) != 1
                if perlis > kay
                if abs(ritchie - liskov) != 1
                )


def floor_puzzle2():
    orderings = itertools.permutations([1,2,3,4,5])
    
    for (hopper, kay, liskov, perlis, ritchie) in orderings:
        if (hopper != 5
        and kay != 1
        and not(liskov == 5 or liskov == 1)
        and abs(liskov - kay) != 1
        and perlis > kay
        and abs(ritchie - liskov) != 1):
            
            yield (hopper, kay, liskov, perlis, ritchie)


if __name__ == '__main__':
    sol = floor_puzzle()
    sol2 = floor_puzzle2()