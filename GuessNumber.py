# Guess my number game this restarts so multiple games can be played
# User must attempt to guess randomly selected number within a range in fewest possible attempts
# found this on the internet 8-6-19 now need to modify to my specs first add number of guesses and compile program
# 
# trying 10-3-19 to increase font size and font.py font2.py and getFont.py work and may help

from tkinter import *
import tkinter.font
import random

class Application(Frame):
    """A GUI application which which generates random number and gets user input"""
    
    def __init__(self, master): #initialize newly created Application object
        """Initialize the frame"""
        Frame.__init__(self, master) # super(Application, self).__init__(master) in python 3
        self.grid()
        self.create_widgets()
        self.number = random.randint(1, 100)
        self.numberOfGuesses = 0
        

    def create_widgets(self):
        """Get user inputs"""
        # create instruction label
         #Label(master, text="Helvetica", font=("Helvetica", 16))
        Label(self, text = "I'm thinking of a number between 1 and 100.", font=("Helvetica", 16)).grid(row = 0, column = 0, sticky = W)
        Label(self, text = "Try and guess it in 8 or fewer attempts if possible!", font=("Helvetica", 16)).grid(row = 1, column = 0, sticky = W)

        # create guess input prompt label and entry
        Label(self, text = "Enter your guess in the box: ", font=("Helvetica", 16)).grid(row = 2, column = 0, sticky = W)
        self.guess_ent = Entry(self, font=("Helvetica", 15))
       
        self.guess_ent.grid(row = 2, column = 1, columnspan =2, sticky = W)

        # create start game prompt label and submit button
        Label(self, text="Press enter or the 'Submit' button to start the game!", font=("Helvetica", 16)).grid(row=3, column=0, sticky=W)
        Button(self, text = "Submit",font=("Helvetica", 14), command = self.run_game).grid(row = 3, column = 1, sticky = W)

        Label(self, text="Press 'Play Again!' button to restart the game!", font=("Helvetica", 16)).grid(row=4, column=0, sticky=W)
        Button(self, text="Play Again!", font=("Helvetica", 14), command = self.start_over).grid(row=4, column=1, sticky=W)

        # create computer feedback text box
        self.text = Text(self, font=("Helvetica", 15), width = 75, height = 10, wrap = WORD)
        self.text.grid(row = 5, column = 0, columnspan = 4)

        self.master.bind('<Return>', self.parse)
        self.grid()


    #need to delete guess
    def start_over(self):
        self.guess_ent.delete(0, END)
        self.text.delete(0.0, END)
        self.number = random.randint(0, 101)
        self.numberOfGuesses = 0

    def validate(self):
        global guess
        try:
            guess = int(self.guess_ent.get())
            if not guess > 1 or not guess <= 99:
                guess = str(guess)
                self.guess_ent.delete(0, END)
                self.text.delete(0.0, END)
                
                print_text = "Ho Ho HO, You guessed %s  Please enter a number between 1 and 100!" % guess
                self.text.insert(0.0, print_text, )
                self.master.bind('<Return>', self.parse)
            else:
                self.goForIt()  
        except ValueError:
            guess = str(self.guess_ent.get())
            self.guess_ent.delete(0, END)
            self.text.delete(0.0, END)
            
            print_text = "HA! You guessed %s. Please enter a number for your guess!" % guess 
            self.text.insert(0.0, print_text)
            self.master.bind('<Return>', self.parse)
        

    def run_game(self):
        """Generate number and get user input"""
        self.validate()

    def goForIt(self):
        self.numberOfGuesses +=1

        if guess != self.number:
            print_text = "You guessed {0}.".format(guess)
#            print_text += "\nMy number is {0}".format(self.number)

            if guess > self.number:
                print_text += " That's too high. Guess lower..."
            elif guess < self.number:
                print_text += " That's too low. Guess higher..."

            self.text.delete(0.0, END)
            self.text.insert(0.0, print_text)

            self.guess_ent.delete(0, END)
        else:
            print_text = "You guessed {0}.".format(guess)
            print_text += "\n\nCongratulation that was my number! "
            print_text += "\n\nYou guessed it in only {0} guesses!  Well done!".format(self.numberOfGuesses)
            self.text.delete(0.0, END)
            self.text.insert(0.0, print_text)
            # create start game over prompt label and Play Again! button

    def parse(self, event):
        self.run_game()
           
            

root = Tk()
root.title("Guess my number game!")
app = Application(root)
root.mainloop()


