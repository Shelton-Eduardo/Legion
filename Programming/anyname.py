# Задание 04

def merged_dics(*args):
    original_dic = dict()
    for dic in args:

        if not isinstance(dic, dict):
            continue
        for key, value in dic.items():
            original_dic[key] = original_dic.get(key, 0) + value
    return original_dic


a = merged_dics({"John": 6, "Shelton": 6, "baka": 6, "Mahad": 6}, {"John": 6, "Hello": 6, "Hi": 6})
print(f"задание 04 \n{a}")


#  задание    12


def extract_unique(nested_list):
    return {item for sublist in nested_list for item in sublist}


example_input = [[1, 2], [2, 3]]
result = extract_unique(example_input)

print(f"задание 12 \n{result}")

#   задание 19
import math

def sort_by_distance(points: list):
    return sorted(points, key=lambda p: math.sqrt(p['x'] ** 2 + p['y'] ** 2))


print(f"задание 19: \n{sort_by_distance([
    {'x': 3, 'y': 4},
    {'x': 1, 'y': 1},
    {'x': 0, 'y': 2},
    {'x': -1, 'y': -1}
])}")


#  задание   26

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True

    if n % 2 == 0 or n % 3 == 0: return False

    for i in range(5, int(math.sqrt(n)) + 1, 6):
        if n % i == 0 or n % (i + 2) == 0: return False
    return True


print(f"задание 26: {is_prime(7)}")


# Задание  3

def filterstrings(str_list, minlen=0):
    return [s for s in str_list if isinstance(s, str) and len(s) >= minlen]


list1 = ['abc', 'de', 'fghij', 'kl', 'mnopqr']
print("задание 03\n")
print(filterstrings(list1, 4))
print(filterstrings(list1, 5))
print(filterstrings(list1, 6))