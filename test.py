import unittest

class TestStringMethods(unittest.TestCase):

    def test_upper(self):
        self.asserEqual('foo'.upper(), "FOO")

    def test_isupper(self):
        self.asserTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'Hello World'
        self.assertEqual(s.split(), ['Hello', 'World'])
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()