import sys
sys.path.append("D:\Python Programs")

import oddindexed

import unittest
class Test_index(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(oddindexed.oddindex("hyderabad"),['y', 'e', 'a', 'a'])

if __name__=="__main__":
    unittest.main()
