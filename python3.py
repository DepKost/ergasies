#!/usr/bin/python

import sys

string = ''
counter0 = 0
flag = True

while (flag):
    for char in sys.stdin.read(1):
        if char == '\n':
            flag = False
            break
        else:
            if char == '0':
                counter0 = counter0 + 1
            else:
                string = string + char

for i in range(counter0):
    string = string + '0'

print string
