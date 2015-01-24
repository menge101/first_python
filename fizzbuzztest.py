from fizzbuzz import FizzBuzz
import unittest

class FizzBuzzTest(unittest.TestCase):

  def test_happy_path(self):
    nums = [-13,-11,-7,-2,-1,1,2,7,11,13]
    for value in nums:      
      self.assertEqual(FizzBuzz.fizzbuzz(self,(2 * value)), (2 * value))
      self.assertEqual(FizzBuzz.fizzbuzz(self,(3 * value)), 'Fizz')
      self.assertEqual(FizzBuzz.fizzbuzz(self,(5 * value)), 'Buzz')
      self.assertEqual(FizzBuzz.fizzbuzz(self,(15 * value)), 'Fizzbuzz')

  def test_non_string(self):
    with self.assertRaises(TypeError) as cm:
      FizzBuzz.fizzbuzz(self, 'not an integer')

if __name__ == '__main__':
  unittest.main()
