import unittest


class TestCase(unittest.TestCase):
    
    def test_basic(self):
        testcase = "aAyush"
        expected = "AAYUSH"
        my_func = lambda x:x.upper()
        self.assertEqual(my_func(testcase),expected)
    

unittest.main()
