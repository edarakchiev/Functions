def negative_numbers(numbers):
    return [n for n in numbers if n < 0]


def positive_numbers(numbers):
    return [num for num in numbers if num >= 0]


def print_negative_bigger():
    print("The negatives are stronger than the positives")


def print_positive_bigger():
    print("The positives are stronger than the negatives")


def positive_vs_negative(pos_num, neg_num):
    if pos_num >= abs(neg_num):
        return True
    return False


nums = [int(el) for el in input().split()]
negative_num = sum(negative_numbers(nums))
positive_num = sum(positive_numbers(nums))

print(f"{negative_num}")
print(f"{positive_num}")
if positive_vs_negative(positive_num, negative_num):
    print_positive_bigger()
else:
    print_negative_bigger()