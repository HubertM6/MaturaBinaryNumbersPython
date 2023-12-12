from pathlib import Path
import sys

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

import unittest
import time

from src.task_3 import task_three
from test.test_logger import TestLogger

SUMMARY_TEST_LOG_FILE = "./test_results/task_3/test_summary.txt"
DETAILS_TEST_LOG_FILE = "./test_results/task_3/test_details.txt"


class TaskTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = TestLogger()

    @classmethod
    def tearDownClass(cls):
        cls.logger.save_results(SUMMARY_TEST_LOG_FILE, DETAILS_TEST_LOG_FILE)

    def test_task_three_matura_example(self):
        input_path = "./tests_input/matura_task_three_example.txt"

        expected = (5, 1)
        start = time.time()
        result = task_three(input_path)
        end = time.time()
        duration = end - start

        TaskTest.logger.log_single_test_result("test_task_three_matura_example", result == expected, duration)
        self.assertEqual(expected, result)

    def test_task_three_matura_official(self):
        input_path = "./tests_input/matura_official_test.txt"

        expected = (859, 925)
        start = time.time()
        result = task_three(input_path)
        end = time.time()
        duration = end - start

        TaskTest.logger.log_single_test_result("test_task_three_matura_official", result == expected, duration)
        self.assertEqual(expected, result)

    def test_task_three_big(self):
        input_path = "./tests_input/big_test.txt"

        expected = (274, 346281)
        start = time.time()
        result = task_three(input_path)
        end = time.time()
        duration = end - start

        TaskTest.logger.log_single_test_result("test_task_three_big", result == expected, duration)
        self.assertEqual(expected, result)

    def test_task_three_max(self):
        input_path = "./tests_input/max_test.txt"

        expected = (123457, 123459)
        start = time.time()
        result = task_three(input_path)
        end = time.time()
        duration = end - start

        TaskTest.logger.log_single_test_result("test_task_three_max", result == expected, duration)
        self.assertEqual(expected, result)

    def test_task_three_only_zero(self):
        input_path = "./tests_input/only_zero.txt"

        expected = (1, 1)
        start = time.time()
        result = task_three(input_path)
        end = time.time()
        duration = end - start

        TaskTest.logger.log_single_test_result("test_task_three_only_zero", result == expected, duration)
        self.assertEqual(expected, result)

    def test_task_three_only_one(self):
        input_path = "./tests_input/only_one.txt"

        expected = (1, 1)
        start = time.time()
        result = task_three(input_path)
        end = time.time()
        duration = end - start

        TaskTest.logger.log_single_test_result("test_task_three_only_one", result == expected, duration)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
