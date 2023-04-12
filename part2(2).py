def get_positive_float(prompt):
    """
    Helper function to get a positive float from user input
    """
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Please enter a positive value")
            else:
                return value
        except ValueError:
            print("Please enter a valid number")

def print_daily_data(starting_organisms, avg_daily_increase, num_days):
    """
    Function to print the daily data for a given number of days
    """
    # Print the header
    print(f"{'Day':<10} {'Organisms':<15}")
    
    # Print the starting data for day 1
    print(f"{'01':<10} {int(starting_organisms):<15}")
    
    # Loop through each day and calculate the data
    for day in range(2, num_days+1):
        # Calculate the number of organisms for this day
        organisms = starting_organisms * (1 + avg_daily_increase/100) ** (day-1)
        
        # Print the data for this day
        print(f"{day:02d} {int(organisms):<15}")

# Get user input
starting_organisms = get_positive_float("Enter the starting number of organisms: ")
avg_daily_increase = get_positive_float("Enter the average daily percentage increase: ")
num_days = int(get_positive_float("Enter the number of days' worth of data to print: "))

# Print the daily data
print_daily_data(starting_organisms, avg_daily_increase, num_days)
