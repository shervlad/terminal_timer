import time
import sys
import pyfiglet
from playsound import playsound
import curses
from threading import Thread

def play_sound():
    playsound('./timer_alarm.mp3')

def timer(screen):
    curses.start_color()
    curses.use_default_colors()
    curses.init_pair(1, curses.COLOR_GREEN,  -1)
    curses.init_pair(2, curses.COLOR_YELLOW, -1)
    curses.init_pair(3, curses.COLOR_RED,    -1)

    curses.curs_set(0)

    seconds = 60

    if len(sys.argv) > 1:
        seconds = int(sys.argv[1])


    while seconds > 0:
        (h,w) = screen.getmaxyx()
        screen.clear()

        color = curses.color_pair(1)
        if(seconds <= 20):
            color = curses.color_pair(2)

        text = pyfiglet.figlet_format(str(seconds), font="doh")
        if(seconds > 10):
            y = (h - (len(text.split("\n"))))//2
            for line in text.split("\n"):
                x = (w-len(line))/2
                try:
                    screen.insstr(y, x, line, color)
                except:
                    pass
                y += 1
            screen.refresh()
            seconds -= 1
            curses.napms(1000)
        else:
            y = (h - (len(text.split("\n"))))//2
            color = curses.color_pair(3)
            for line in text.split("\n"):
                x = (w-len(line))/2
                try:
                    screen.insstr(y, x, line, color)
                except:
                    pass
                y += 1
            screen.bkgd(' ',curses.A_REVERSE)
            screen.refresh()
            curses.napms(100)
            screen.bkgd(' ',curses.color_pair(3))
            screen.refresh()
            curses.napms(900)

            #color = curses.color_pair(3)
            #y = (h - (len(text.split("\n"))))//2
            #for line in text.split("\n"):
            #    x = (w-len(line))/2
            #    try:
            #        screen.insstr(y, x, line, color)
            #    except:
            #        pass
            #    y += 1

            screen.refresh()
            seconds -= 1

    screen.clear()
    screen.refresh()

    text = pyfiglet.figlet_format("STOP", font="alphabet")
    y = (h - (len(text.split("\n"))))//2
    for line in text.split("\n"):
        x = (w-len(line))/2
        try:
            screen.insstr(y, x, line, color)
        except:
            pass
        y += 1
    screen.refresh()
    T = Thread(target=play_sound)
    T.start()

def main(screen):
    timer(screen)
    restart=True
    while(True):
        ch = screen.getkey()
        if(ch == 'r'):
            timer(screen)
        elif(ch == 'c'):
            break
curses.wrapper(main)
