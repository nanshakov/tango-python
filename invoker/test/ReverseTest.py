from Invoker import reverse_number
import unittest


class ReverseTest(unittest.TestCase):
    def test_base_case(self):
        self.assertEqual(14, reverse_number(41))

    def test_base_case_2(self):
        self.assertEqual(114, reverse_number(411))

    def test_zero(self):
        self.assertEqual(0, reverse_number(0))

if __name__ == '__main__':
    unittest.main()
