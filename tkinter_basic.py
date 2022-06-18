import tkinter

root = tkinter.Tk()
root.withdraw()

from tkinter import simpledialog as sd, filedialog as fd

my_string = sd.askinteger(title="Hello", prompt="Please enter a string.")

print(my_string)

my_filename = fd.askopenfilename(title="Please choose a file.")
print(my_filename)