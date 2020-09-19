import unittest

from point import Point


class TestPoint(unittest.TestCase):
    def test_point_init(self):
        point = Point()

        self.assertEqual(point.x, 0.0)
        self.assertEqual(point.y, 0.0)

        point = Point(10, 5)

        self.assertEqual(point.x, 10.0)
        self.assertEqual(point.y, 5.0)

    def test_point_init_exception(self):
        with self.assertRaises(TypeError):
            Point('wrong', 'type')

        with self.assertRaises(TypeError):
            Point(dir, float)

    def test_point_string(self):
        point_string = str(Point())
        self.assertEqual(point_string, '(0.0, 0.0)')

    def test_point_setters_and_getters(self):
        point = Point(10, 5)

        self.assertEqual(point.x, 10.0)
        self.assertEqual(point.y, 5.0)

        point.x = 42

        self.assertEqual(point.x, 42.0)

    def test_point_setters_and_getters_exception(self):
        point = Point(10, 5)

        with self.assertRaises(TypeError):
            point.x = 'wrong'

        with self.assertRaises(TypeError):
            point.x = dir

    def test_point_operators(self):
        a = Point()
        b = Point()
        c = Point(10, 12)

        self.assertTrue(a == b)
        self.assertFalse(a == c)
        self.assertFalse(a != b)
        self.assertTrue(a != c)


if __name__ == '__main__':
    unittest.main()
