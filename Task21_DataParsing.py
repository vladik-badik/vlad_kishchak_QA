import json

users = []

with open('users.txt', 'r') as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        fields = [field.strip() for field in line.split(';')]
        name = fields[0]
        age = None
        if len(fields) > 1 and fields[1]:
            try:
                age = int(fields[1])
            except ValueError:
                pass
        phones = []
        if len(fields) > 2 and fields[2]:
            phones = [phone.strip() for phone in fields[2].split(',')]
        users.append({'name': name, 'age': age, 'phones': phones})

with open('/Users/vladkishchak/Vlados_Qa_automation/users_out.json', 'w') as f:
    json.dump(users, f)

with open('/Users/vladkishchak/Vlados_Qa_automation/users_out.txt', 'w') as f:
    for user in users:
        age_str = str(user['age']) if user['age'] is not None else ''
        phones_str = ','.join(user['phones']) if user['phones'] else ''
        f.write(f"{user['name']};{age_str};{phones_str}\n")