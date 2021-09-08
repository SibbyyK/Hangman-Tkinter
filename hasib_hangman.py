from tkinter import *
from random import choice


class Hangman:  # hangman
    wordlist = []  # wordlist list

    def __init__(self, root):
        with open("words.txt") as p:  # opens word list
            for word in p:  # for loop that takes all the words in the txt file
                # and appends it to the word list and strips any spaces
                self.wordlist.append(word.strip())

        self.root = root
        root.title("Hangman")  # title

        self.lives = 0  # how many they have starting from 0
        # turns all words into Upper Case
        self.word = choice(self.wordlist).upper()
        # the guessing platform for the word (_ _ _)
        self.underscores = ["_"] * len(self.word)
        self.guess = ""  # users guess
        self.guessed = "GUESSES: "  # the letters a user has guessed
        # starting image
        self.hangmanimg = PhotoImage(file="images/hangman01.png")
        print(self.word)

        # Starting Image placement -------------------------------------
        # makes canvas for the images
        self.imghangman = Canvas(root, width=600, height=500)
        # places img in the middle and spans it
        self.imghangman.grid(row=0, columnspan=3)
        self.imghangman.create_image(340, 240, image=self.hangmanimg)

        # Underling for each guessed letter/character ------------------------
        self.wordblank = StringVar()  # make it a string
        # makes underscores in length with words ('fire' 4 "_")
        self.wordblank.set(" _ " * len(self.word))
        # makes Label
        self.wordblanklabel = Label(root, textvariable=self.wordblank)
        # placement where the Label is
        self.wordblanklabel.grid(row=1, column=0, sticky=W+E)

        # Guess here Label -------------------------------------
        self.enterhere = Label(root, text="ENTER LETTER: ")  # label with text
        self.enterhere.grid(row=1, column=1, sticky=W+E)  # placement of label

        # Entry for correct letters ----------------------------
        # The validate method is called whenever user edit the entry widget.
        charc = root.register(self.validate)
        # The“key”value specifies that validation occurs whenever any keystroke
        # the "%P" means that the function will be passed the new value
        self.entry = Entry(root, validate="key", validatecommand=(charc, "%P"))
        # Placement of the Label for the Entry
        self.entry.grid(row=1, columnspan=4, column=2, sticky=W+E)

        # Shows the guessed letters that has been guessed --------------------
        self.guesses = StringVar()  # guess is a string
        # sets guessedwords//userinput into guesed string
        self.guesses.set(self.guessed)
        # sets the guessed words here (from the code above)
        self.guesseslabel = Label(root, textvariable=self.guesses)
        self.guesseslabel.grid(row=2, column=3, sticky=W+E)

        # adds a restart button ------------------------------------------
        # reset function on button press
        self.restartgame = Button(root, text="Restart", command=self.reset)
        self.restartgame.grid(row=2, column=1, sticky=W+E)

        # Enter button - and does the check guess function -------------------
        # check guess funciton on button press
        self.enterbutton = Button(root, text="Enter", command=self.checkguess)
        self.enterbutton.grid(row=2, column=2, sticky=W+E)

        # Quit Button -------------------------------
        self.quit = Button(root, text="Exit", command=self.root.destroy)
        self.quit.grid(row=2, column=0, sticky=W+E)

    # Image configuration ----------------------------------
    # This function updates the image depending on the lives
    def imagerotation(self):
        image_lst = ["images/hangman01.png",
                     "images/hangman02.png",
                     "images/hangman03.png",
                     "images/hangman04.png",
                     "images/hangman05.png",
                     "images/hangman06.png",
                     "images/hangman07.png"]
        self.lives = self.lives % len(image_lst)
        self.images = PhotoImage(file=image_lst[self.lives])
        self.imghangman.create_image(340, 240, image=self.images)

        # the validation for the entry//user input
    def validate(self, text):
        # Validates input into entry field.
        # if not user input is not a text - return true
        # returns user input as a text
        if not text:
            return True
        else:
            # else if user input is a text set it to an upper case
            self.guess = text.upper()
            return True

    # Resets the entire game
    def reset(self):
        self.lives = 0  # reset lives back to zero
        self.imagerotation()  # sets hangman
        # chooses word from wordlist and .upper makes it CAPITALS
        self.word = choice(self.wordlist).upper()
        # sets the blank spaces between each underscore
        self.wordblank.set(" _ " * len(self.word))
        # sets the underscores again
        self.underscores = ["_"] * len(self.word)
        self.guessed = "GUESSES: "  # changes this back to "Guesses"
        self.guesses.set(self.guessed)  # resets the guessed label
        print(self.word)  # shows answer in console word

    def checkguess(self):
        if self.guess in self.guessed[8]:
            self.entry.delete(0, END)  # deletes entry
            return
        self.guessed += self.guess  # adds guessed words/letters to guess
        self.guesses.set(self.guessed)  # sets guesses to guessed words/letters
        if self.guessed[-1] not in self.word:  # if guess is not part of word
            self.lives += 1  # add one life
            self.imagerotation()  # change image
        else:
            self.formword()  # forms letter on the underscores

        if "_" in self.underscores:  # if there are still remaining underscores
            if self.lives == 6:  # if lives is 6 game ends
                self.wordblank.set(self.word)  # show the word
                self.guesses.set("YOU LOSE.")  # display you lose

        # if there are no more underscores in and the word
        # self.underscores is equal to the word
        if ''.join(self.underscores) == self.word:
            self.guesses.set("You WIN!")  # then display you win
            self.wordblank.set(self.word)  # show the word

        self.entry.delete(0, END)  # reset entry

    # This function updates the display of underscored word
    def formword(self):
        # if the guessed letter is in the word then
        if self.guessed[-1] in self.word:
            # for index/the word, the letter/string is
            # enumerated by each charecter and is adds onto the underscore
            for index, letter in enumerate(self.underscores):
                # if the word index/letter is equal to the users guess
                if self.word[index] == self.guessed[-1]:
                    self.underscores[index] = self.word[index]
        # sets the underlines/wordblanks to the underscores and displays it
        self.wordblank.set(str(self.underscores))


# main function that runs entire game
def main():
    root = Tk()  # tk window

    game = Hangman(root)  # creates class object

    root.mainloop()  # runs code


main()
