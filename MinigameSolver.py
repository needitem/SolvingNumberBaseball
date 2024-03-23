import random
import tkinter as tk
from tkinter import messagebox
class MinigameSolverGUI:
    def __init__(self, master):
        self.master = master
        master.title("Minigame Solver")

        self.guess_label = tk.Label(master, text="Guess: ")
        self.guess_label.pack()

        self.balls_label = tk.Label(master, text="Balls: ")
        self.balls_label.pack()

        self.balls_entry = tk.Entry(master)
        self.balls_entry.pack()

        self.strikes_label = tk.Label(master, text="Strikes: ")
        self.strikes_label.pack()

        self.strikes_entry = tk.Entry(master)
        self.strikes_entry.pack()

        self.guess_button = tk.Button(master, text="Guess", command=self.make_guess)
        self.guess_button.pack()

        self.possible_numbers = generate_possible_numbers()
        self.make_guess(first_guess=True)

    def make_guess(self, first_guess=False):
        if first_guess:
            guess = make_guess(self.possible_numbers)
            self.guess_label.config(text="Guess: " + guess)
        
        if len(self.possible_numbers) > 1:
            guess = random.choice(self.possible_numbers)
            self.guess_label.config(text="Guess: " + guess)
        elif len(self.possible_numbers) == 1:
            messagebox.showinfo("Result", "The number you called is: " + self.possible_numbers[0])
        else:
            messagebox.showinfo("Result", "No valid number found.")

        if not first_guess:
            balls = int(self.balls_entry.get())
            strikes = int(self.strikes_entry.get())
            self.possible_numbers = filter_possible_numbers(self.possible_numbers, guess, balls, strikes)

def generate_possible_numbers():
    possible_numbers = []
    for i in range(10000):
        number_str = str(i).zfill(4)  # Pad zeros to make it 4 digits
        if len(set(number_str)) == 4:  # Ensure all digits are unique
            possible_numbers.append(number_str)
    return possible_numbers

def filter_possible_numbers(possible_numbers, guess, balls, strikes):
    remaining_numbers = []
    for number in possible_numbers:
        temp_balls = 0
        temp_strikes = 0
        for i in range(4):
            if number[i] == guess[i]:
                temp_strikes += 1
            elif number[i] in guess:
                temp_balls += 1
        if temp_balls == balls and temp_strikes == strikes:
            remaining_numbers.append(number)
    return remaining_numbers

def make_guess(possible_numbers):
    return random.choice(possible_numbers)

root = tk.Tk()
my_gui = MinigameSolverGUI(root)
root.mainloop()
