# bot salute
def greet(bot_name, birth_year):
    print('Hello! My name is {}.'.format(bot_name))
    print('I was created in {}.'.format(birth_year))

# user name
def remind_name():
    print('Please, remind me your name.')
    name = input()
    print('What a great name you have, {}!'.format(name))

# count user age
def guess_age():
    print('Let me guess your age.')
    print('Enter remainders of dividing your age by 3, 5 and 7.')

    rem3 = int(input())
    rem5 = int(input())
    rem7 = int(input())
    age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105

    print("Your age is {}; that's a good time to start programming!".format(age))

# bot count
def count():
    print('Now I will prove to you that I can count to any number you want.')

    num = int(input())
    curr = 0
    while curr <= num:
        print(curr, '!')
        curr = curr + 1


# test of programming
def test():
    print("Let's test your programming knowledge.")
    print('Why do we use methods?')
    print('1. To repeat a statement multiple times.')
    print('2. To decompose a program into several small subroutines.')
    print('3. To determine the execution time of a program.')
    print('4. To interrupt the execution of a program.')
    answ = input()
    while answ != '2':
        if answ == '2':
            break;
        else:
            print('Please, try again.')
            answ = input()
    print('Completed, have a nice day!')


def end():
    print('Congratulations, have a nice day!')


greet('Stifler', '2021')  # bot name and year
remind_name()
guess_age()
count()
test()
end()
