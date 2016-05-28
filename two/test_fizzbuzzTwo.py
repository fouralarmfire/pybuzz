from fizzbuzzTwo import fizzbuzz
import unittest

class TestFizzBuzzTwo(unittest.TestCase):

	def test_non_multiple_should_return_number(self):
		self.assertEqual(fizzbuzz(1), 1)

	def test_multiple_of_three_should_say_fizz(self):
		self.assertEqual(fizzbuzz(3), 'fizz')

	def test_multiple_of_five_should_say_buzz(self):
		self.assertEqual(fizzbuzz(5), 'buzz')

	def test_multiple_of_fifteen_should_say_fizzbuzz(self):
		self.assertEqual(fizzbuzz(15), 'fizzbuzz')

if __name__ == '__main__':
	unittest.main()