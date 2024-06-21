#!/usr/bin/env python3
import prompt
import random


def main():
    print("Welcome to the Brain Games!")
    calc()


def calc():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    cnt = 0
    while cnt < 3:
        r_number1 = random.randint(1, 100)
        r_number2 = random.randint(1, 100)
        operator = random.choice(['+' ,'-' ,'*'])
        print(f'Question: {r_number1} {operator} {r_number2}')
        if operator == '+':
            correct_answer = r_number1 + r_number2
        elif operator == '-':
            correct_answer = r_number1 - r_number2
        else:
            correct_answer = r_number1 * r_number2
        answer = prompt.integer('Your answer:  ')
        if correct_answer == answer:
            cnt += 1
            print('Correct!')
            if cnt == 3:
                print(f'Cogratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            break


if __name__ == "__main__":
    main()


