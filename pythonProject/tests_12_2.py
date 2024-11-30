from runner_and_tournament import Runner
from runner_and_tournament import Tournament
import unittest


class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = []

    def setUp(self):
        self.runner_1 = Runner('Усэйн', 10)
        self.runner_2 = Runner('Андрей', 9)
        self.runner_3 = Runner('Ник', 3)


    def test_tournament_1(self):
        tournament_current = Tournament(90, self.runner_1, self.runner_3)
        result = tournament_current.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    def test_tournament_2(self):
        tournament_current = Tournament(90, self.runner_2, self.runner_3)
        result = tournament_current.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[2] == 'Ник')

    def test_tournament_3(self):
        tournament_current = Tournament(90, self.runner_1, self.runner_2, self.runner_3)
        result = tournament_current.start()
        TournamentTest.all_results.append(result)
        self.assertTrue(result[3] == 'Ник')

    @classmethod
    def tearDownClass(cls):
        for i, elem in enumerate(cls.all_results):
            print(f'{i + 1}.', end=' ')
            for place, runner in elem.items():
                print(f'{place}: {runner.name} (speed: {runner.speed})', end=' ')
            print()

if __name__ == '__main__':
    unittest.main()


