pro_dictionary = {
    "name": "Laptop",
    "price": 1200,
    "specs": {
        "processor": "Intel i7",
        "ram": "16GB",
        "storage": "512GB SSD"
    }
}

#print(pro_dictionary["specs"]["ram"])
for key in pro_dictionary:
    print(key, ":", pro_dictionary[key])