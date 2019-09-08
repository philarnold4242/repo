import unittest

from module import MyClass


class TestMyClass(unittest.TestCase):

    def test_myfunc(self):

        qry = MyClass.myfunc(self, 2, 3);
        sbj = 5

        self.assertEqual(sbj, qry)


if __name__ == '__main__':
    unittest.main()

