def sum_multiplied(nums, multiplier):
    return sum(nums) * multiplier


def odd_numbers(nums):
    return [num for num in nums if num % 2 == 1]


def even_numbers(nums):
    return [num for num in nums if num % 2 == 0]


command = input()
numbers = [int(n) for n in input().split()]
m = len(numbers)
result = None
if command == "Odd":
    result = sum_multiplied(odd_numbers(numbers), m)
elif command == "Even":
    result = sum_multiplied(even_numbers(numbers), m)
print(result)