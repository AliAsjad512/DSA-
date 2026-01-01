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