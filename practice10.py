# Write a program that:

# Creates pos_inf = float("inf") and nan_val = float("nan")
# Print both values
# Check and print if pos_inf is infinite using math.isinf()
# Check and print if nan_val is nan using math.isnan()
# Try adding 500 to both and print the results

pos_inf = float("inf")
nan_val = float("nan")
print(pos_inf,nan_val)
import math as m
print(m.isfinite(pos_inf))