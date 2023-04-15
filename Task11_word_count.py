##### рахуємо слова в реченнях яке вводить користувач
# user_sentence = input("Enter text:")
# sentences = user_sentence.split(".")
#### або ми можем рахувати вже слова в дефолтному реченні
multi_string = "Hello my name is Giovany Georgio. But everybody calls me Georgio."
sentences = multi_string.split(".")
print("multi_string =" , multi_string)
word_counts = []
for sentence in sentences:
    words = sentence.strip().split(" ")
    if len(words) > 1:
        word_count = len([word for word in words if word])
        word_counts.append(word_count)

print("words_number -> ",word_counts)
