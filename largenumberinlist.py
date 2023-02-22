import sys
sys.path.append("D:\Python Programs")
import largestnumberinlists

import unittest
class Test_largestnumbers(unittest.TestCase):
    def testcase_1(self):
        self.assertEqual(largestnumberinlists.largest([1,9999,2,3,4989]),9999)
    def testcase_2(self):
        self.assertEqual(largestnumberinlists.secondlargest([1,9999,2,3,4989]),4989)


    if __name__=="__main__":
        unittest.main()
