import unittest
import logParse


class TestFirstLines(unittest.TestCase):
    def test_error_one(self):
        logParse.first_lines('textForParsing.log', 3, 2)

    def test_error_two(self):
        logParse.first_lines('textForParsing.log', 3, 4)

    def test_error_three(self):
        logParse.first_lines('textForParsing.log', 3, 82)

if __name__ == '__main__':
    unittest.main()
