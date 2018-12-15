import quilt_lang as _
import unittest


class TestMethods(unittest.TestCase):
    def test_leadingzero(s):
        s.assertEqual(_.leadingzero(1, 2), "01")

    def test_absolutenum(s):
        s.assertEqual(_.absolutenum(1), 1)
        s.assertEqual(_.absolutenum(-1), 1)

    def test_splitstring(s):
        s.assertEqual(_.splitstring("hello world !"), ["hello", "world", "!"])
        s.assertEqual(
            _.splitstring("hello world !", ' ', None), ["hello", "world", "!"])
        s.assertEqual(
            _.splitstring("hello world !", " "), ["hello", "world", "!"])
        s.assertEqual(_.splitstring("hello world !", " ", 0), "hello")

    def test_sort(s):
        s.assertEqual(_.sort(["c", "a", "b"]), ["a", "b", "c"])

    def test_pykeyword(s):
        s.assertTrue("True" in _.pykeyword("list"))
        s.assertTrue(_.pykeyword("in", "True"))
        s.assertFalse(_.pykeyword("in", "foo"))
        with s.assertRaises(RuntimeWarning):
            _.pykeyword("foo", "foo")

    def test_binboolflip(s):
        s.assertFalse(_.binboolflip(0))
        s.assertEqual(_.binboolflip(False), 0)
        s.assertTrue(_.binboolflip(1))
        s.assertEqual(_.binboolflip(True), 1)
        with s.assertRaises(RuntimeWarning):
            _.binboolflip("foo")

    def test_comparenum(s):
        s.assertTrue(_.comparenum(1, 1, "equal"))
        s.assertFalse(_.comparenum(0, 1, "equal"))
        s.assertTrue(_.comparenum(0, 1, "not equal"))
        s.assertFalse(_.comparenum(1, 1, "not equal"))
        s.assertTrue(_.comparenum(0, 1, "less than"))
        s.assertFalse(_.comparenum(1, 1, "less than"))
        s.assertTrue(_.comparenum(1, 0, "greater than"))
        s.assertFalse(_.comparenum(1, 1, "greater than"))
        s.assertTrue(_.comparenum(1, 0, "more than"))
        s.assertFalse(_.comparenum(1, 1, "more than"))
        s.assertTrue(_.comparenum(0, 1, "less than or equal to"))
        s.assertTrue(_.comparenum(1, 1, "less than or equal to"))
        s.assertFalse(_.comparenum(2, 1, "less than or equal to"))
        s.assertTrue(_.comparenum(1, 0, "greater than or equal to"))
        s.assertTrue(_.comparenum(1, 1, "greater than or equal to"))
        s.assertFalse(_.comparenum(0, 1, "greater than or equal to"))
        s.assertTrue(_.comparenum(1, 0, "more than or equal to"))
        s.assertTrue(_.comparenum(1, 1, "more than or equal to"))
        s.assertFalse(_.comparenum(0, 1, "more than or equal to"))
        with s.assertRaises(RuntimeWarning):
            _.comparenum(1, 1, "foo")

    def test_throwerror(s):
        with s.assertRaises(RuntimeError):
            _.throwerror("foo")

    def test_convertstring(s):
        s.assertEqual(_.convertstring(1), "1")

    def test_opposite(s):
        s.assertTrue(_.opposite(False))
        s.assertFalse(_.opposite(True))
        with s.assertRaises(RuntimeWarning):
            _.opposite("foo")

    def test_typematch(s):
        s.assertTrue(_.typematch(True, bool))
        s.assertTrue(_.typematch("foo", str))
        s.assertFalse(_.typematch(True, str))

    def test_sametype(s):
        s.assertTrue(_.sametype(True, False))
        s.assertFalse(_.sametype(True, "foo"))


if __name__ == '__main__':
    unittest.main()
