auction={}
maxValue=0;
HigherBider=''
while True:
  name=input("Enter bider name")
  bid=int(input("Enter your bid"))
  num = input("Do we have another bider yes or no: ")
  auction[name] = bid
  # auction['bid'] = bid
        
    # exit the loop if the user enters 0
  if num == 'no':
   break
    
for key, value in auction.items():
     if value>maxValue:
        maxValue=value
        HigherBider=key
print("MaxV : ",maxValue)