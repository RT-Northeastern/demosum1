import unittest 
from rt_fizzbuzz import rt_fizzbuzz

class TestFizzBuzz(unittest.TestCase): 
    def test_fizz(self): 
        self.assertTrue(rt_fizzbuzz(6) == "Fizz")
        self.assertFalse(rt_fizzbuzz(4) == "Fizz")
        self.assertEqual(rt_fizzbuzz(3),"Fizz")

    def test_buzz(self): 
        self.assertTrue(rt_fizzbuzz(10) == "Buzz")
        self.assertFalse(rt_fizzbuzz(11) == "Buzz")
        self.assertEqual(rt_fizzbuzz(5), "Buzz")

    def test_fizzbuzz(self): 
        self.assertTrue(rt_fizzbuzz(30) == "Fizzbuzz")
        self.assertFalse(rt_fizzbuzz(31) == "Fizzbuzz")
        self.assertEqual(rt_fizzbuzz(15), "Fizzbuzz")

    def test_number(self): 
        self.assertTrue(rt_fizzbuzz(2) == "2")
        self.assertFalse(rt_fizzbuzz(3) == "2")
        self.assertEqual(rt_fizzbuzz(1), "1")


unittest.main()




