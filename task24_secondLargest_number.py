lst=[1,2,3,4,5,7,10,22,45,45.5]
# lst=[3]
def second_largest(lst):
    if len(lst) < 2:
        return None

    largest = second_largest = float('-inf')
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest if second_largest != float('-inf') else None
print(second_largest(lst))