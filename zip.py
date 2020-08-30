number_list = [1, 2, 3]
str_list = ['one', 'two', 'three']
 
result = list(zip(number_list, str_list))
print(result)
 
for first_value, second_value in result:
    print(first_value, " - ", second_value)