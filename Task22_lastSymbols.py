def read_last(file_path, symbol_number):
    with open('strings.txt', 'r') as f:
        for line in f:
            line = line.rstrip('\n')
            if line:
                print(line[-symbol_number:])
read_last('string.txt', 1)