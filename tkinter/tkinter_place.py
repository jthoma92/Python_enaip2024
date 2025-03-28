import tkinter as tk

window = tk.Tk()

#per vedere il gestore di geometria - PLACE

frame = tk.Frame(master=window, width=300, height=200)
frame.pack()

label1 = tk.Label(master=frame, text="questo è 0, 0", bg="green", fg="white")
label1.place(x=0, y=0)

label2 = tk.Label(master=frame, text="questo è 100, 100", bg="blue", fg="white")
label2.place(x=100, y=100)

window.mainloop()