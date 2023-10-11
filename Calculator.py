import sys

def add(n1, n2):
  answer = (n1 + n2)
  print(answer)
def subtract(n1, n2):
  answer = (n1 - n2)
  print(answer)
def multiply(n1, n2):
  answer = (n1 * n2)
  print(answer)
def divide(n1, n2):
  answer = (n1 / n2)
  print(answer)

print("A. Addition")
print("B. Subtraction")
print("C. Multiplacation")
print("D. Division")
print("E. Exit")

choice = input("Enter Your Choice: ")
if "a" == choice or "A" == choice:
  print("Addition")
  n1 = int(input(": "))
  n2 = int(input(": "))
  add(n1, n2)
elif "b" == choice or "B" == choice:
  print("Subtraction")
  n1 = int(input(": "))
  n2 = int(input(": "))
  subtract(n1, n2)
elif "c" == choice or "C" == choice:
  print("Multiplacation")
  n1 = int(input(": "))
  n2 = int(input(": "))
  multiply(n1, n2)
elif "d" == choice or "D" == choice:
  print("Division")
  n1 = int(input(": "))
  n2 = int(input(": "))
  divide(n1, n2)
elif "e" == choice or "E" == choice:
  sys.exit("You Exited The Program")
