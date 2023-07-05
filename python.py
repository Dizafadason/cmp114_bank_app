def calculate_sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

# Example usage
my_list = [1, 2, 3, 4, 5]
result = calculate_sum(my_list)
print("Sum:", result)
