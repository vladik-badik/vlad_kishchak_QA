height = int(input("Enter height: "))
width = int(input("Enter width: "))
symbol = input("Enter symbol: ")

for i in range(height):
    for j in range(width):
        print(symbol, end="")
    print()