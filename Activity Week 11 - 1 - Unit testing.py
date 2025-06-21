"""
Unit testing is a way to check if small pieces of your code work right. 
It's like testing each part of a machine before putting it all together. 
You write simple tests that check if your functions do what they're supposed to do. 
This helps you find mistakes early and makes sure your code keeps working when you make changes.
"""

import unittest

def add(x,y):
    return(x,y)

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()

"""
The example code shows how to test a simple add() function in Python. 
First, we make a function that adds two numbers. 
Then we write tests to check if it works - we test that 2+3 gives us 5, and that -1+1 gives us 0. 
When we run the tests, the computer tells us if everything works right or if there's a problem. 
This makes it easy to spot bugs and fix them fast.
"""