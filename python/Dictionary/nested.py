capitals = {
    'France': 'Paris',
    'Germany': 'Berlin',
    'Italy': 'Rome'
}

# Nested List in Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Marseille"],
#     "Germany": ["Berlin", "Hamburg", "Munich"],
#     "Italy": ["Rome", "Milan", "Naples"]
# }

# for country, cities in travel_log.items():
    
#     for city in cities:
#       if city == "Lille":
#        print(city)

#print(travel_log["France"][1])
    
nested_list = ["A", "B", ["C","D"]]
print(nested_list[2][1])


travel_log = {
  "France":{
    "num_times_visited": 12,
    "cities_visited": ["Paris", "Lille", "Marseille"]
  },
  "Germany":{
    "num_times_visited": 5,
    "cities_visited": ["Berlin", "Hamburg", "Munich"]
  },
  "Italy":{
    "num_times_visited": 3,
    "cities_visited": ["Rome", "Milan", "Naples"]
  }
}

print(travel_log["Germany"]["cities_visited"][2])