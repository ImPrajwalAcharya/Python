import random
import os
import time


def flipcoin():
    os.system('clear')
    animatecoin()
    displaycoin()
    flipagain = input('Enter to roll again tab to exit')
    if (flipagain == ''):
        flipcoin()


def displaycoin():
    new = random.randint(0, 1)
    if (new == 0):
        print('Head')
    else:
        print('Tail')


def animatecoin():
    for i in range(10):
        displaycoin()
        time.sleep(0.5)
        os.system('clear')


def animatedice():
    for i in range(10):
        display()
        time.sleep(0.5)
        os.system('clear')


def display():
    new = random.randint(1, 6)
    if (new == 1):
        print(' ------- ')
        print('|       |')
        print('|   *   |')
        print('|       |')
        print(' ------- ')
    elif (new == 2):
        print(' ------- ')
        print('|       |')
        print('| *   * |')
        print('|       |')
        print(' ------- ')
    elif (new == 3):
        print(' ------- ')
        print('|  *    |')
        print('|   *   |')
        print('|    *  |')
        print(' ------- ')
    elif (new == 4):
        print(' ------- ')
        print('| *   * |')
        print('|       |')
        print('| *   * |')
        print(' ------- ')
    elif (new == 5):
        print(' ------- ')
        print('| *   * |')
        print('|   *   |')
        print('| *   * |')
        print(' ------- ')
    else:
        print(' ------- ')
        print('| *   * |')
        print('| *   * |')
        print('| *   * |')
        print(' ------- ')


def rolldice():
    os.system('clear')
    animatedice()
    display()
    rollagain = input('Enter to roll again tab to exit')
    if (rollagain == ''):
        rolldice()


while (1):
    choice = input('Choose\n1.FlipCoins\n2.RollDice\n3.Exit')
    if (int(choice) == 1):
        flipcoin()
    elif (int(choice) == 2):
        rolldice()
    elif (int(choice) == 3):
        exit()
    else:
        print('Wrong choice')
