example_string_1 = '12 23 23 54 45 67 32'

int_list_1 = list(map(int,example_string_1.split()))
print(f" The list 1 is : {int_list_1}")


example_string_2 = '12,23,4323,2452,23,42,234234,1234,1'

int_list_2 = list(map(int,example_string_2.split(',')))
print(f" The list 2 is : {int_list_2}")


int_list = map(int,example_string_1.split())
print(f" The MAP list : {int_list}")