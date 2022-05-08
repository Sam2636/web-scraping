#print(format(round(0.45689072435423, ".4f")))
s="+",0.0456
print(type(s))

import functools
  
""" # initialize tuple
test_tuple = (1, 4, 5)
  
# printing original tuple 
print("The original tuple : " + str(s))
  
# Convert Tuple to integer
# Using reduce() + lambda
res = functools.reduce(lambda sub, ele: sub * 10 + ele,s)
  
# printing result
print("Tuple to integer conversion : " + str(res)) """
  
# Convert Tuple to integer
# Using int() + join() + map()
res = int(''.join(map(str, s)))

# printing result
print("Tuple to integer conversion : " + str(res))

