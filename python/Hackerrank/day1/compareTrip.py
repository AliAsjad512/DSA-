def compareTriplets(a, b):
    alice = 0
    bob = 0
    
    for x, y in zip(a, b):
        if x > y:
            alice += 1
        elif y > x:
            bob += 1
    return [alice, bob]

print(compareTriplets([5, 6, 7], [3, 6, 10]))
