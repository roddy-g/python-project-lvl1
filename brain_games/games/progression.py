import random


STEP_MIN = 1
STEP_MAX = 10
PROGRESSION_START_MIN = 1
PROGRESSION_START_MAX = 50
PROGRESSION_LENGTH = 10
MISSING_PLACE_MIN = 0
GAME_TASK = 'What number is missing in the progression?'


def generate_round():
    step = random.randint(STEP_MIN, STEP_MAX)
    start = random.randint(PROGRESSION_START_MIN, PROGRESSION_START_MAX)
    progression = [(start + step * i) for i in range(PROGRESSION_LENGTH)]
    missing_place = random.randint(MISSING_PLACE_MIN, PROGRESSION_LENGTH - 1)
    correct_answer = str(progression[missing_place])
    progression[missing_place] = ".."
    question = ' '.join([str(elem) for elem in progression])
    return correct_answer, question
