import prompt


def check(answer, correct_answer, name):
    if answer == correct_answer:
        print('Correct!')
        return True
    else:
        print("""\"{}\" is wrong answer ;(. Correct answer was \"{}\".
Let\"s try again, {}!""".format(answer, correct_answer, name))
        return False


def greeting():
    print("\nWelcome to the Brain Games!")


def greeting_name():    
    name = prompt.string('May I have your name? ')
    print('Hello, ', name, "!\n")
    return name
