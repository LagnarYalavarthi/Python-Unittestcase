import sys
sys.path.append("D:\Python Programs")

import fibanocci

import unittest
class Test_fib(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(fibanocci.fibanocci(5),"fib number")
    def testcase_2(self):
        self.assertEqual(fibanocci.fibanocci(7),"not fib")

if __name__=="__main__":
    unittest.main()
