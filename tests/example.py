import unittest
import example

class ExampleTest(unittest.TestCase):

    def Useless(self):
        self.assertTrue(example.Example('test').thing == 'test')
