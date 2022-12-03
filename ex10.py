from random import randint


def computer_pick():
    return randint(1, 9)


def user_pick():
    try:
        user = int(input('Pick number from 1 to 9: '))
        if user not in range(1, 10):
            print('Only numbers 1-9 accepted')
        else:
            return user
    except ValueError:
        print('Only numbers')
        quit()


def game():
    while True:
        if user_pick() == computer_pick():
            print('You won!')
            break
        else:
            print('Try again')


game()
