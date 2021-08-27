import random

import pyautogui

import time

# text = input('Enter your text: \n  ')

while True:
    try:
        n = int(input('How many times you want to repeat it:\n  '))
        t = int(input('Enter needed seconds: \n  '))
        break
    except ValueError:
        print("Please input integer only...\n")
        continue

print(
    f' will be repeated {n} times after {t} seconds.\nTo stop move your cursor to the upper left corner of your screen.')
print(f'Go to the desired textfield in\n')
for i in range(t):
    print(f'{t - i} seconds\n')
    time.sleep(1)

for i in range(n):
    ru = random.randint(0, 3)
    rm = random.randint(2, 15)

    ra = random.randint(2, 18)
    rh = random.randint(2, 17)
    text = "U" + "m" * rm + "a" * ra + "h" * rh
    pyautogui.typewrite(f'{text}')
    pyautogui.press('enter')
    time.sleep(2)
