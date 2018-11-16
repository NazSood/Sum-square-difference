
number = 1
result = 0
result2 = 0

for i in range (1, 101):
  result += number * number
  result2 += number
  number += 1 
  #print("Result: {:d} & number: {:d}" .format(result, number))

print("Result: {:d}" .format(result))
print("Square of sum {:d}" .format((result2 * result2)))
print("difference: {:d}" .format((result2 * result2) - result))
