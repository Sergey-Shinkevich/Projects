count = 0


def calculate_float_int(member):
    global count
    count = count + member


def calculate_str(member):
    global count
    count = count + len(member)


def calculate_list(member):
    calculate_check(member)


def calculate_dict(member):
    dict1 = list(member.values())
    calculate_list(dict1)
    dict2 = list(member.keys())
    calculate_list(dict2)


def calculate_tuple(member):
    tuple1 = list(member)
    calculate_list(tuple1)


def calculate_set(member):
    set1 = list(member)
    calculate_list(set1)


def calculate_structure_sum(data_str):
    global count
    calculate_check(data_str)
    return count


def calculate_check(member):
    i = 0
    while i <= (len(member) - 1):
        if (isinstance(member[i], float)) or (isinstance(member[i], int)):
            calculate_float_int(member[i])
        if isinstance(member[i], str):
            calculate_str(member[i])
        if isinstance(member[i], list):
            calculate_list(member[i])
        if isinstance(member[i], tuple):
            calculate_tuple(member[i])
        if isinstance(member[i], dict):
            calculate_dict(member[i])
        if isinstance(member[i], set):
            calculate_set(member[i])
        i = i + 1


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
