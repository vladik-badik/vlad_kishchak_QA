# my_list = [2, 4, 6, 2, 1, 1, 9, 4, 6]
# my_min = 3
# my_max = 6
# my_sum, my_prod = sum_and_product(my_list, my_min, my_max)
# print(f"The sum of elements between {my_min} and {my_max} is {my_sum}")
# print(f"The product of elements between {my_min} and {my_max} is {my_prod}")

my_list = [2, 4, 6, 2, 1, 1, 9, 4, 6]
my_min = 2
my_max = 9

sum_result = 0
mul_result = 1
found = False

for num in my_list:
    if my_min <= num <= my_max:
        found = True
        sum_result += num
        mul_result *= num

if found:
    print("sum = ", sum_result)
    print("mul = ", mul_result)
else:
    print("No elements found between", my_min, "and", my_max)
    print("sum = 0")
    print("mul = 0")