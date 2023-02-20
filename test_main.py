import math
from unittest import TestCase
from main import getData
from main import search

#
class Test(TestCase):
    def test_search(self):
        jugs = [math.inf,1,4,10,15,22]
        final = 181
        cost, path = search(jugs, final)
        self.assertEqual(cost, 19)

    def test_search1(self):
        jugs = [math.inf,3,6]
        final = 2
        cost, path = search(jugs, final)
        self.assertEqual(cost, -1)

    def test_search2(self):
        jugs = [math.inf,2]
        final = 143
        cost, path = search(jugs, final)
        self.assertEqual(cost, -1)

    def test_search3(self):
        jugs = [math.inf,2,3,5,19,121,852]
        final = 11443
        cost, path = search(jugs, final)
        self.assertEqual(cost, 36)

    def test_search4(self):
        jugs = [math.inf,2,5,6,72]
        final = 143
        cost, path = search(jugs, final)
        self.assertEqual(cost, 7)
