import csv
import random

class colors:
    CORRECT = '\033[92m'
    WRONGSPOT = '\033[93m'
    WRONG = '\033[91m'
    ENDC = '\033[0m'

display = []
keyboard = ["q", "w", "e", "r", "t", "y", "u", "i", "o", "p",
            "a", "s", "d", "f", "g", "h", "j", "k", "l",
            "z", "x", "c", "v", "b", "n", "m"]
keyboard_back = keyboard.copy()
loop = True

with open("valid.txt") as f:
    valid_list = f.read().split("\n")

with open('answer.txt') as f:
    answer_list = f.read().split("\n")

answer = str(random.choice(answer_list)).upper()

wlen = len(answer)

def mod(ans, gue):
    answer = list(ans)
    guess = list(gue)
    back = guess.copy()
    for i in range(wlen):
        for j in range(wlen):
            if guess[i] == answer[j] and i == j:
                back[i] = colors.CORRECT + guess[i] + colors.ENDC
                if guess[i].lower() in keyboard_back:
                    keyboard[keyboard_back.index(guess[i].lower())] = colors.CORRECT + guess[i].lower() + colors.ENDC
                    keyboard_back[keyboard_back.index(guess[i].lower())] = colors.CORRECT + guess[i].lower() + colors.ENDC
                break
            elif guess[i] == answer[j] and i != j:
                back[i] = colors.WRONGSPOT + guess[i] + colors.ENDC
                if guess[i].lower() in keyboard_back:
                    keyboard[keyboard_back.index(guess[i].lower())] = colors.WRONGSPOT + guess[i].lower() + colors.ENDC
        if guess[i] not in answer and guess[i].lower() in keyboard_back:
            keyboard[keyboard_back.index(guess[i].lower())] = "-"
    return ' '.join(back)

while loop:
    guess = input().upper()
    if guess.lower() not in valid_list or len(guess) < wlen:
        print(colors.WRONG + "not valid" + colors.ENDC)
        continue
    if guess == answer:
        loop = False
    guess = mod(answer, guess)
    display.append(guess)
    if wlen == 5:
        print("     ", end="")
    elif wlen == 4:
        print("      ", end="")
    print("_", end="")
    for i in range(wlen-1):
        print("__", end="")
    print()
    for i in display:
        if wlen == 5:
            print('     ', end='')
        elif wlen == 4:
            print("      ", end="")
        print(i)
    print()
    for i in range(10):
        print(keyboard[i], end=' ')
    print()
    print(' ', end='')
    for i in range(10, 19):
        print(keyboard[i], end=' ')
    print()
    print('   ', end='')
    for i in range(19, 26):
        print(keyboard[i], end=' ')
    print()