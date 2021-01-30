def round_number(nums):
    return [round(num) for num in nums]


numbers = [float(n) for n in input().split()]
print(round_number(numbers))