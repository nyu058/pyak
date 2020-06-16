# pyak
Python program to automically press a key after some time interval.

`pyak == py auto key`

Before you run make sure you have python3 installed, and then install the package in developer mode:

`pip3 install pyak`

example to press shift key every 15 minutes during work hour when slack is running：

`pyak 900 -k shift -t 8:00 17:00 -p slack`

>**Note:** For macos you may need to allow the terminal to control your keyboard by going to **System Preferences -> Security & Privacy -> Privacy -> Accessibility** and make sure terminal (or whatever console you are running it from) is selected

Detailed useage:

```
usage: auto_key.py [-h] [-k [KEY]] [-t START END] [-p [PROCESS]] [SECONDS]

Auto key presser

positional arguments:
  SECONDS               Interval between each key press in seconds.

optional arguments:
  -h, --help            show this help message and exit
  -k [KEY], --key [KEY]
                        Key to press, i.e. shift, f1. Defaults to shift key if
                        not provided
  -t START END, --time_active START END
                        If provided, the key will only be pressed during the
                        specified time. i.e -t 8:00 17:00
  -p [PROCESS], --process [PROCESS]
                        Name or regex of running process to trigger the key press.
```

安心摸鱼

### TODO
add windows logging support
