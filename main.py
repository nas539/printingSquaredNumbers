first_number = 1
second_number = 15
third_number = 20
fourth_number = 35

def printing_a_dictionary_of_squared_numbers(num1, num2):
    first_list = [number for number in range(num1, num2 + 1)]
    squared_list = [number ** 2 for number in range(num1, num2 + 1)]
    new_list = zip(first_list, squared_list)
    return new_list
  

print(dict(printing_a_dictionary_of_squared_numbers(first_number, second_number)))
print(dict(printing_a_dictionary_of_squared_numbers(third_number, fourth_number)))