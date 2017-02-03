# python3
import sys

# input = sys.stdin.read()
# tokens = input.split()
# n = int(tokens[0])

def fibonacci_sum_last_digit(n):
  for i in range(0, n+1):
    if i==0:
      a = 0
      b = 0
      c = 0
    else:
      c = int((a + b + 1)%10)
      a = b
      b = c
  return c

# def fibonacci(n):
#   f = [0,1]
#   for i in range(2,n+1):
#     f.append(f[i-1] + f[i-2])
#   return f[n]

# def fib_sum_last_digit(n):
#   return (fibonacci(n-1) - 1)%10


print (fibonacci_sum_last_digit(n))