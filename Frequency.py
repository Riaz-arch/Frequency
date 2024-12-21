def count_value_frequency(test_dict, value_to_check):
    frequency = sum(1 for v in test_dict.values() if v == value_to_check)
    return frequency

test_dict = {
    'a': 1,
    'b': 2,
    'c': 1,
    'd': 3,
    'e': 2,
    'f': 1
}

value_to_check = 1
frequency = count_value_frequency(test_dict, value_to_check)

print(f"The frequency of the value {value_to_check} in the dictionary is: {frequency}")