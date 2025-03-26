import tkinter as tk

window = tk.Tk()

#per vedere il gestore di geometria - GRID

frame1_1 = tk.Frame(master=window, borderwidth=1, relief=tk.GROOVE)
frame1_1.grid(row=1, column=1)
label1_1 = tk.Label(master=frame1_1, text="riga 1, colonna 1")
label1_1.pack()

frame1_2 = tk.Frame(master=window, borderwidth=1, relief=tk.GROOVE)
frame1_2.grid(row=1, column=2)
label1_2 = tk.Label(master=frame1_2, text="riga 1, colonna 2")
label1_2.pack()



window.mainloop()