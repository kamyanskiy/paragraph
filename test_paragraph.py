import unittest

from paragraph import paragraph


class MyTestCase(unittest.TestCase):
    def test_paragraph(self):
        expected = ['1 2 3', '1 2.3', '1.2 3', '1.2.3']
        self.assertEqual(expected, paragraph("1.2.3"))

if __name__ == '__main__':
    unittest.main()
