from pathlib import Path
import sys

path_root = Path(__file__).parents[1]
sys.path.append(str(path_root))

import unittest
import time

from src.task import task_one
from test.test_logger import TestLogger

SUMMARY_TEST_LOG_FILE = "./test_results/task_1/test_summary.txt"
DETAILS_TEST_LOG_FILE = "./test_results/task_1/test_details.txt"


class TaskTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.logger = TestLogger()

    @classmethod
    def tearDownClass(cls):
        cls.logger.save_results(SUMMARY_TEST_LOG_FILE, DETAILS_TEST_LOG_FILE)

    def test_task_one_matura_example(self):
        input_path = "./tests_input/matura_task_one_example.txt"

        expected = 3
        start = time.time()
        result = task_one(input_path)
        end = time.time()
        duration = end - start

        TaskTest.logger.log_single_test_result("test_task_one_matura_example", result == expected, duration)
        self.assertEqual(expected, result)

    def test_task_one_only_zero(self):
        input_path = "./tests_input/only_zero.txt"

        expected = 1
        start = time.time()
        result = task_one(input_path)
        end = time.time()
        duration = end - start

        TaskTest.logger.log_single_test_result("test_task_one_only_zero", result == expected, duration)
        self.assertEqual(expected, result)

    def test_task_one_only_one(self):
        input_path = "./tests_input/only_one.txt"

        expected = 0
        start = time.time()
        result = task_one(input_path)
        end = time.time()
        duration = end - start

        TaskTest.logger.log_single_test_result("test_task_one_only_one", result == expected, duration)
        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
