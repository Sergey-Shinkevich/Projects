import time
from multiprocessing import Pool


def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as file:
        while file.readline() != '':
            readline_1 = file.readline()
            all_data.append(readline_1)


filenames = [f'./file {number}.txt' for number in range(1, 5)]

# Линейный вызов
start_time = time.time()
for file in filenames:
    read_info(file)
end_time = time.time()
execution_time = round((end_time - start_time), 2)
print(f'Время чтения файлов: {execution_time} секунд (Линейный)')

# Многопроцессный
if __name__ == '__main__':
    start_time = time.time()
    with Pool(processes=4) as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    execution_time = round((end_time - start_time), 2)
    print(f'Время чтения файлов: {execution_time} секунд (Многопроцессный)')