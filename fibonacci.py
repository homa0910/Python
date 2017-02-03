# python3
import sys

input = sys.stdin.read()
tokens = input.split()
n = int(tokens[0])

def fibonacci(n):
  f = [0,1]
  for i in range(2,n+1):
    f.append(f[i-1] + f[i-2])
  return f[n]

print (fibonacci(n))