#! /usr/bin/env python
#
# GUI module generated by PAGE version 4.6
# In conjunction with Tcl version 8.6
#    Mar 06, 2016 10:02:16 PM
import sys
import serial

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

import DASH_support


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = Tk()
    root.title('DASH_GUI_v1')
    geom = "725x342+218+196"
    root.geometry(geom)
    DASH_support.set_Tk_var()
    w = DASH_GUI_v1(root)
    DASH_support.init(root, w)
    root.mainloop()

w = None


def create_DASH_GUI_v1(root, param=None):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = Toplevel (root)
    w.title('DASH_GUI_v1')
    geom = "725x342+218+196"
    w.geometry(geom)
    DASH_support.set_Tk_var()
    w_win = DASH_GUI_v1(w)
    DASH_support.init(w, w_win, param)
    return w_win


def destroy_DASH_GUI_v1():
    global w
    w.destroy()
    w = None


class DASH_GUI_v1:
    def __init__(self, master=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#d9d9d9' # X11 color: 'gray85'
        font10 = "-family {Segoe UI} -size 9 -weight normal -slant "  \
            "roman -underline 0 -overstrike 0"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.', background=_bgcolor)
        self.style.configure('.', foreground=_fgcolor)
        self.style.configure('.', font="TkDefaultFont")
        self.style.map('.', background=
                       [('selected', _compcolor), ('active', _ana2color)])
        master.configure(background="#d9d9d9")
        master.configure(highlightbackground="#d9d9d9")
        master.configure(highlightcolor="black")

        self.goBtn = Button(master)
        self.goBtn.place(relx=0.39, rely=0.73, height=24, width=47)
        self.goBtn.configure(activebackground="#d9d9d9")
        self.goBtn.configure(activeforeground="#000000")
        self.goBtn.configure(background=_bgcolor)
        self.goBtn.configure(disabledforeground="#a3a3a3")
        self.goBtn.configure(foreground="#000000")
        self.goBtn.configure(highlightbackground="#d9d9d9")
        self.goBtn.configure(highlightcolor="black")
        self.goBtn.configure(pady="0")
        self.goBtn.configure(text='''Go''')

        self.portLabel = Message(master)
        self.portLabel.place(relx=0.63, rely=0.11, relheight=0.07, relwidth=0.05)
        self.portLabel.configure(background=_bgcolor)
        self.portLabel.configure(foreground="#000000")
        self.portLabel.configure(highlightbackground="#d9d9d9")
        self.portLabel.configure(highlightcolor="black")
        self.portLabel.configure(text='''Port''')
        self.portLabel.configure(width=60)

        self.comSelect = ttk.Combobox(master)
        self.comSelect.place(relx=0.68, rely=0.12, relheight=0.06, relwidth=0.2)
        self.comSelect.configure(textvariable=DASH_support.combobox)
        self.comSelect.configure(takefocus="")

        self.txtCommand = Entry(master)
        self.txtCommand.place(relx=0.04, rely=0.73, relheight=0.06
                              , relwidth=0.34)
        self.txtCommand.configure(background="white")
        self.txtCommand.configure(disabledforeground="#a3a3a3")
        self.txtCommand.configure(font="TkFixedFont")
        self.txtCommand.configure(foreground="#000000")
        self.txtCommand.configure(highlightbackground="#d9d9d9")
        self.txtCommand.configure(highlightcolor="black")
        self.txtCommand.configure(insertbackground="black")
        self.txtCommand.configure(selectbackground="#c4c4c4")
        self.txtCommand.configure(selectforeground="black")
        self.txtCommand.focus_set()
        self.txtCommand.bind('<Return>', lambda e: DASH_support.goDASH(self))

        self.btnFwd = Button(master)
        self.btnFwd.place(relx=0.75, rely=0.5, height=44, width=54)
        self.btnFwd.configure(activebackground="#d9d9d9")
        self.btnFwd.configure(activeforeground="#000000")
        self.btnFwd.configure(background=_bgcolor)
        self.btnFwd.configure(command=lambda: DASH_support.fwd(1))
        self.btnFwd.configure(disabledforeground="#a3a3a3")
        self.btnFwd.configure(foreground="#000000")
        self.btnFwd.configure(highlightbackground="#9b9b9b")
        self.btnFwd.configure(highlightcolor="#000000")
        self.btnFwd.configure(pady="0")
        self.btnFwd.configure(takefocus="0")
        self.btnFwd.configure(text='''Forward''')

        self.btnLeft = Button(master)
        self.btnLeft.place(relx=0.6695, rely=0.635, height=44, width=54)
        self.btnLeft.configure(activebackground="#d9d9d9")
        self.btnLeft.configure(activeforeground="#000000")
        self.btnLeft.configure(background=_bgcolor)
        self.btnLeft.configure(command=lambda: DASH_support.lft(1))
        self.btnLeft.configure(disabledforeground="#a3a3a3")
        self.btnLeft.configure(foreground="#000000")
        self.btnLeft.configure(highlightbackground="#d9d9d9")
        self.btnLeft.configure(highlightcolor="black")
        self.btnLeft.configure(pady="0")
        self.btnLeft.configure(takefocus="0")
        self.btnLeft.configure(text='''Left''')

        self.btnRvs = Button(master)
        self.btnRvs.place(relx=0.75, rely=0.77, height=44, width=54)
        self.btnRvs.configure(activebackground="#d9d9d9")
        self.btnRvs.configure(activeforeground="#000000")
        self.btnRvs.configure(background=_bgcolor)
        self.btnRvs.configure(command=lambda: DASH_support.rvrs(1))
        self.btnRvs.configure(disabledforeground="#a3a3a3")
        self.btnRvs.configure(foreground="#000000")
        self.btnRvs.configure(highlightbackground="#d9d9d9")
        self.btnRvs.configure(highlightcolor="black")
        self.btnRvs.configure(pady="0")
        self.btnRvs.configure(takefocus="0")
        self.btnRvs.configure(text='''Reverse''')

        self.btnRight = Button(master)
        self.btnRight.place(relx=0.8305, rely=0.635, height=44, width=54)
        self.btnRight.configure(activebackground="#d9d9d9")
        self.btnRight.configure(activeforeground="#000000")
        self.btnRight.configure(background=_bgcolor)
        self.btnRight.configure(command=lambda: DASH_support.rght(1))
        self.btnRight.configure(disabledforeground="#a3a3a3")
        self.btnRight.configure(foreground="#000000")
        self.btnRight.configure(highlightbackground="#d9d9d9")
        self.btnRight.configure(highlightcolor="black")
        self.btnRight.configure(pady="0")
        self.btnRight.configure(takefocus="0")
        self.btnRight.configure(text='''Right''')

        self.btnStop = Button(master)
        self.btnStop.place(relx=0.75, rely=0.635, height=44, width=54)
        self.btnStop.configure(activebackground="#d9d9d9")
        self.btnStop.configure(activeforeground="#000000")
        self.btnStop.configure(background=_bgcolor)
        self.btnStop.configure(command=lambda: DASH_support.stop(1))
        self.btnStop.configure(disabledforeground="#a3a3a3")
        self.btnStop.configure(foreground="#000000")
        self.btnStop.configure(highlightbackground="#9b9b9b")
        self.btnStop.configure(highlightcolor="#000000")
        self.btnStop.configure(pady="0")
        self.btnStop.configure(takefocus="0")
        self.btnStop.configure(text='''Stop''')
        self.btnStop.configure(width=54)

        self.listBox = ScrolledListBox(master)
        self.listBox.place(relx=0.04, rely=0.03, relheight=0.65, relwidth=0.45)
        self.listBox.configure(background="white")
        self.listBox.configure(font="TkTextFont")
        self.listBox.configure(foreground="black")
        self.listBox.configure(highlightbackground="#d9d9d9")
        self.listBox.configure(highlightcolor="black")
        # self.listBox.configure(insertbackground="black")
        self.listBox.configure(selectbackground="#c4c4c4")
        self.listBox.configure(selectforeground="black")
        self.listBox.configure(takefocus="0")
        self.listBox.configure(width=244)
        # self.listBox.configure(wrap=WORD)

        self.connectCOM = Button(master)
        self.connectCOM.place(relx=0.885, rely=0.115, height=24, width=67)
        self.connectCOM.configure(activebackground="#d9d9d9")
        self.connectCOM.configure(activeforeground="#000000")
        self.connectCOM.configure(background=_bgcolor)
        self.connectCOM.configure(command=lambda: DASH_support.conCOM(self))
        self.connectCOM.configure(disabledforeground="#a3a3a3")
        self.connectCOM.configure(foreground="#000000")
        self.connectCOM.configure(highlightbackground="#d9d9d9")
        self.connectCOM.configure(highlightcolor="black")
        self.connectCOM.configure(pady="0")
        self.connectCOM.configure(text='''Connect''')
        self.connectCOM.configure(width=67)

        self.portScan = Button(master)
        self.portScan.place(relx=0.885, rely=0.04, height=24, width=67)
        self.portScan.configure(activebackground="#d9d9d9")
        self.portScan.configure(activeforeground="#000000")
        self.portScan.configure(background=_bgcolor)
        self.portScan.configure(command=lambda: DASH_support.portScan(self))
        self.portScan.configure(disabledforeground="#a3a3a3")
        self.portScan.configure(foreground="#000000")
        self.portScan.configure(highlightbackground="#d9d9d9")
        self.portScan.configure(highlightcolor="black")
        self.portScan.configure(pady="0")
        self.portScan.configure(text='''Scan Ports''')
        self.portScan.configure(width=67)

        self.dutyCycle = Scale(master)
        self.dutyCycle.place(relx=0.53, rely=0.03, relwidth=0.0, relheight=0.92
                             , width=45)
        self.dutyCycle.configure(activebackground="#d9d9d9")
        self.dutyCycle.configure(background=_bgcolor)
        self.dutyCycle.configure(font=font10)
        self.dutyCycle.configure(foreground="#000000")
        self.dutyCycle.configure(from_="100.0")
        self.dutyCycle.configure(highlightbackground="#d9d9d9")
        self.dutyCycle.configure(highlightcolor="black")
        self.dutyCycle.configure(length="310")
        self.dutyCycle.configure(to="0.0")
        self.dutyCycle.configure(troughcolor="#d9d9d9")

        self.menubar = Menu(master, bg=_bgcolor, fg=_fgcolor)
        master.configure(menu = self.menubar)

        self.goBtn.configure(command=lambda: DASH_support.goDASH(self))
        self.txtCommand.bind('<Key-Up>', lambda e: DASH_support.fwd(1))
        self.txtCommand.bind('<KeyRelease-Up>', lambda e: DASH_support.stop(1))
        self.txtCommand.bind('<Key-Left>', lambda e: DASH_support.lft(1))
        self.txtCommand.bind('<KeyRelease-Left>', lambda e: DASH_support.stop(1))
        self.txtCommand.bind('<Key-Down>', lambda e: DASH_support.rvrs(1))
        self.txtCommand.bind('<KeyRelease-Down>', lambda e: DASH_support.stop(1))
        self.txtCommand.bind('<Key-Right>', lambda e: DASH_support.rght(1))
        self.txtCommand.bind('<KeyRelease-Right>', lambda e: DASH_support.stop(1))


# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        # self.configure(yscrollcommand=self._autoscroll(vsb),
        #    xscrollcommand=self._autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = Pack.__dict__.keys() | Grid.__dict__.keys() \
                  | Place.__dict__.keys()
        else:
            methods = Pack.__dict__.keys() + Grid.__dict__.keys() \
                  + Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)


def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        return func(cls, container, **kw)
    return wrapped


class ScrolledListBox(AutoScroll, Listbox):
    '''A standard Tkinter Text widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        Listbox.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

if __name__ == '__main__':
    vp_start_gui()



