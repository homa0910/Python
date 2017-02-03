# python3
import sys

input = sys.stdin.read()
tokens = input.split()
n = int(tokens[0])

def fibonacci_last_digit(n):
  a = 0
  b = 1
  for i in range(0,n+1):
    if i == 0:
      c = a
    elif i == 1:
      c = b
    else:
      c = a + b
      a = b
      b = c
  return c % 10

print (fibonacci_last_digit(n))