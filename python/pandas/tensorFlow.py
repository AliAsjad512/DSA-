import pandas as pd
series = pd.Series(["BMW", "Toyota", "Honda"])
print(series)

colors= pd.Series(["Red","Blue", "White"])
print(colors)

# Series is one dimensional 
# DataFrame is two dimensiona
car_data = pd.DataFrame({"Car make": series, "colors":colors})
print(car_data)

car_sales=pd.read_csv("car-sales.csv")
print(car_sales)
print(car_sales.dtypes)
print(car_sales.columns)
car_sales.index
car_sales.describe()
car_sales.info()
