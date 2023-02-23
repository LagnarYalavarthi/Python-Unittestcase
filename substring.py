import sys
sys.path.append("D:\Python Programs")
import sub_string

import unittest
class Test_string(unittest.TestCase):
    def testcase1(self):
        self.assertTrue(sub_string.substring(("lagnaryalavarthi"),("lagnar")))

if __name__=="__main__":
    unittest.main()
