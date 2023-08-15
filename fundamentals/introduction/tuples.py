# tuple = 1,2,3,4,5
# tuple_2 = 5, 6
# print( tuple + tuple_2)


def calc_sum_and_diff(a,b):
    sum = a + b
    diff = a - b
    result = (sum, diff)
    print(f'the value of sum is {result[0]} ')
    print(f'the value of difference {result[1]}')

    return result

print(calc_sum_and_diff(34,23))

person = {'name':'Nd','age': 26,'hobbies': ['coding','hanging out','praying', 'dancing']}


# person.pop('hobbies')
print(person['hobbies'])


def print_hello_ten_times(x =10):
    for num in range(x):
        print('Hello')

print_hello_ten_times()
print_hello_ten_times(4)