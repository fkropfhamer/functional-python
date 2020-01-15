import unittest
import myFunctions

class TestMyFunctionsMethods(unittest.TestCase):

    def test_map(self):
        fn = lambda x : 2 * x
        self.assertEqual(myFunctions.myMap([], fn), [])
        self.assertEqual(myFunctions.myMap([1,2,3], fn), [2, 4, 6])

    def test_filter(self):
        fn = lambda x : False
        fn2 = lambda x : True
        fn3 = lambda x : x == 2
        list = [1, 2, 3]

        self.assertEqual(myFunctions.myFilter(list, fn), list)
        self.assertEqual(myFunctions.myFilter(list, fn2), [])
        self.assertEqual(myFunctions.myFilter(list, fn3), [1, 3])

    def test_reduce(self):
        self.assertEqual(myFunctions.myReduce([], 5, lambda x, y : x), 5)

    def test_sum(self):
        self.assertEqual(myFunctions.mySum([]), 0)
        self.assertEqual(myFunctions.mySum([1, 2, 3]), 6)


if __name__ == "__main__":
    unittest.main()
