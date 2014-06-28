import unittest
import example

class ExampleTest(unittest.TestCase):

    def testUseless(self):
        ex = example.Example('test')
        self.assertTrue(ex.thing == 'test')

if __name__ == '__main__':
    unittest.main()
