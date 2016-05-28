import fizzbuzz
import unittest

class TestFizzBuzz(unittest.TestCase):
	
	def test_that_number_is_divisible_by_three(self):
		self.assertTrue(fizzbuzz.by_three(3))

	def test_that_number_is_not_divisible_by_three(self):
		self.assertFalse(fizzbuzz.by_three(1))

	def test_that_number_is_divisible_by_five(self):
		self.assertTrue(fizzbuzz.by_five(5))

	def test_that_number_is_not_divisible_by_five(self):
		self.assertFalse(fizzbuzz.by_five(1))

	def test_that_number_is_divisible_by_fifteen(self):
		self.assertTrue(fizzbuzz.by_fifteen(15))

	def test_that_number_is_not_divisible_by_fifteen(self):
		self.assertFalse(fizzbuzz.by_fifteen(1))

	def test_that_says_fizz_when_divisible_by_three(self):
		self.assertEqual(fizzbuzz.says(3), 'fizz')

	def test_that_says_buzz_when_divisible_by_five(self):
		self.assertEqual(fizzbuzz.says(5), 'buzz')

	def test_that_says_fizzbuzz_when_divisible_by_fifteen(self):
		self.assertEqual(fizzbuzz.says(15), 'fizzbuzz')

	def test_that_returns_number_if_none_of_above(self):
		self.assertEqual(fizzbuzz.says(1), 1)

if __name__ == '__main__':
	unittest.main()