import sys
import time

number=1
while True:
    number += 1
    print('\a ', end="") 
    sys.stdout.write('\010')
    #print('\b\b')
    time.sleep(1)
    if number>int(10):
        break

print("here")