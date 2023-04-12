# to store total rainfall
total_rainfall_per_year = []

# Ask number of year
num_years = int(input("Enter the number of years: "))

# Loop each year
for year in range(1, num_years+1):
    # Define a list to store the monthly rainfall for this year
    monthly_rainfall = []
    
    # Loop each month
    for month in range(1, 13):
        rainfall = float(input(f"Enter the rainfall amount for Year {year}, Month {month} (in centimeters): "))
        monthly_rainfall.append(rainfall)
    
    # Calculate the total rainfall for this year
    total_rainfall = sum(monthly_rainfall)
    total_rainfall_per_year.append(total_rainfall)
    
    # Calculate the average monthly rainfall for this year
    avg_monthly_rainfall = total_rainfall / 12
    
    # Print the total and average rainfall for this year
    print(f"Year {year}: Total rainfall = {total_rainfall} cm, Average monthly rainfall = {avg_monthly_rainfall} cm")

# Calculate the overall average monthly rainfall
overall_avg_monthly_rainfall = sum(total_rainfall_per_year) / (num_years * 12)
print(f"\nOverall average monthly rainfall = {overall_avg_monthly_rainfall} cm")
