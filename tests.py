import unittest
from bowling import score

class MyTests(unittest.TestCase):
    def test_everything_is_fine_please(self):
        self.assertEqual(score("11111111112222222222"), 30)
        self.assertEqual(score("5/11------------3/11"), 26)
        self.assertEqual(score("1/35XXX458/X3/23"),     160)
        self.assertEqual(score("1/35XXX458/X3/XX6"),    189)

if __name__ == '__main__':
    unittest.main()
