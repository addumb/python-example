import unittest
import example

class ExampleTest(unittest.TestCase):

    def testUseless(self):
        self.ex = example.Example()
        self.assertEqual(self.ex.thing, 'Not nothing.')

