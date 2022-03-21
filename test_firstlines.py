import unittest
import logParse


class TestFirstLines(unittest.TestCase):
    def test_error_one(self):
        logParse.first_lines('textForParsing.log', 27, 2)

    def test_error_two(self):
        logParse.first_lines('textForParsing.log', 27, 4)

    def test_error_three(self):
        # this test fails due to: check in line.133 in logParse.py is not present here
        logParse.first_lines('textForParsing.log', 27, 82)

    def test_error_four(self):
        logParse.first_lines('textForParsing.log', 27, -3)

if __name__ == '__main__':
    unittest.main()
