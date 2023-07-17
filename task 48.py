import os
import random
import string
import concurrent.futures
import time

def file_generator(directory, number_of_files, size):
    os.makedirs(directory, exist_ok=True)
    for i in range(number_of_files):
        file_name = os.path.join(directory, f"file_{i}.txt")
        content_size = random.randint(size // 2, size)
        content = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=content_size))
        with open(file_name, 'w') as file:
            file.write(content)


def letter_counter_in_one_thread(directory, letter_to_find):
    count = 0
    for file_name in os.listdir(directory):
        file_path = os.path.join(directory, file_name)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                count += content.count(letter_to_find)
    return count



def count_letter_in_file(file_path, letter_to_find):
    with open(file_path, 'r') as file:
        content = file.read()
        return content.count(letter_to_find)

def letter_counter_in_n_threads(directory, letter_to_find, number_of_threads):
    count = 0
    files = [os.path.join(directory, file_name) for file_name in os.listdir(directory)]
    with concurrent.futures.ThreadPoolExecutor(max_workers=number_of_threads) as executor:
        results = executor.map(lambda file: count_letter_in_file(file, letter_to_find), files)
        count = sum(results)
    return count



directory = 'files'
number_of_files = 200
size = 1000000
letter_to_find = 'a'
number_of_threads = 4
start_time = time.time()
file_generator(directory, number_of_files, size)
end_time = time.time()
file_generation_time = end_time - start_time
start_time = time.time()
count_one_thread = letter_counter_in_one_thread(directory, letter_to_find)
end_time = time.time()
one_thread_time = end_time - start_time
start_time = time.time()
count_multiple_threads = letter_counter_in_n_threads(directory, letter_to_find, number_of_threads)
end_time = time.time()
multiple_threads_time = end_time - start_time


print(f"Files generated in: {file_generation_time} seconds")
print(f"Count of '{letter_to_find}' in one thread: {count_one_thread}, Time: {one_thread_time} seconds")
print(f"Count of '{letter_to_find}' in {number_of_threads} threads: {count_multiple_threads}, Time: {multiple_threads_time} seconds")
