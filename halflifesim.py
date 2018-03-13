import tkinter as tk
from tkinter.messagebox import *

#Create class for radioactive isotope objects
class RadioactiveIsotope:
    def __init__(self, name, mass, half_lives):
        self.name = name
        self.mass = mass
        self.half_lives = half_lives

#Write the half-life function, for when user clicks "Half-life" for isotope
def half_life(isotope, output, choice):
    if isotope.mass > 0.0 and isotope.mass < 1.0:
        output.set("This isotope has had enough.")
    else:
        isotope.mass /= 2
        isotope.half_lives += 1
        if isotope.half_lives == 1:
            output.set("After " + str(isotope.half_lives) + " half-life," \
                   + "The current mass of this isotope is: " \
                    + str(isotope.mass) + " g.")
        else:
            output.set("After " + str(isotope.half_lives) + " half-lives," \
                   + "The current mass of this isotope is: " \
                    + str(isotope.mass) + " g.")

#Write the clear definition, which resets everything to initial values
def clear(isotope_list, output, choice):
    for iso in isotope_list:
        iso.mass = iso.mass * 2 ** iso.half_lives
        iso.half_lives = 0
    output.set("")
    choice.set(0)
        
#Create window, give it a title, and specify window dimensions
master = tk.Tk()
master.title("Half-life Simulator v1.0")
master.geometry("775x250+30+30")

#Intialize instructions docstring
instruct = """
Welcome to the Half Life Simulator!  Please select a radioactive
isotope from the list with its radio button, and press Half-Life
button to see what it's mass is after one half-life.  You can
keep pressing the Half-Life button to keep halving the mass of the
isotope selected.  The molar mass of each isotope is in it's name
(e.g. Uranium-238).  Each isotope will always start out with its
molar mass before you click "Half-life."  The Clear button will
set the selected isotope back to Promethium-145, give back the
masses of all radioactive isotopes, and set the output back to
nothing.  Click the Quit button to quit.
"""

showinfo(title="Half-life Simulator v1.0: Instructions", \
         message=instruct)

#initialize isotopes list
isotopes=[RadioactiveIsotope("Promethium-145", 145.0, 0), \
          RadioactiveIsotope("Polonium-209", 209.0, 0), \
          RadioactiveIsotope("Francium-223", 223.0, 0), \
          RadioactiveIsotope("Uranium-236", 236.0, 0), \
          RadioactiveIsotope("Plutonium-244", 244.0, 0), \
          RadioactiveIsotope("Berkelium-247", 247.0, 0), \
          RadioactiveIsotope("Einsteinium-252", 252.0, 0), \
          RadioactiveIsotope("Lawrencium-262", 262.0, 0), \
          RadioactiveIsotope("Meitnerium-276", 276.0, 0), \
          RadioactiveIsotope("Roentgenium-281", 281.0, 0)]

#Include our radiation symbol in window
photo=tk.PhotoImage(file='radiation_symbol.gif')
symbol = tk.Text(master, height=13, width=31)
symbol.place(x=20, y=20)
symbol.image_create(1.0, image=photo)

#Place the instructions for picking a radioactive isotope
instructions = tk.Label(master, text = "Please select a radioactive isotope: ")
instructions.place(x=275, y=20)

#Create "choice" variable for selecting radioactive isotope
choice = tk.IntVar()
out = tk.StringVar() #output variable for changing output in label box

#Place listbox containing radioactive isotopes
pos = 0
for i in isotopes:
    tk.Radiobutton(master, text=i.name, \
                variable=choice, \
                value=pos).place(x=275, y=pos*20+35)
    pos+=1
    
#Create the textbox where the simulation actually happens with scrollbar
output = tk.Label(master, width=24, height=13, textvariable=out, bg='white', \
                   wraplength=100)

#Place the textbox in appropriate place
output.place(x=575,y=20)

#Create frames for all three controls
frame_one = tk.Frame(master).place(x=450, y=80)
frame_two = tk.Frame(master).place(x=450, y=110)
frame_three = tk.Frame(master).place(x=450, y=140)

#Place control buttons 'half-life', 'clear' and 'quit'
hlButton = tk.Button(frame_one, text="Half-life", fg='black', \
                      bg='yellow', width=10, \
                     command=lambda: half_life(isotopes[choice.get()],
                                               out,\
                                               choice)).place(x=475, y=80)

clrButton = tk.Button(frame_two, text="Clear", width=10, \
                       command=lambda: clear(isotopes,\
                                               out,\
                                               choice)).place(x=475, y=110)
                      
quiButton = tk.Button(frame_three, text="Quit", command=master.destroy, \
                       width=10).place(x=475, y=140)

master.mainloop()

