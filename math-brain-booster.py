import ctypes
import random
import threading
import time
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk as ttk


class Application:
    def __init__(self):
        self.randomizer = 0
        self.answer = 0
        self.counter = 0
        self.t0 = time.perf_counter()
        self.mindigit = 1  # 最小桁数
        self.maxdigit = 3  # 最大桁数
        self.minnum = 10**self.mindigit - 1
        self.maxnum = 10**self.maxdigit - 1

        self.window()

    def window(self):
        def info(title, content):
            tkinter.messagebox.showinfo(title, content)

        def close(event):
            root.destroy()

        def next():
            entry_answer.delete(0, tkinter.END)
            tkstr_counter.set("Count\t{}".format(self.counter))
            self.counter += 1

            rand1 = random.randint(self.minnum, self.maxnum)
            rand2 = random.randint(self.minnum, self.maxnum)

            tkint_num1.set(rand1)
            tkint_num2.set(rand2)
            self.randomizer = round(random.randrange(0, 2))
            if self.randomizer == 0:
                tkstr_symbol.set("+")
                self.answer = rand1 + rand2
            elif self.randomizer == 1:
                tkstr_symbol.set("-")
                self.answer = rand1 - rand2
            else:
                pass

        def check():
            while True:
                try:
                    int(entry_answer.get())
                    if int(entry_answer.get()) == self.answer:
                        next()
                    else:
                        pass
                except:
                    pass

                time.sleep(10 / 1000)

        def timer():
            self.t0 = time.perf_counter()
            while True:
                dt = round(time.perf_counter() - self.t0)
                if dt // 60 < 10:
                    m = "0{}".format(dt // 60)
                else:
                    m = "{}".format(dt // 60)
                if dt % 60 < 10:
                    s = "0{}".format(dt % 60)
                else:
                    s = "{}".format(dt % 60)
                tkstr_timer.set("Time\t{}:{}".format(m, s))

                time.sleep(1 / 60)

        def reset():
            self.counter = 0
            self.t0 = time.perf_counter()
            next()
            quit()

        def func2(event):
            thread2 = threading.Thread(target=reset)
            thread2.start()

        root = tkinter.Tk()
        root.title("Math Brain Booster v0.0")
        root.geometry("+10+10")
        root.resizable(False, False)

        root.withdraw()

        icondata = """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
drDvkp8JAGbXG5s2aY3TJ5YNg5jPYQIgO36+sNJTEhSRRiVWT3xGpH2fXqA1C2i4
FBqRjjVS69X6m59OuiKg4enU3g/I9QhAg7qGW+G5co2PFx8ydzTWTHZhUhRgNZMn
U3SwxObzbJn/LKwzOxrpqHvnQZaH+SoRE2E5U+TDm5/zwkR0x3sAJTD+X7fv87jq
BU+qD9KbM+8bANfzsS0pGpEtEU4Wax5XPloiZfnUD4m0boJUHJ+CZ7CM8Chf5dfX
75Js1dVm9JdqHiXfwhhhs1jjrRv3GI34WFJ/V9g8M5Crerhio04F9bwtjFUcCgAG
5e8Xv5v59uV/vI/vnUNEio60vaVtpsZw6zoEpOBAvgtdASoulN22Q/KN8wPqVPCr
RR/0b362nDFjcfYrPeWwr1/8MyIy7vrez4AfgKR7aacvUR/1vG3Qv4L8Eciu/ml/
J8V7BgBg9kdXAIwYewLVFF0cmN+rs554vBgwVhHRbVT91Xd/2geah3Ioh3Ioh3Io
X0r5P3+6oSQnIHMFAAAAJXRFWHRkYXRlOmNyZWF0ZQAyMDE3LTAzLTMwVDEyOjQ2
OjIyKzAyOjAw0Es1hQAAACV0RVh0ZGF0ZTptb2RpZnkAMjAxNy0wMy0zMFQxMjo0
NjoyMiswMjowMKEWjTkAAABGdEVYdHNvZnR3YXJlAEltYWdlTWFnaWNrIDYuNy44
LTkgMjAxNi0wNi0xNiBRMTYgaHR0cDovL3d3dy5pbWFnZW1hZ2ljay5vcmfmvzS2
AAAAGHRFWHRUaHVtYjo6RG9jdW1lbnQ6OlBhZ2VzADGn/7svAAAAGHRFWHRUaHVt
Yjo6SW1hZ2U6OmhlaWdodAA1MTLA0FBRAAAAF3RFWHRUaHVtYjo6SW1hZ2U6Oldp
ZHRoADUxMhx8A9wAAAAZdEVYdFRodW1iOjpNaW1ldHlwZQBpbWFnZS9wbmc/slZO
AAAAF3RFWHRUaHVtYjo6TVRpbWUAMTQ5MDg3MDc4Mk5d7xIAAAATdEVYdFRodW1i
OjpTaXplADE1LjVLQkL1fqs4AAAAVXRFWHRUaHVtYjo6VVJJAGZpbGU6Ly8uL3Vw
bG9hZHMvY2FybG9zcHJldmkva0dWNGRtMS8xMTk0LzE0OTA4ODYzMTEtMjgtY2Fs
Y3V0b3JfODI0OTUucG5ngnrAswAAAABJRU5ErkJggg=="""

        root.tk.call(
            "wm", "iconphoto", root._w, tkinter.PhotoImage(data=icondata)
        )

        menubar = tkinter.Menu(root, tearoff=False)

        menu1 = tkinter.Menu(menubar, tearoff=False)
        menu1.add_command(label="Exit", command=lambda: root.destroy())

        menu2 = tkinter.Menu(menubar, tearoff=False)

        menu3 = tkinter.Menu(menubar, tearoff=False)

        menubar.add_cascade(label="Files", menu=menu1)
        menubar.add_cascade(label="Edit", menu=menu2)
        menubar.add_cascade(label="View", menu=menu3)

        root.config(menu=menubar)

        inner = ttk.Frame(root)
        inner.grid(column=0, row=0, ipadx=0, ipady=0, padx=20, pady=(10, 20))

        coloumn0 = tkinter.Canvas(inner, width=100, height=0)
        coloumn1 = tkinter.Canvas(inner, width=80, height=0)
        coloumn2 = tkinter.Canvas(inner, width=100, height=0)
        coloumn3 = tkinter.Canvas(inner, width=80, height=0)
        coloumn4 = tkinter.Canvas(inner, width=200, height=0)
        coloumn0.grid(column=0, row=0)
        coloumn1.grid(column=1, row=0)
        coloumn2.grid(column=2, row=0)
        coloumn3.grid(column=3, row=0)
        coloumn4.grid(column=4, row=0)

        tkint_num1 = tkinter.IntVar()
        tkint_num2 = tkinter.IntVar()

        num1_display = ttk.Label(
            inner,
            textvariable=tkint_num1,
            font=("", 20, "bold"),
            anchor=tkinter.CENTER,
        )
        num1_display.grid(
            column=0,
            row=1,
            columnspan=1,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=20,
            pady=20,
        )
        num2_display = ttk.Label(
            inner,
            textvariable=tkint_num2,
            font=("", 20, "bold"),
            anchor=tkinter.CENTER,
        )
        num2_display.grid(
            column=2,
            row=1,
            columnspan=1,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=20,
            pady=20,
        )

        tkstr_symbol = tkinter.StringVar()
        symbol_display = ttk.Label(
            inner,
            textvariable=tkstr_symbol,
            font=("", 20, "bold"),
            anchor=tkinter.CENTER,
        )
        symbol_display.grid(
            column=1,
            row=1,
            columnspan=1,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=20,
            pady=20,
        )
        tkstr_symbol.set("+")

        equal_display = ttk.Label(
            inner, text="=", font=("", 20, "bold"), anchor=tkinter.CENTER
        )
        equal_display.grid(
            column=3,
            row=1,
            columnspan=1,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=20,
            pady=20,
        )

        entry_answer = ttk.Entry(inner, width=0, font=("", 20, "bold"))
        entry_answer.grid(
            column=4,
            row=1,
            columnspan=1,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=20,
            pady=20,
        )

        tkstr_timer = tkinter.StringVar()
        timer_display = ttk.Label(
            inner,
            textvariable=tkstr_timer,
            font=("", 16, "bold"),
            anchor=tkinter.CENTER,
        )
        timer_display.grid(
            column=0,
            row=2,
            columnspan=3,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        tkstr_counter = tkinter.StringVar()
        counter_display = ttk.Label(
            inner,
            textvariable=tkstr_counter,
            font=("", 16, "bold"),
            anchor=tkinter.CENTER,
        )
        counter_display.grid(
            column=0,
            row=3,
            columnspan=3,
            sticky=tkinter.W,
            ipadx=0,
            ipady=0,
            padx=10,
            pady=4,
        )

        button_reset = tkinter.Button(
            inner,
            text="Reset",
            width=0,
            font=("", 12, "bold"),
            anchor=tkinter.CENTER,
        )
        button_reset.grid(
            column=4,
            row=2,
            rowspan=2,
            sticky=tkinter.NSEW,
            ipadx=0,
            ipady=0,
            padx=20,
            pady=4,
        )
        button_reset.bind("<Button-1>", func2)

        root.bind("<Escape>", close)

        next()

        thread0 = threading.Thread(target=check)
        thread0.start()

        thread1 = threading.Thread(target=timer)
        thread1.start()

        root.deiconify()
        root.mainloop()

    """
    def settings(self):
        root = tkinter.Tk()
        root.title("Settings")
        root.geometry("+10+10")
        root.resizable(False, False)
        root.withdraw()

        inner = ttk.Frame(root)
        inner.grid(column=0, row=0, padx=20, pady=(10, 20))

        column0 = tkinter.Canvas(inner, width=200, height=0)
        column1 = tkinter.Canvas(inner, width=50, height=0)
        column2 = tkinter.Canvas(inner, width=200, height=0)
        column0.grid(column=0, row=0)
        column1.grid(column=1, row=0)
        column2.grid(column=2, row=0)

        label_difficluty = ttk.Label(
            inner,
            text="Difficulty",
            font=("", 12, "bold"),
            anchor=tkinter.CENTER,
        )
        label_difficluty.grid(column=0, row=1)
    """


if __name__ == "__main__":
    try:
        ctypes.windll.shcore.SetProcessDpiAwareness(True)
    except:
        pass

    Application()
