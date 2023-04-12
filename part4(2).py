def print_list(numbers):
    """
    Function to print all the elements in a list horizontally
    """
    print(" ".join(str(num) for num in numbers))

def print_greater_than(numbers, threshold):
    """
    Function to print all the elements in a list that are greater than a given threshold
    """
    greater_numbers = [num for num in numbers if num > threshold]
    print(f"The numbers greater than {threshold} are:")
    print_list(greater_numbers)

myNumbers = [4, 8, 12, 8, 33, 11, 5, 10, 20, 3]

print("All the numbers in the list:")
print_list(myNumbers)

print()
print_greater_than(myNumbers, 12)


