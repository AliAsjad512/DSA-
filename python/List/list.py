xs = [3,1,2]
print(xs,xs[2])
print(xs[-1])

xs[2] = 'foo' # Lists can contain elements of different types 

xs.append('bar') # Add new element to the end of the list 
print(xs)
x=xs.pop() # Remove and retun the last element of the list 
