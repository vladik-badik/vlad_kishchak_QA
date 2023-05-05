min_width = int(input("Enter the minimum width: "))
max_width = int(input("Enter the maximum width: "))

if min_width > max_width:
    print("Minimum width cannot be greater than maximum width.")
    exit()

if (max_width - min_width) % 2 != 0:
    print("The difference between maximum and minimum width should be an even number.")
    exit()

for i in range(min_width, max_width + 1, 2):
    print(" " * ((max_width - i) // 2), end="")
    print("*" * i)
for i in range(max_width - 2, min_width - 1, -2):
    print(" " * ((max_width - i) // 2), end="")
    print("*" * i)