def find_longest_string(file):
    longest_string = ''
    with open(file, 'r') as file:
        current_string = ''
        while True:
            char = file.read(1)
            if not char:
                if len(current_string) > len(longest_string):
                    longest_string = current_string
                break
            current_string += char
            if char == '\n':
                if len(current_string) > len(longest_string):
                    longest_string = current_string
                current_string = ''
    return longest_string.strip()


file= '/Users/vladkishchak/Vlados_Qa_automation/file.txt'
longest_string = find_longest_string(file)
print(f'The longest line is: {longest_string}')