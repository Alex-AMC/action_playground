import unittest

import chickens


class TestChickens(unittest.TestCase):

    def setUp(self) -> None:
        self.chicken = chickens.Chicken(name='Daisy', age=1)

    def test_adding_works(self):
        """ Adding an egg to the chicken works"""
        self.chicken.total_eggs = 0
        self.chicken.add_egg_to_total(2)
        self.assertEqual(self.chicken.total_eggs, 2)

    def test_age_works(self):
        """ I can see the age"""
        self.assertEqual(self.chicken.age, 1)


if __name__ == '__main__':
    unittest.main()
