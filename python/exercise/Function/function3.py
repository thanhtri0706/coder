
def calc_hypo(a = 0, b = 0):
  if type(a) not in (int, float) \
     or type(b) not in (int, float):
    print('Bad argument')
    return False
  
  if a <= 0 or b <= 0:
    print("Bad argument")
    return False

  hypo = (a * a + b * b) ** 0.5
  return hypo


print(calc_hypo(0, 5))
print(calc_hypo('hi', 'bye'))
print(calc_hypo(3,4))