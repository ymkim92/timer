This is very simple timer working in Linux.
I have tested this in the Lubuntu 19.04 and Python 3.7.
This project uses ``poetry``.

# Features
- Print how many time is left
- Play sound at the end of timer
- Show up system notification at the end of timer

# Requirements
You need python3, mplayer and notify-send.
For the last two commands, you can install with this command:
```
$ sudo apt install mplayer libnotify-bin
```

# Installation

```
$ pip install https://github.com/ymkim92/timer/archive/master.zip
```

# Usage
```
$ pytimer
usage: pytimer [-h] minutes
pytimer: error: the following arguments are required: minutes

$ pytimer 30

```

In the example above, it will print current time and display how many time left.
When it expires, it will play a sound and show up its notification.
