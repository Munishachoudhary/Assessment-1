def sum(numbers):
    total = 0
    for number in numbers:
        total += number
    return total

numbers_list = [1, 2, 3, 4, 5]
result = sum(numbers_list)
print(f"sum is: {result}")