import tkinter
from tkinter import Label

def create_window():
    
    root = tkinter.Tk()
    root.title("Blackjack")
    root.geometry('800x450')

    #welcome_lb = Label(root, text= "Welcome to Blackjack", font= 'Arial 17 bold')

    deposit_lb = Label(root, text= "Deposit:", font= 'Arial 17 bold')
    bet_lb = Label(root, text= "Bet:", font= 'Arial 17 bold')

    deposit_lb.grid(row= 0, column= 0, sticky= "W")
    bet_lb.grid(row= 1, column= 0, sticky= "W")

    e1 = tkinter.Entry(root)
    e2 = tkinter.Entry(root)

    e1.grid(row= 0, column= 1)
    e2.grid(row= 1, column= 1)

    root.mainloop()