animals = ['cat','dog','moneky','monkey']
for animal in animals:
    print(animal)

    for i in range(0,5,2):
        print("I am in iteration",i)


    
    animal =['elephant','tiger','lion','giraffe']
    for idx, animal in enumerate(animal):
        
        print('#{}: {}' .format(idx+1, "Animal:", animal))