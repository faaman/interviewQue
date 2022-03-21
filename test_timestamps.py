import unittest
import logParse


class TestTimeStamps(unittest.TestCase):
    def test_error_one(self):
        logParse.find_timestamps('textForParsing.log', 27)

    def test_error_two(self):
        logParse.find_timestamps('textNoIpvs.log', 5)


if __name__ == '__main__':
    unittest.main()
