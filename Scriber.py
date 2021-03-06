from pynput.mouse import Controller
from pynput.keyboard import Listener
import png
import msvcrt
import sys
import select
import keyboard

mouse = Controller()
width = 192
height = 108

aCount = 0
bCount = 0
cCount = 0

s = [['0' for w in range(width)] for h in range(height)]

lastSavedMouseX = 0

while True:

    if keyboard.is_pressed('q'):
        break
    path = ''

    while True:  # making a loop
        try:
            x = lastSavedMouseX = int(mouse.position[0] / 10)
            y = int(mouse.position[1] / 10)
            s[y][x] = '1'
        except:
            pass
        if keyboard.is_pressed('a'):  # if key 'q' is pressed
            aCount += 1
            path += 'a/'
            break  # finishing the loop
        elif keyboard.is_pressed('b'):  # if key 'q' is pressed
            bCount += 1
            path += 'b/'
            break  # finishing the loop
        elif keyboard.is_pressed('c'):  # if key 'q' is pressed
            cCount += 1
            path += 'c/'
            break  # finishing the loop
        if keyboard.is_pressed('q'):
            break

    ones = 0
    for i in range(len(s)):
        ones += s[i].count('1')

    if ones < 40:
        continue

    if path != '':
        modVal = 1
        # 20%
        if 'a' in path:
            modVal = aCount
        if 'b' in path:
            modVal = bCount
        if 'c' in path:
            modVal = cCount

        if modVal % 5 == 0:
            path = 'test/' + path
        else:
            path = 'train/' + path

        print("Writing to path: " + path)

        while abs(mouse.position[0] - lastSavedMouseX) < 10:
            pass

        s = map(lambda x: map(int, x), s)

        f = open(path + 'char' + str(modVal) + '.png', 'wb')
        w = png.Writer(width, height, greyscale=True, bitdepth=1)
        w.write(f, s)
        f.close()
        s = [['0' for w in range(width)] for h in range(height)]
