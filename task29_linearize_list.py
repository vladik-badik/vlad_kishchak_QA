lst = [1, 2, [3, 4, [5, 6], 7], 8, [9, [10]], 11]
def linearize_list(lst):
    result = []
    for element in lst:
        if isinstance(element, list):
            result.extend(linearize_list(element))
        else:
            result.append(element)
    return result

print(linearize_list(lst))