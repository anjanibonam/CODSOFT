
def do_math(a, b, op):
  """
  Executes a basic arithmetic operation based on the operator.

  Args:
      a: The first operand (float).
      b: The second operand (float).
      op: The symbol representing the operation (str, one of "+", "-", "*", "/").

  Returns:
      The result of the calculation (float) or None if an error occurs.
  """
  ops = {
      "+": lambda x, y: x + y,
      "-": lambda x, y: x - y,
      "*": lambda x, y: x * y,
      "/": lambda x, y: y and x / y  
  }
  if op in ops:
    return ops[op](a, b)
  else:
    print("Invalid operation symbol provided.")
    return None

while True:
  while True:
    try:
      a = float(input("Enter the first number: "))
      b = float(input("Enter the second number: "))
      op = input("Choose an operation (+, -, *, /): ")
      break
    except ValueError:
      print("Invalid input. Please enter numbers only.")

  result = do_math(a, b, op)
  if result is not None:
    print(f"{a} {op} {b} = {result}")

  choice = input("Do you want to perform another calculation? (yes/no): ")
  if choice.lower() != "yes":
    break

print("Calculator closed.")