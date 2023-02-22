import sys
sys.path.append("D:\Python Programs")

import ithhoccurance

import unittest
class Test_occurance(unittest.TestCase):
    def testcase1(self):
        self.assertEqual(ithhoccurance.ithoccurance(["hi","hello","hi","byee","lagnar","hi","abc","hi","yyg","hi"]),['hi', 'hello', 'hi', 'byee', 'lagnar', 'abc', 'hi', 'yyg', 'hi'])

if __name__=="__main__":
    unittest.main()
