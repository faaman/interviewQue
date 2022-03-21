import unittest
import logParse


class TestLastLines(unittest.TestCase):
    def test_error_one(self):
        logParse.last_lines('textForParsing.log', 27, 4, 24)

    def test_error_two(self):
        logParse.last_lines('textForParsing.log', 27, 1, 27)

    def test_error_three(self):
        # here the user is looking to print more lines than are present in the file, so it just prints all lines
        logParse.last_lines('textForParsing.log', 27, 82, 0)

    def test_error_four(self):
        # this does not work as a test, needs tweaking
        logParse.last_lines('textForParsing.log', 27, -3, 0)

if __name__ == '__main__':
    unittest.main()
