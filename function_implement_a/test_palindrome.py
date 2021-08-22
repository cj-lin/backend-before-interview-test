import unittest

from palindrome import isPalindrome


class TestPalindromes(unittest.TestCase):

    def test_ex1(self):
        self.assertTrue(isPalindrome('A man, a plan, a canal: Panama'))

    def test_ex2(self):
        self.assertFalse(isPalindrome('race a car'))


if __name__ == '__main__':
    unittest.main()
