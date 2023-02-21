import sys
sys.path.append("D:\Python Programs")
import copydict

import unittest
class Test_copyofdict(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(copydict.cpdict({'name':'lagnar','age':25,'location':'avanigadda'}),{'name':'lagnar','age':25,'location':'avanigadda'})


if __name__=="__main__":
    unittest.main()
