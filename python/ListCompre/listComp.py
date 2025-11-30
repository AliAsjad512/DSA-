nums = [0,1,2,3,4]
squares=[]
for x in nums:
    squares.append(x**2)
    print(squares)

    num =[0,1,2,3,4]
    squares=[x**2 for x in num]
    print(squares)

    #Even Squares

    even_squares=[x**2 for x in num if x%2==0]
    print(even_squares)

