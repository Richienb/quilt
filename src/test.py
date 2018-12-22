import quilt_lang as _
import unittest


class TestMethods(unittest.TestCase):
    def test_leadingzero(s):
        s.assertEqual(_.leadingzero(1, 2), "01")

    def test_splitstring(s):
        s.assertEqual(_.splitstring("hello world !"), ["hello", "world", "!"])
        s.assertEqual(
            _.splitstring("hello world !", ' ', None), ["hello", "world", "!"])
        s.assertEqual(
            _.splitstring("hello world !", " "), ["hello", "world", "!"])
        s.assertEqual(_.splitstring("hello world !", " ", 0), "hello")

    def test_pykeyword(s):
        s.assertTrue("True" in _.pykeyword("list"))
        s.assertTrue(_.pykeyword("in", "True"))
        s.assertFalse(_.pykeyword("in", "foo"))
        with s.assertRaises(ValueError):
            _.pykeyword("foo", "foo")

    def test_binboolflip(s):
        s.assertFalse(_.binboolflip(0))
        s.assertEqual(_.binboolflip(False), 0)
        s.assertTrue(_.binboolflip(1))
        s.assertEqual(_.binboolflip(True), 1)
        with s.assertRaises(ValueError):
            _.binboolflip("foo")

    def test_typematch(s):
        s.assertTrue(_.typematch(True, bool))
        s.assertTrue(_.typematch("foo", str))
        s.assertFalse(_.typematch(True, str))

    def test_sametype(s):
        s.assertTrue(_.sametype(True, False))
        s.assertFalse(_.sametype(True, "foo"))


if __name__ == '__main__':
    unittest.main()
