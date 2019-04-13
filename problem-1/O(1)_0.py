# Returns the sum of all multipliers of x for numbers from 1 to end.
def sumOfMultipliers(end, x):
  n = end / x
  return (n * (n + 1) / 2) * x

end = 999 # below 1000
x = 3
y = 5
# We have to subtract one sum of the multipliers of x * y because these multipliers take part in both of the sums of the multipliers of x and y and hence contribute twice in the final sum.
sum = sumOfMultipliers(end, x) + sumOfMultipliers(end, y) - sumOfMultipliers(end, x * y)

print(sum)
