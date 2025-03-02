import numpy as np

prices = np.array([100, 200, 300])
increase = np.array([10, 20, 30])

new_prices = prices + increase  # Element-wise addition
print(new_prices)

sales = np.array([23.4567, 67.89123, 12.34567])
rounded_sales = np.round(sales, 2)
print(rounded_sales)

#  ufunc Logs
values = np.array([10, 100, 1000])
log_values = np.log10(values)
print(log_values)

#  ufunc Summations
calories = np.array([2200, 2500, 1800, 2000, 2300, 2600, 2100])
total_calories = np.sum(calories)
print(total_calories) 

# ufunc Products
growth_rates = np.array([1.05, 1.07, 1.03])  
total_growth = np.prod(growth_rates)
print(total_growth) 

# ufunc Differences
temperatures = np.array([30, 32, 31, 29, 35])
temperature_change = np.diff(temperatures)
print(temperature_change)

# lcm
times = np.array([4, 6, 8]) 
lcm = np.lcm.reduce(times)
print(lcm)

#gcd
times = np.array([48, 72, 96])
gcd = np.gcd.reduce(times)
print(gcd) 

