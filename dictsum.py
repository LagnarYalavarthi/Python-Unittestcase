import sys
sys.path.append("D:\Python Programs")

import sumdict

import unittest
class Test_sumofdict(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(sumdict.sumdict({"a":2, "b":3, "c":5}),10)

if __name__=="__main__":
    unittest.main()
