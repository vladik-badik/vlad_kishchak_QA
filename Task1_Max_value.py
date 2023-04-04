val1 = int(input("Enter first value: "))
val2 = int(input("Enter second value: "))
val3 = int(input("Enter third value: "))

max_val = val1

if val2 > max_val:
    max_val = val2

if val3 > max_val:
    max_val = val3

print("Max value is : ", max_val)

