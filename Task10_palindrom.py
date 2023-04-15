user_input = input("Enter text: ")
user_input = user_input.strip().lower()
is_palindrome = user_input == user_input[::-1]

print(is_palindrome)


user_input = input("Enter text: ")
user_input = user_input.strip().lower()

for i in range(len(user_input) // 2):
    if user_input[i] != user_input[-i-1]:
        print(False)
        break
else:
    print(True)