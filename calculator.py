def add(x, y):
  answer = x + y
  return answer

def subtract(x, y):
  answer = x - y
  return answer

def multiply(x, y):
  answer = x * y
  return answer

def divide(x, y):
  if y != 0:
    answer = x/y
  else:
    answer = "CANNOT DIVIDE BY ZERO"
  return answer

def exp(x, y):
    answer = x ** y
    return answer

print(add(3, 5))
print(subtract(10, 4))
print(multiply(2, 6))
print(divide(8, 2))
print(exp(2, 3))