import tkinter

window=tkinter.Tk()
window.title("GUI")

tkinter.Label(window,text="Welcome to Python!").pack()

tkinter.Button(window,text="Click Me").pack()
window.mainloop()