import prompt
import random

def gcd():
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Find the greatest common divisor of given numbers.")
    cnt = 0
    while cnt < 3:
        r_number1 = random.randint(1, 100)
        r_number2 = random.randint(1, 100)
        print(f'Question: {r_number1} {r_number2}')
        a = max(r_number1, r_number2)
        b = min(r_number1, r_number2)
        while b != 0:
            max_divisor = b
            b = a % b
            a = max_divisor
        answer = prompt.integer('Your answer:  ')
        if max_divisor == answer:
            cnt += 1
            print('Correct!')
            if cnt == 3:
                print(f'Cogratulations, {name}!')
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{max_divisor}'.")
            print(f"Let's try again, {name}!")
            break

