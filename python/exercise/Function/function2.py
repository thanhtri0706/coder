
# calculate hypotenuse of a right-angled triangle
import math

def calc_hypo(a = 0, b = 0):
  hypo = math.sqrt(a*a + b*b)
  return hypo

print(calc_hypo(3,4))
