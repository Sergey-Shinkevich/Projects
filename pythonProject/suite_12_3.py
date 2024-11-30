import unittest
import tests_12_3_1
import tests_12_3_2

runnerST = unittest.TestSuite()
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_1.TournamentTest))
runnerST.addTest(unittest.TestLoader().loadTestsFromTestCase(tests_12_3_2.RunnerTest))
runner = unittest.TextTestRunner(verbosity=2)
runner.run(runnerST)

