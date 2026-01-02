import pandas as pd

# Example student data
data = {
    'ID': [101, 102, 103],
    'Name': ['Ali', 'John', 'Maria'],
    'Math': [85, 72, 95],
    'Science': [90, 68, 92],
    'English': [78, 80, 88]
}

df = pd.DataFrame(data)
print('Math score mean',df['Math'].mean())
print('Science score mean',df['Science'].mean())
print('English score mean',df['English'].mean())
print(df)

print('\n\n\ncar sale mean')

car_sales['Price'] = (
    car_sales['Price']
    .astype(str)
    .str.replace('$', '', regex=False)
    .str.replace(',', '', regex=False)
    .str.strip()
)

car_sales['Price'] = pd.to_numeric(car_sales['Price'], errors='coerce')

print(car_sales['Price'].mean())
print(car_sales["Price"].max())
print(car_sales["Price"].min())
car_sales[car_sales["Make"] == "Toyota"]["Price"].max()

pd.crosstab(car_sales["Make"], car_sales["Doors"])

grouped = car_sales.groupby("Make").mean(numeric_only=True)
bmw_data = grouped.loc["BMW"]
print(bmw_data)

white_toyotas = car_sales[(car_sales["Make"] == "Toyota") & (car_sales["Colour"] == "White")]

white_toyotas_mean = white_toyotas.mean(numeric_only=True)
print(white_toyotas_mean)

## Manipultaing data 
car_sales["Make"].str.lower()
car_sales["Make"] = car_sales["Make"].str.lower()
seats_column = pd.Series([5, 5, 5, 5, 5,])
car_sales["Seats"] = seats_column
seats_column = pd.Series([5, 5, 5, 5, 5,])
car_sales["Seats"] = seats_column
car_sales["Seats"].fillna(5, inplace=True)
car_sales
car_sales


fuel_economy = [7.5, 9.2, 5.0, 9.6, 8.7,4.7,7.6,8.7,3.0,7.6]
car_sales["Fuel per 100KM"] = fuel_economy
car_sales

car_sales.sample(frac=1)