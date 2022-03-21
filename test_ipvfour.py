import unittest
import logParse


class TestIpvFour(unittest.TestCase):
    def test_error_one(self):
        logParse.find_ipv4('textForParsing.log', 27)

    def test_error_two(self):
        logParse.find_ipv4('textNoIpvs.log', 5)


if __name__ == '__main__':
    unittest.main()
