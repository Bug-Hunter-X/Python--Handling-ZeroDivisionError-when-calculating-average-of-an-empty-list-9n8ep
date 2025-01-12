def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

# Example usage with an empty list
average = calculate_average([])
print(f"The average is: {average}")

# Example usage with a list of numbers
numberList = [10,20,30,40,50]
average = calculate_average(numberList)
print(f"The average is: {average}")
