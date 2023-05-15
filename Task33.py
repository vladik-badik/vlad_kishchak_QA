def custom_zip(*sequences, full=False, default=None):

    if full:
        max_length = max(len(seq) for seq in sequences)
        result = []
        for i in range(max_length):
            tuple_i = []
            for seq in sequences:
                if i < len(seq):
                    tuple_i.append(seq[i])
                else:
                    tuple_i.append(default)
            result.append(tuple(tuple_i))
    else:
        result = list(zip(*sequences))
    return result


seq1= [1, 2, 3, 4]
seq2 = ['a', 'b', 'c', 'd']
seq3 = [True, False, True]
print(custom_zip(seq1, seq2, seq3))
print(custom_zip(seq1, seq2, seq3, full=True, default='Q'))