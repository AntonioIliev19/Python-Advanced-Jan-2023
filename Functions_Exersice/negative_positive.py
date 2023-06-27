def print_nums(positive, negative):
    print(negative)
    print(positive)

    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = [int(x) for x in input().split()]
positive_nums = sum(x for x in numbers if x > 0)
negative_nums = sum(x for x in numbers if x < 0)

print_nums(positive_nums, negative_nums)
