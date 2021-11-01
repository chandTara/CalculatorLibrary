from unittest import TestCase
from unittest.mock import patch

from test import Employee

class TestEmployee(TestCase):
    @patch('test.Employee.printEmloyeeCount')
    def test_print_count(self, mock_cnt):
        mock_cnt = 1
        self.assertEqual(mock_cnt,1)

    @patch('test.Employee.displayCount')
    def test_displayCount(self, mock_display):
        mock_display = "Display value"

if __name__ == '__main__':
    unittest.main()
