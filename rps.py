from tkinter import *
import tkinter.font as font

window = Tk()
window.geometry("600x400")
window.configure(background = "Light Grey")

l1 = Label(window, text = "Rock Paper Scissors", fg = "black", font = ("Arial", 35) )
l1.pack(padx = 15, pady = 10)

l2 = Label(window, text = "Let's start the game...", fg = "green", font = ("Arial", 15))
l2.pack(padx = 15, pady = 35)

import_frame = Frame(window)
import_frame.pack()

player_option = Label(import_frame, text = "Your Options:", fg = "Black", font = ("Arial", 10))
player_option.grid(row = 0, column = 0)

rock = Button(import_frame, text = "Rock", bg = "pink", fg = "Black", padx = 20, pady = 5)
rock.grid(row = 1, column = 1, padx = 15, pady = 10)

paper = Button(import_frame, text = "Paper", bg = "grey", fg = "Black", padx = 20, pady = 5)
paper.grid(row = 1, column = 2, padx = 15, pady = 10)

scissors = Button(import_frame, text = "Scissors", bg = "blue", fg = "Black", padx = 20, pady = 5)
scissors.grid(row = 1, column = 3, padx = 15, pady = 10)

score = Label(import_frame, text = "Score:", fg = "Black", font = ("Arial", 10))
score.grid(row = 2, column = 0)

p_choice = Label(import_frame, text = "Your Selection")
p_choice.grid(row = 3, column = 1)

c_choice = Label(import_frame, text = "Computer selection")
c_choice.grid(row = 3, column = 2)

p_score = Label(import_frame, text = "Player score") # Player score
p_score.grid(row = 4, column = 1)

c_score = Label(import_frame, text = "Computer Score") # computer score
c_score.grid(row = 4, column = 2)






window.mainloop()