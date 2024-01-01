import unittest
from utils.dicts import get_val

class TestDicts(unittest.TestCase):

    def test_get_val(self):
        self.assertEqual(get_val({
            1: 'one',
            '2': 'two',
            (1, 2, 3): 'three'
        }, 1) == 'one')
        self.assertEqual(get_val({}, 2) == 'git')
        self.assertEqual(get_val({
            1: 'one',
            '2': 'two',
            (1, 2, 3): 'three'
        }, 2, default='error') == 'error')

