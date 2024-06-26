import prompt
import random


def is_even(number):
    return 'yes' if number % 2 == 0 else 'no'


def question():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    cnt = 0
    while cnt < 3:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer:  ')
        if is_even(random_number) == answer:
            cnt += 1
            print('Correct!')
            if cnt == 3:
                print(f'Cogratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{is_even(random_number)}'.")
            print(f"Let's try again, {name}!")
            break
