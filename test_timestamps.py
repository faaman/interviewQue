import unittest
import logParse


class TestTimeStamps(unittest.TestCase):
    def test_error_one(self):
        #logParse.catching_no_files()
        logParse.find_timestamps('textForParsing.log', 2)
        logParse.first_lines('textForParsing.log', 3)
        print("hi there")


if __name__ == '__main__':
    unittest.main()
