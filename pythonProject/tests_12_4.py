import logging
import unittest
class Runner:
    def __init__(self, name, speed=5):
        if isinstance(name, str):
            self.name = name
        else:
            raise TypeError(f'Имя может быть только строкой, передано {type(name).__name__}')
        self.distance = 0
        if speed > 0:
            self.speed = speed
        else:
            raise ValueError(f'Скорость не может быть отрицательной, сейчас {speed}')

    def run(self):
        self.distance += self.speed * 2

    def walk(self):
        self.distance += self.speed

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    def __eq__(self, other):
        if isinstance(other, str):
            return self.name == other
        elif isinstance(other, Runner):
            return self.name == other.name


class Tournament:
    def __init__(self, distance, *participants):
        self.full_distance = distance
        self.participants = list(participants)

    def start(self):
        finishers = {}
        place = 1
        while self.participants:
            for participant in self.participants:
                participant.run()
                if participant.distance >= self.full_distance:
                    finishers[place] = participant
                    place += 1
                    self.participants.remove(participant)

        return finishers

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            test_runner = runner.Runner('Peter',-2)
            for _ in range(10):
                test_runner.walk()
            self.assertEqual(test_runner.distance, 50)
            logging.info('test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner')


    def test_run(self):
        try:
            test_runner = Runner(0)
            for _ in range(10):
                test_runner.run()
            self.assertEqual(test_runner.distance, 100)
            logging.info('"test_run" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner')


    def test_challenge(self):
        test_runner_1 = Runner('Peter')
        test_runner_2 = Runner('Peter')
        for _ in range(10):
            test_runner_1.walk()
            test_runner_2.run()
        self.assertNotEqual(test_runner_1.distance, test_runner_2.distance)

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', encoding='utf-8',
                        format='%(asctime)s | %(levelname)s | %(message)s')