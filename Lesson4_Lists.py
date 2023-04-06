# lst = [1,2,3,4, "qwerrt", None, [3,4,5,6,8]]
# print(lst)
#
#
# print(len(lst))

# lst= [1,2,3,4,5,6,7,8,9]
# print(lst[1:6:2])
# print(lst[1::2])
#
# lst_copy = lst[:]
# print(lst)
# print(lst_copy)
# lst[2] = 1221212121
#
# lst=[1,2]
# lst2=lst*3
# print(lst2)

# lst= [None] * 1000
# lst[777]=23
# print(lst)

# lst=[[1,2]] ####Homework
# lst2= lst*3
# print(lst2)
# lst[0].append((555)) ## додає в кінець списку те шо передаємо
# print(lst)
# print(lst2)

######
# lst = ["a", 'b', 'c' , 'd']

# for item in lst:
#     print(item)
# for item in lst:
#     print(lst)

# for item in lst:
#     print(item.upper())

# expected_value = ["a", 'b', 'c' , 'd']
# actual_value = ["a", 'b', 'R' , 'd']
#
# for index, item in enumerate (expected_value):
#     # print(index , item)
#     if actual_value[index] !=item:
#         print(f"Error on {index} comparison")
#####

# lst= [1,2]
# a,b= lst
# print(a)
# print(b)

# lst = [1,2,3,4,5]
# a,b, *c =lst
# print(a)
# print(b)
# print(c)


lst = [1,2,3,4,5]
*a,b,c =lst
print(a)
print(b)
print(c)



