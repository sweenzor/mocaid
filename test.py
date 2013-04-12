import sys
import time

from blessings import Terminal

t = Terminal()

print t.bold('Hi there!')
print t.bold_red_on_bright_green('It hurts my eyes!')

with t.location(0, t.height - 1):
    print 'This is at the bottom.'

print t.move_down + 'hi'

inp = None
while inp != 'q':
    inp = t.getch()
    if inp:
        print 'hi:' +  inp
