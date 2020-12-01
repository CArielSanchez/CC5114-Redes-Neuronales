import unittest
from tsp import *
#Testea diferentes perceptrones.
class Test_TSP(unittest.TestCase):

    def test_dist(self):
        c1=City("A",0,0)
        c2=City("B",3,4)
        d=c2.getDistance(c1)
        d1zero=c1.getDistanceZero()
        d2zero =c2.getDistanceZero()
        latitude1,longitude1 = c1.getCoordinate()
        latitude2,longitude2 = c2.getCoordinate()
        self.assertEqual(d,5)
        self.assertEqual(d1zero,0)
        self.assertEqual(d2zero,5)
        self.assertEqual(latitude1,0)
        self.assertEqual(longitude1,0)
        self.assertEqual(latitude2,3)
        self.assertEqual(longitude2,4)
    def test_dist2(self):
        c1=City("A",3,4)
        c2=City("B",9,12)
        d=c2.getDistance(c1)
        d1zero=c1.getDistanceZero()
        d2zero =c2.getDistanceZero()
        latitude1,longitude1 = c1.getCoordinate()
        latitude2,longitude2 = c2.getCoordinate()
        self.assertEqual(d,10)
        self.assertEqual(d1zero,5)
        self.assertEqual(d2zero,15)
        self.assertEqual(latitude1,3)
        self.assertEqual(longitude1,4)
        self.assertEqual(latitude2,9)
        self.assertEqual(longitude2,12)

    def test_dist3(self):
        c1=City("A",3,4)
        c2=City("B",3,4)
        d=c2.getDistance(c1)
        d1zero=c1.getDistanceZero()
        d2zero =c2.getDistanceZero()
        latitude1,longitude1 = c1.getCoordinate()
        latitude2,longitude2 = c2.getCoordinate()
        self.assertEqual(d,0)
        self.assertEqual(d1zero,5)
        self.assertEqual(d2zero,5)
        self.assertEqual(latitude1,3)
        self.assertEqual(longitude1,4)
        self.assertEqual(latitude2,3)
        self.assertEqual(longitude2,4)



if __name__=="__main__":
    unittest.main()