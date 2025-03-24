import tkinter as tk

window = tk.Tk()

border_effects = {
                "flat":tk.FLAT,
                "sunken":tk.SUNKEN,
                "raised":tk.RAISED,
                "groove":tk.GROOVE,
                "ridge":tk.RIDGE,
                }

frame_a = tk.Frame(relief=tk.GROOVE, borderwidth=5)
frame_b = tk.Frame(relief=tk.RIDGE, borderwidth=5)
frame_a.pack(side=tk.LEFT)
frame_b.pack(side=tk.LEFT)

saluto_1 = tk.Label(
                text="***Ciao a tutti***", 
                font=("Courier", 20),
                bg="black",
                fg="#53a8bd",
                master=frame_a
                # width=20,
                # height=10
                )
saluto_2 = tk.Label(
                text="***ARRIVEDERCI***", 
                font=("Courier", 20),
                bg="black",
                fg="#53a8bd",
                master=frame_b
                # width=20,
                # height=10
                )

entry_1 = tk.Entry(
                    fg="yellow",
                    bg="blue",
                    width=50,
                    master=frame_a
                    )

button_1 = tk.Button(
                text="-----BUTTON-----", 
                font=("Courier", 20),
                bg="black",
                fg="#53a8bd",
                width=20,
                height=10,
                master=frame_a,
                relief=tk.RAISED,
                borderwidth=10
                )

button_2 = tk.Button(
                text="-----PULSANTE-----", 
                font=("Courier", 20),
                fg="black",
                bg="#53a8bd",
                width=20,
                height=10,
                master=frame_b,
                relief=tk.RAISED,
                borderwidth=10
                )

saluto_1.pack()
saluto_2.pack()
entry_1.pack()
button_1.pack()
button_2.pack()


window.mainloop()  #ESEGUE L'EVENT LOOP - tkinter cercherà input 
