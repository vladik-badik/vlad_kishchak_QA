s = "aab qq c badcc a qqqqqaqqqqaa tpara"

lst= s.split()  # розділяю срічку на слова

result = []  # створюю пустий список куди буду додавати слова з двома буквами А

for word in lst:
    if word.count('a') == 2:
        result.append(word.capitalize())  # Додати слово в список і зробити першу букву Великою

header = " ".join(result)  # обєднати слова в заголовок


print("Header:", header)
print("String:", s)