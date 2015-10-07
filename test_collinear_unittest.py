import unittest
from collinear import collinear1,collinear2,collinear3
 
class TestUM(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_1(self):
        self.assertEqual( collinear1(0,0,1,0,100000,1),-1)
        self.assertEqual( collinear2(0,0,1,0,100000,1),-1)
        self.assertEqual( collinear3(0,0,1,0,100000,1),-1)
         
    def test_2(self):
        self.assertEqual( collinear1(0,0,0,0,1,1),1)
        self.assertEqual( collinear2(0,0,0,0,1,1),1)
        self.assertEqual( collinear3(0,0,0,0,1,1),1)

    def test_3(self):
        self.assertEqual( collinear1(0,0,0,0,0,1),1)
        self.assertEqual( collinear2(0,0,0,0,0,1),1)
        self.assertEqual( collinear3(0,0,0,0,0,1),1)

    def test_4(self):
        self.assertEqual( collinear1(0,0,3,3,5,5),1)
        self.assertEqual( collinear2(0,0,3,3,5,5),1)
        self.assertEqual( collinear3(0,0,3,3,5,5),1)

    def test_5(self):
        self.assertEqual( collinear1(0,0,1,0,2,0),-1)
        self.assertEqual( collinear2(0,0,1,0,2,0),-1)
        self.assertEqual( collinear3(0,0,1,0,2,0),-1)

    def test_6(self):
        self.assertEqual( collinear1(0,0,100,0,200,0),-1)
        self.assertEqual( collinear2(0,0,100,0,200,0),-1)
        self.assertEqual( collinear3(0,0,100,0,200,0),-1)

        
if __name__ == '__main__':
    unittest.main()
