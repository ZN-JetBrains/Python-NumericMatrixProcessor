def range_sum(numbers, start, end):
    if not numbers:
        return 0

    sum_ = 0
    for num in numbers:
        if start <= num <= end:
            sum_ += num
    return sum_


input_numbers = [int(x) for x in input().split(' ') if x.isdigit()]
a, b = [int(x) for x in input().split(' ')]
print(range_sum(input_numbers, a, b))
