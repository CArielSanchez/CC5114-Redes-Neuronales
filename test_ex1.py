import unittest
from ex1 import Perceptron,Gates

class Test_Perceptron(unittest.TestCase):
    def test_AND(self):
        AND_Perceptron = Perceptron([1, 1], -1.5)
        self.assertEqual(AND_Perceptron.run([1 ,1]), 1)
        self.assertEqual(AND_Perceptron.run([1, 0]), 0)
        self.assertEqual(AND_Perceptron.run([0, 1]), 0)
        self.assertEqual(AND_Perceptron.run([0, 0]), 0)

    def test_OR(self):
        OR_Perceptron = Perceptron([1, 1], -0.5)
        self.assertEqual(OR_Perceptron.run([1, 1]), 1)
        self.assertEqual(OR_Perceptron.run([1, 0]), 1)
        self.assertEqual(OR_Perceptron.run([0, 1]), 1)
        self.assertEqual(OR_Perceptron.run([0, 0]), 0)
    def test_NAND(self):
        NAND_Perceptron = Perceptron([-2, -2], 3)
        self.assertEqual(NAND_Perceptron.run([1, 1]), 0)
        self.assertEqual(NAND_Perceptron.run([1, 0]), 1)
        self.assertEqual(NAND_Perceptron.run([0, 1]), 1)
        self.assertEqual(NAND_Perceptron.run([0, 0]), 1)

    def test_Summing_Number_Gate(self):
        self.assertEqual(Gates().Summing_Numbers(1, 1), (1, 0))
        self.assertEqual(Gates().Summing_Numbers(1, 0), (0, 1))
        self.assertEqual(Gates().Summing_Numbers(0, 1), (0, 1))
        self.assertEqual(Gates().Summing_Numbers(0, 0), (0, 0))

if __name__=="__main__":
    unittest.main()