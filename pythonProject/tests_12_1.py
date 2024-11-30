import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_runner = runner.Runner('Peter')
        for _ in range(10):
            test_runner.walk()
        self.assertEqual(test_runner.distance, 50)


    def test_run(self):
        test_runner = runner.Runner('Peter')
        for _ in range(10):
            test_runner.run()
        self.assertEqual(test_runner.distance, 100)


    def test_challenge(self):
        test_runner_1 = runner.Runner('Peter')
        test_runner_2 = runner.Runner('Peter')
        for _ in range(10):
            test_runner_1.walk()
            test_runner_2.run()
        self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)



