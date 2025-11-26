import unittest

class TestApp(unittest.TestCase):
    def test_example(self):
        self.assertEqual(1 + 1, 2)

if _name_ == "_main_":
    unittest.main()
