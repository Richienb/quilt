import quilt_lang as _
import unittest

_.pingtest()


class TestMethods(unittest.TestCase):
    def test_leadingzero(self):
        self.assertEqual(_.leadingzero(1, 2), "01")


if __name__ == '__main__':
    unittest.main()
