def sum_numbers(string):
    numbers = string.split(',')
    total_sum = sum([int(num) for num in numbers])
    return total_sum