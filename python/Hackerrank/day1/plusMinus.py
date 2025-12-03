def plusMinus(arr):
    n = len(arr)
    pos = sum(1 for x in arr if x > 0)
    neg = sum(1 for x in arr if x < 0)
    zer = sum(1 for x in arr if x == 0)
    
    print(f"{pos/n:.6f}")
    print(f"{neg/n:.6f}")
    print(f"{zer/n:.6f}")

plusMinus([-4, 3, -9, 0, 4, 1])
