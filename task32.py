def custom_map(func, *sequences):
    result = []
    min_length = min(len(seq) for seq in sequences)
    for i in range(min_length):
        args = [seq[i] for seq in sequences]
        result.append(func(*args))
    return result

result1 = custom_map(sum, [[1, 2, 3], [4, 5]])
print(result1)
result2 = custom_map(lambda x, y: x + y, [1, 2, 3, 4], (3, 4, 4, 4, 4, 4, 44))
print(result2)