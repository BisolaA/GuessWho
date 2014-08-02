from tkinter import *

window = Tk()
window.wm_title("Guess Who (GUI)") # The title of the window.
window.geometry("100x50")  # The size of the window.

def Start():
    from tkinter import messagebox
    import random
    import time
    import os
    
    window.destroy()

    root = Tk() 
    root.wm_title("Guess Who (GUI)") # The title of the window.
    root.geometry("370x55")  # The size of the window.

    guesses = 5
    
    # database of options to guess from
    class student:
        def __init__(self,name,hair,eyes,height,gender,glasses):
            self.name = name
            self.hair = hair
            self.eyes = eyes
            self.height = height
            self.gender = gender
            self.glasses = glasses
    
    James = student("James","black","brown","tall","male","doesn't wear")
    Niall = student("Niall","brown","brown","tall","male","doesn't wear")
    Niles = student("Niles","ginger","blue","medium","male","doesn't wear")
    
    def passgame(): # function for setting guesses
        global guesses
        guesses-=1
        v.set(guesses)
        
        messagebox.showinfo("You passed!","The answer was {0}.".format(select[0].name)) # when you guess correctly
        root.destroy()
        
        if guesses == 0:
            messagebox.showinfo("You Lost!","You Lost, the game will close once you press OK. The answer was {0}".format(select[0].name)) # guess incorrectly
            root.destroy()
    
    people = [James, Niall, Niles]
    select = random.sample(people,1) #game randomly selects a person from database
    user = StringVar()

    #list of functions for clues

    def hairClue():
        messagebox.showinfo("Hair Clue", "Person has {0} hair.".format(select[0].hair))

    def eyeClue():
        messagebox.showinfo("Eye Clue", "Person has {0} eyes.".format(select[0].eyes))
    
    def heightClue():
        messagebox.showinfo("Height Clue", "This person can be described as {0}.".format(select[0].height))

    def genderClue():
        messagebox.showinfo("Gender Clue", "Person is a {0}.".format(select[0].gender))

    def glassesClue():
        messagebox.showinfo("Glasses Clue", "This person {0} glasses.".format(select[0].glasses))

    def check():
        global guesses
        ans = user.get()
        
        if len(ans) == 0:
            messagebox.showinfo("Type a guess","Type a guess!") # if user field is empty
        elif ans == select[0].name:
            messagebox.showinfo("Correct","You are correct well done!") # guess is correctd
            root.destroy()
        else:
            messagebox.showinfo("Wrong","Sorry you're wrong, try again") # guess is incorrect
            guesses-=1
            v.set(guesses)

            if guesses == 0:
                messagebox.showinfo("You Lost!","You Lost, the game will close once you press OK. The answer was {0}".format(select[0].name))
                root.destroy()

    
    check = Button(root, text="Verify!", font=("Bold", 7), fg="Black", width=8, height=0,command=check)
    check.place(x=305, y=5)

    entry = Entry(root, textvariable= user, font=("Bold", 10), fg="red", width=36)
    entry.place(x=47, y=5)

    # Clues

    hair = Button(root,text="Hair",font=("Bold", 7), fg="Black",command=hairClue)
    hair.place(x=35, y=30)

    eyes = Button(root, text="Eyes", font=("Bold", 7), fg="Black", command=eyeClue)
    eyes.place(x=5, y=30)

    height = Button(root, text="Height", font=("Bold", 7), fg="Black", command=heightClue)
    height.place(x=60, y=30)

    gender = Button(root, text="Gender", font=("Bold", 7), fg="Black",command=genderClue)
    gender.place(x=95, y=30)

    glasses = Button(root, text="Glasses", font=("Bold", 7), fg="Black",command=glassesClue)
    glasses.place(x=131, y=30)

    enter = Label(root, text="Enter: ")
    enter.place(x=5, y=5)
    
    lives = Label(root, text="Lives:", font=("Bold", 10), fg="Red")
    lives.place(x=310, y=30)

    btnPass = Button(root, text="Pass", font=("Bold", 7), fg="Black",command=passgame)
    btnPass.place(x=270, y=30)

    v = StringVar()
    v.set(guesses)
    
    guessText = Label(root, textvariable=v, font=("Bold", 10), fg="Red")
    guessText.place(x=350, y=30)

def quit(): #Quit function
    exit()

def instruct():
    messagebox.showinfo("Instructions","Upon starting the game you will get a new window. Click each button for a clue, this will tell you something new about them. If you think you know who it is, type it in the text box. Every name MUST start with a capital.")

window.geometry("250x130")
window.configure(background='purple')

start = Button(window, text="Start Game", font=("Bold", 10), fg="Black", width=29, height=0,command=Start)
start.place(x=5,y=5)

options = Button(window, text="Options", font=("Bold", 10), fg="Black", width=29, height=0)
options.place(x=5,y=35)

instructions = Button(window, text="Instructions", font=("Bold", 10), fg="Black", width=29, height=0,command=instruct)
instructions.place(x=5,y=65)

btexit = Button(window, text="Exit Game", font=("Bold", 10), fg="Black", width=29, height=0,command=quit)
btexit.place(x=5,y=95)

window.mainloop()







    
