#####Iterators
# lst =[1,2,3]
# for i in lst:
#     print(i)

lst = [1, 2, 3]
lst_iter = iter(lst)
# print(type(lst_iter))
print(next(lst_iter))
print(next(lst_iter))
print(next(lst_iter))
# print(next(lst_iter