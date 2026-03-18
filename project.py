# Wrong calculation logic
def average(numbers):
    return sum(numbers) / len(numbers) - 1  # Bug: subtracting 1 unnecessarily

     print(average([10, 20, 30]))
