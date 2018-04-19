from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master, bg='blue')
        self.master = master # main window/master widget
        self.init__window() # not a function that exists - created below

    def init__window(self):
        self.master.title('Initiative Tracker')
        self.pack(fill=BOTH, expand=1)

        # quitButton = Button(self, text='Q U I T', command=self.client_exit)
        # quitButton.place(x=0, y=0)
        startMessage = Label(self, text='Press \'Roll for initiative!\' when ready')
        startMessage.pack(fill=BOTH, pady=30)

        startButton = Button(self, text='Roll for initiative!', command=lambda : self.roll__window
        startButton.pack(fill=Y, pady=55)



        # initialize menu
        menu = Menu(self.master) # menu of the main window
        self.master.config(menu=menu)

        # create file menu button
        file = Menu(menu)
        file.add_command(label='Exit', command=self.client_exit) # command added to file
        menu.add_cascade(label='File', menu=file) # add file to menu. Cascade is the list layout

        # create edit menu button
        # edit = Menu(menu)
        # edit.add_command(label='Undo')
        # menu.add_cascade(label='Edit', menu=edit)

    def roll__window(self):
        self.master.title('Everybody roll!')
        self.pack(fill=BOTH, expand=1)
        msg = Label(self, text='HELLO')
        msg.pack()

    def client_exit(self):
        exit()

root = Tk() # root window
root.geometry('400x300')
app = Window(root)

root.mainloop() # initializes window




# def start_window():
#     # Top window
#     win=Tk()
#     win.title('Ready... fight!')
#     win.geometry('200x200')
#
#     # functions
#     def hello():
#         print('Hello!')
#
#     def set_ally_init():
#         # Window/frame
#         win.destroy()
#         win_ally=Tk()
#         win_ally.title('Ally initiative')
#         # frame_ally = Frame(win_ally)
#
#         # Widgets/labels
#         title = Label(win_ally, text='Enter Ally Initiative', bg='#66e006')
#         pc_list = Listbox(win_ally, height=4, fg='#55C100', bg='#e7e7e7')
#         pc_list.insert(END, 'Ivellios')
#         pc_list.insert(END, 'Goodan')
#         pc_list.insert(END, 'Turalyon')
#         pc_list.insert(END, 'Vitarin')
#
#         # Setting everything into window
#         title.pack()
#         pc_list.pack()
#         # ally_frame.pack()
#
#
#         ally_win.mainloop()
#
#     # setting everything
#     # menubar = Menu(win, image='polygons.jpg')
#     # menubar.add_command(label='Print Hello', command=hello)
#     start_button = Button(win, text='Begin Battle', command=set_ally_init)
#     start_button.grid(padx=45, pady=40)
#     # win.config(menu=menubar)
#     win.mainloop()
#
# def main():
#     start_window()
#     # win=Tk()
#     # v = StringVar()
#     # e = Entry(win, textvariable=v)
#     # e.pack()
#     # def get_text():
#     #     print(v.get())
#     # def set_text():
#     #     v.set('This is set from the program')
#     # bget = Button(win, text='get', command=get_text)
#     # bset = Button(win, text='set', command=set_text)
#     # bset.pack()
#     # bget.pack(side=RIGHT)
#
#     # Listbox
#     # lb = Listbox(win, height=3)
#     # lb.pack()
#     # lb.insert(END, 'I')
#     # lb.insert(END, 'Love')
#     # lb.insert(END, 'Leah')
#     # sb = Scrollbar(win, orient=VERTICAL)
#     # sb.pack(side=LEFT, fill=Y)
#     # sb.configure(command=lb.yview)
#     # lb.configure(yscrollcommand=sb.set)
#
#     # win.mainloop()
#
# if __name__ == '__main__':
#     main()
