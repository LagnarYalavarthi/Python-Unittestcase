import sys
sys.path.append("D:\Python Programs")
import reverse_string

import unittest
class Test_rev(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(reverse_string.reverse("lagnar"),"rangal")

if __name__=="__main__":
    unittest.main()
