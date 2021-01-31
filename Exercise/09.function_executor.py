def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


def divisible_num(num1, num2):
    return num1 // num2


def func_executor(*args):
    result = []
    for el in args:
        func = el[0]
        data = el[1]
        current_result = func(*data)
        result.append(current_result)
    return result


print(func_executor((sum_numbers, (1, 2)), (multiply_numbers, (2, 4)), (divisible_num, (6, 3))))
