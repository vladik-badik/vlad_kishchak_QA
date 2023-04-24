users = [
    {'name': 'Влад', 'age': 25},
    {'name': 'Саша', 'age': 17},
    {'name': 'Аліна', 'age': 32},
    {'name': 'Іван', 'age': 21}
]
names_over_18 = [user['name'] for user in users if user['age'] >= 18]
print(names_over_18)