# def operate(operator, *args):
#     if operator == "+":
#         result = 0
#         for n in args:
#             result += n
#         return result
#     elif operator == "-":
#         result = args[0]
#         for n in args[1:]:
#             result -= n
#         return result
#     elif operator == "*":
#         result = 1
#         for n in args:
#             result *= n
#         return result
#     elif operator == "/":
#         result = args[0]
#         for n in args[1:]:
#             result /= n
#         return result

from functools import reduce


def operate(operator, *args):
    return reduce(lambda x, y: eval(f"{x}{operator}{y}"), args)


print(operate("+", 1, 2, 3))
print(operate("*", 3, 4))
print(operate("/", 8, 4, 2))
print(operate("-", 7, 4))

