lst =  [10, 15, 21, 25, 30, 33, 35, 45, 50, 51, 55, 60]
list_3_not_5 = []
list_5_not_3 = []
list_3_and_5 = []
for num in lst:
    if num % 3 == 0 and num % 5 == 0:
        list_3_and_5.append(num)
    elif num % 3 == 0:
        list_3_not_5.append(num)
    elif num % 5 == 0:
        list_5_not_3.append(num)

print("Numbers that can be devided by 3 but not by 5:", list_3_not_5)
print("Numbers that can be devidede by 5 but not by 3:", list_5_not_3)
print("Numbers that can be devided by both 3 and 5:", list_3_and_5)