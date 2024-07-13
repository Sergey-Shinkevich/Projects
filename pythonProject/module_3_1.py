

def count_calls():
    global calls
    calls = calls + 1
    return calls


def string_info(string):
    str_info = len(string), string.upper(), string.lower()
    count_calls()
    return str_info


def is_contains(string, list_to_search):
    result = False
    count_calls()
    for i in range(len(list_to_search)):
        if string.lower() == list_to_search[i].lower():
            result = True
    return result


calls = 0
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))
print(is_contains('cycle', ['recycling', 'cyclic']))
print(calls)
