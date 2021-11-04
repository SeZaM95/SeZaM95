import keyboard
import time

flagSpeed = False
speed = 60
StrSpeed = ""
comment = False

while(True):
    key = keyboard.read_key()
    time.sleep(0.5)
    if key <= '9' and key >= '0':
        speed = 15 * 2 ** int(key)
        print("speed:", speed)
    if key == 'f2':
        speed /= 2 ** 0.5
        print("speed:", speed)
    if key == 'f8':
        speed *= 2 ** 0.5
        print("speed:", speed)
    if key == 'shift':
        note = open('note.txt').read()
        for i in note:
            if i =='-':
                keyboard.send("shift+'")
            if i ==':' and flagSpeed == False:
                flagSpeed = True
            if flagSpeed and i <= '9' and i >= '0':
                StrSpeed += i
            if i == '#':
                StrSpeed = ""
                comment = True;
            if i!=' ' and i!= '\n' and not comment and not flagSpeed:
                keyboard.send(i)
##                time.sleep(0.1)
            if i == ' ' and not comment and not flagSpeed:
                time.sleep(60/(4*speed))
            if i == '\n':
                if StrSpeed != '':
                    speed = int(StrSpeed)
                flagSpeed = False
                comment = False
                time.sleep(60/(2*speed))
    if key == 'esc':
        break;
