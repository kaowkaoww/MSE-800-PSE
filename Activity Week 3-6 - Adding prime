#Activity W3-6: Expand your previous project (Activity W3-6) with adding prime functionality

class checkNum:
  def __init__(self,number):
    self.number = number

  def calculateFac(self):
    result = 1
    for i in range(1, self.number+1):
      result *=i
    return result
  
  def is_prime(self):
    if self.number <= 1:
      return False
    for i in range(2, int(self.number ** 0.5) + 1):
            if self.number % i == 0:
                return False
    return True



#input
number = int(input("Enter number :"))

#calNum
num_operations = checkNum(number)

#output
print(f"{number}! = {num_operations.calculateFac()}")
if num_operations.is_prime():
   print(f"{number} is a prime number")
else:
   print(f"{number} is not prime number")
