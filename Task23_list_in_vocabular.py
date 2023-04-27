lst = [1,2,3,4,5,6,7,8]
def to_dict(lst):
    result = {}
    for i in range(0, len(lst), 2):
        result[lst[i]] = lst[i+1]
    return result
print(to_dict(lst))

