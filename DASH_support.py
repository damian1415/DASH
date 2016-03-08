#! /usr/bin/env python
#
# Support module generated by PAGE version 4.6
# In conjunction with Tcl version 8.6
#    Mar 06, 2016 10:02:21 PM


import sys
import DASH
import serial
import glob
import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

BT = serial.Serial()


def set_Tk_var():
    # These are Tk variables used passed to Tkinter and must be
    # defined before the widgets using them are created.
    global combobox
    combobox = StringVar()


def serial_ports():
    """ Lists serial port names

        :raises EnvironmentError:
            On unsupported or unknown platforms
        :returns:
            A list of the serial ports available on the system
    """
    if sys.platform.startswith('win'):
        ports = ['COM%s' % (i + 1) for i in range(256)]
    elif sys.platform.startswith('linux') or sys.platform.startswith('cygwin'):
        # this excludes your current terminal "/dev/tty"
        ports = glob.glob('/dev/tty[A-Za-z]*')
    elif sys.platform.startswith('darwin'):
        ports = glob.glob('/dev/tty.*')
    else:
        raise EnvironmentError('Unsupported platform')

    result = []
    for port in ports:
        try:
            s = serial.Serial(port)
            s.close()
            result.append(port)
        except (OSError, serial.SerialException):
            pass
    return result


def conCOM(p1):
    ports = p1.comSelect.get()
    BT.port = ports
    BT.baudrate = 115200
    BT.open()
    print(BT.isOpen())
    sys.stdout.flush()


def portScan(p1):
    ports = serial_ports()
    p1.comSelect.configure(values=ports)
    p1.comSelect.current(0)
    sys.stdout.flush()


def rght(p1):
    print('DASH_support.rght')
    sys.stdout.flush()


def rvrs(p1):
    print('DASH_support.rvrs')
    sys.stdout.flush()


def fwd(p1):
    print('DASH_support.fwd')
    sys.stdout.flush()


def lft(p1):
    print('DASH_support.lft')
    sys.stdout.flush()


def stop(p1):
    print('DASH_support.stop')
    sys.stdout.flush()


def init(top, gui, arg=None):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None


def match_cmds(p1):
    matched = [c for c in cmds if c.startswith(p1)]
    if matched:
        return matched[0]


def goDASH(p1):
    p1.listBox.tag_configure('color', foreground='#00aa00')
    p1.listBox.insert(END, ">" + p1.txtCommand.get(), 'color')
    p1.listBox.tag_configure('color1', foreground='#aa0000')
    p1.listBox.insert(END, " Power: " + str(p1.dutyCycle.get()) + "\n", 'color1')
    cmds = ["forward", "right", "left", "stop", "revers", "set"]
    cmd = p1.txtCommand.get()
    if cmd.lower() == 'set':
        BT.write(str(unichr(p1.dutyCycle.get())))
        print(p1.dutyCycle.get())
    elif cmd.lower() == 'forward':
        print('Forward')
    elif cmd == 'Reverse':
        print('Reverse')
    elif cmd == 'Right':
        print('Right')
    elif cmd == 'Left':
        print('Left')
    p1.btnFwd.focus_set()
    sys.stdout.flush()


if __name__ == '__main__':
    import DASH
    DASH.vp_start_gui()
