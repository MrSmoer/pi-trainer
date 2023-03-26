# Pi-Trainer
A muscle-memory python script to remember digits of pi.

## Installation
### Windows
It uses curses for ui, so on windows you will need to install `windows-curses`
```
pip3 install windows-curses
```
### Android
This can also run within Termux, preferably installed through F-Droid
I recommend the PC-Numpad (not yet on appstores, build it yourself or [download it here](addons-languages-numpad-apk-1.apk)) extension for AnySoftKeyboard, to build up that muscle memory.

## Manual
- `q` quits
- `r` retry
- `+` or `-` (Senso only) changes the number of additional digits each round 
### Modes
- Standard - just type through the digits, mistakes count, but don't block
- Number Learning - type through digits blindly, beginning at certain digit, mistakes reset
- Senso - Like early senso game, each round one more. +/- change the increment size
- Select number - select the number you want to learn. Currently supported: Pi, e, random, and custom, which is loaded from custom.txt
