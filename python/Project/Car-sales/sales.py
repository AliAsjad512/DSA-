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