import unittest

from num_of_sorted import get_num_of_sorted


class TestPalindromes(unittest.TestCase):

    def test_ex0(self):
        self.assertEqual(get_num_of_sorted(["abc", "bce", "cae"]), 1)

    def test_ex1(self):
        self.assertEqual(get_num_of_sorted(["cba", "daf", "ghi"]), 1)

    def test_ex2(self):
        self.assertEqual(get_num_of_sorted(["a", "b"]), 0)

    def test_ex3(self):
        self.assertEqual(get_num_of_sorted(["zyx", "wvu", "tsr"]), 3)


if __name__ == '__main__':
    unittest.main()
