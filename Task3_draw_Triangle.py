height = int(input("enter triagle side: "))
for i in range(height):
    print(" " * (height - i - 1), end="")
    print("*" * (i + 1))